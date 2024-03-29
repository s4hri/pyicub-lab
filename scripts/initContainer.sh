#!/bin/bash

echo "DOCKYMAN -> Running inizialization script (docker container)"

source ${ROBOTOLOGY_SUPERBUILD_INSTALL_DIR}/share/robotology-superbuild/setup.sh

YARP_FORWARD_LOG_ENABLE=0 yarpserver --write --ip $ICUBSRV_IP --socket $ICUBSRV_PORT &
sleep 1

if ! $ICUB_SIMULATION ; then
  sshpass -p $ICUB_PSW ssh -o StrictHostKeyChecking=no $ICUB_USER@$ICUB_IP "yarprun --server /"$ICUB_HOST" --log &" &
fi

yarprun --server /$ICUBSRV_HOST --log &

yarpmanager --apppath ${ICUB_APPS}/applications --from ${ICUB_APPS}/applications/cluster-config.xml

if ! $ICUB_SIMULATION ; then
  sshpass -p $ICUB_PSW ssh -o StrictHostKeyChecking=no $ICUB_USER@$ICUB_IP "killall -9 yarprun"
  sshpass -p $ICUB_PSW ssh -o StrictHostKeyChecking=no $ICUB_USER@$ICUB_IP "killall -9 yarpdev"
fi
