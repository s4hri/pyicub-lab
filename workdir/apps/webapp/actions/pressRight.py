  
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

from pyicub.helper import iCub, JointPose, JointsTrajectoryCheckpoint, LimbMotion, ICUB_PARTS, iCubFullbodyAction, iCubFullbodyStep

def my_action():
    action = iCubFullbodyAction()

    pose_press_up   = JointPose(target_joints=[ -6.64], joints_list=[5])
    pose_press_down = JointPose(target_joints=[  5.00], joints_list=[5])
    
    press_up   = JointsTrajectoryCheckpoint(pose_press_up  , duration=0.2, timeout=0.2)
    press_down = JointsTrajectoryCheckpoint(pose_press_down, duration=0.2, timeout=0.2)
    
    mRX = LimbMotion(ICUB_PARTS.RIGHT_ARM)
    mRX.addCheckpoint(press_down)
    mRX.addCheckpoint(press_up)
    
    step1 = iCubFullbodyStep()
    
    step1.setLimbMotion(mRX)

    action.addStep(step1)
    

    return action

icub = iCub()

action = my_action()
icub.play(action, wait_for_completed=False)
action.exportJSONFile('json/pressRight.json')
