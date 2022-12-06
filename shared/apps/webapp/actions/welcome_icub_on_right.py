
# BSD 2-Clause License
#
# Copyright (c) 2022, Social Cognition in Human-Robot Interaction,
#                     Istituto Italiano di Tecnologia, Genova
#
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, this
#    list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

from pyicub.helper import iCub, JointPose, GazeMotion, PyiCubCustomCall, JointsTrajectoryCheckpoint, LimbMotion, ICUB_PARTS, iCubFullbodyAction, iCubFullbodyStep

def my_action():
    action = iCubFullbodyAction()
    g1 = GazeMotion(lookat_method="lookAtAbsAngles")
    g1.addCheckpoint([0.0, 8.0, 3.0])
    g1.addCheckpoint([-25.0, 8.0, 3.0])

    speech = PyiCubCustomCall(target="speech.say", args=["Ciao, io sono aicab. Cominciamo a giocare?"])

    pose_up   = JointPose(target_joints=[-84.00, 93.0, 0.0], joints_list=[0,1,2])
    pose_down   = JointPose(target_joints=[-26.90, 46.40, 31.35], joints_list=[0,1,2])

    up   = JointsTrajectoryCheckpoint(pose_up, duration=2.0)
    down = JointsTrajectoryCheckpoint(pose_down, duration=2.0)
    mRX = LimbMotion(ICUB_PARTS.RIGHT_ARM)
    mRX.addCheckpoint(up)
    mRX.addCheckpoint(down)

    step1 = iCubFullbodyStep()
    step2 = iCubFullbodyStep()
    step3 = iCubFullbodyStep()
    step1.setGazeMotion(g1)
    step2.setLimbMotion(mRX)
    step2.addCustomCall(speech)
    mRX = LimbMotion(ICUB_PARTS.RIGHT_ARM)
    mRX.addCheckpoint(down)
    step3.setGazeMotion(g1)
    action.addStep(step1)
    action.addStep(step2)
    action.addStep(step3)


    return action

icub = iCub()

action = my_action()
icub.play(action)
action.exportJSONFile('json/welcome_icub_on_right.json')
