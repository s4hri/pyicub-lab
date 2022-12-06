#   Copyright (C) 2021  Davide De Tommaso
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <https://www.gnu.org/licenses/>
from pyicub.helper import iCubFullbodyAction
from utilities import RobotCam

#from utilities import cameraView, fillAction

import yarp
import json
import os
from pyicub.helper import iCubRESTApp


class WebApp(iCubRESTApp):

    #CWD = os.getcwd()
    CWD = os.getcwd()
    PATH_ACTIONS = CWD + "/actions/json/"
    PATH_GUI     = CWD + "/GUI/"

    def __init__(self, name):
        iCubRESTApp.__init__(self, app_name=name)

        self.port = yarp.BufferedPortBottle()
        self.port.open("/" + name + ":o")
                
        ## JSON
        self.introGUI    = self.__getIntroGUI__()
        self.actionsName = self.__getActionsName__()
        self.actions     = self.__loadActions__()

        ## Status
        self.intros     = None


    # PRIVATE METHODS
    def __getIntroGUI__(self):
        with open (self.PATH_GUI + "/intro.json") as f:
            data = f.read()
        return json.loads(data)

    def __getActionsName__(self):
        actionsName = []
        filenames = sorted(os.listdir(self.PATH_ACTIONS))
        for filename in filenames:
            actionsName.append(filename.split('.json')[0])
        return actionsName

    def __loadActions__(self):
        actions = {}
        for actionName in self.actionsName:
            JSON_action = self.PATH_ACTIONS + "%s.json" % actionName
            ## for pyicub after fix (6.2.x)
            #actions[actionName] = self.icub.createAction(JSON_file=JSON_action) => doesn't work!!
            actions[actionName] = iCubFullbodyAction(JSON_file=JSON_action)
            self.icub._logger_.debug("action founded: %s" % (actionName))
        return actions
        

    # API
    def IntroGUI(self):
        return self.introGUI

    def SetIntros(self, intros):
        print(len(intros))
        introList = []
        introObj = {}
        for intro in intros.keys():
            introObj = {intro : intros[intro]}
            introList.append(introObj)
        self.intros = introList
        return True
    
    def GetIntros(self):
        print("intros",self.intros)
        return self.intros

    def Actions(self):
        return self.actionsName

    def ExecuteAction(self, action):
        self.icub.play(self.actions[action])
        return True

    def Camera(self):
        cam = RobotCam(self.icub._robot_name_)
        res     = cam.getResolution()
        portNum = cam.getPortNum()
        return [portNum, res[0], res[1]]

    def ClickCamera(self, pixelX, pixelY):
        bot = self.port.prepare()
        bot.clear()
        bot.addInt32(pixelX)
        bot.addInt32(pixelY)
        self.port.write()
        self.icub._logger_.debug("pixel clicked: %s %s" % (pixelX, pixelY))
        return True
        
    def ChatBox(self, msg):
        self.icub.speech.say(msg)
        return True

app = WebApp(name="pywebapp")

app.icub.rest_manager.run_forever()