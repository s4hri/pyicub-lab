
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

from pyicub.helper import iCub, JointPose, GazeMotion, JointsTrajectoryCheckpoint, LimbMotion, ICUB_PARTS, iCubFullbodyAction, iCubFullbodyStep

def my_action():
    action = iCubFullbodyAction()

    pose_init_left  = JointPose(target_joints=[-30.00, 43.20, 31.35, 68.23, 46.00, -6.64, 9.4, 38.25, 27.82, 15.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
    pose_init_right = JointPose(target_joints=[-26.90, 46.40, 31.35, 68.23, 48.00, -6.64, 9.4, 38.25, 27.82, 15.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
    pose_init_torso = JointPose(target_joints=[ -5.00], joints_list=[0])

    init_left  = JointsTrajectoryCheckpoint(pose_init_left)
    init_right = JointsTrajectoryCheckpoint(pose_init_right)
    init_torso = JointsTrajectoryCheckpoint(pose_init_torso)

    g1 = GazeMotion(lookat_method="lookAtAbsAngles")
    g1.addCheckpoint([0.0, 0.0, 3.0])

    mLeft = LimbMotion(ICUB_PARTS.LEFT_ARM)
    mLeft.addCheckpoint(init_left)
    mRight = LimbMotion(ICUB_PARTS.RIGHT_ARM)
    mRight.addCheckpoint(init_right)
    mTorso = LimbMotion(ICUB_PARTS.TORSO)
    mTorso.addCheckpoint(init_torso)

    step1 = iCubFullbodyStep()

    step1.setGazeMotion(g1)
    step1.setLimbMotion(mLeft)
    step1.setLimbMotion(mRight)
    step1.setLimbMotion(mTorso)

    action.addStep(step1)

    return action

icub = iCub()

action = my_action()
icub.play(action)
action.exportJSONFile('json/init.json')
