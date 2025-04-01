#!/bin/bash

echo "PyTest ..."

source ${ROBOTOLOGY_SUPERBUILD_INSTALL_DIR}/share/robotology-superbuild/setup.sh

ICUB_HOSTS_ENTRY="$ICUB_IP icub-head"

# Check if the entry already exists
if grep -Fxq "$ICUB_HOSTS_ENTRY" /etc/hosts
then
    echo "iCub entry already exists in /etc/hosts"
else
    # Add the entry to /etc/hosts
    echo "$ICUB_HOSTS_ENTRY" | sudo tee -a /etc/hosts > /dev/null
    echo "iCub entry added to /etc/hosts"
fi

YARP_FORWARD_LOG_ENABLE=0 yarpserver --write &
sleep 2

yarprun --server /$ICUBSRV_NODE --log &
sleep 2

gzserver /workdir/apps/gazebo/icub-world.sdf &
sleep 4

yarprobotinterface --context gazeboCartesianControl --config no_legs.xml --portprefix /icubSim
# sleep 4

# iKinGazeCtrl --context gazeboCartesianControl --from iKinGazeCtrl.ini &
# sleep 2

# iKinCartesianSolver --context gazeboCartesianControl --part right_arm &

# iKinCartesianSolver --context gazeboCartesianControl --part left_arm &

# pytest -v

