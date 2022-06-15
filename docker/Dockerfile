# MIT License
#
# Copyright (c) 2022 Social Cognition in Human-Robot Interaction
#                    Author: Davide De Tommaso (davide.detommaso@iit.it)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

ARG DOCKER_SRC
FROM $DOCKER_SRC

LABEL maintainer="Davide De Tommaso <davide.detommaso@iit.it>"

ARG RELEASE=master
ARG PYICUB_BRANCH=master

WORKDIR /home/icub

USER icub

ENV PATH=$PATH:/home/icub/.local/bin

RUN cd /home/icub && \
    git clone https://github.com/s4hri/pyicub -b ${PYICUB_BRANCH} && \
    cd pyicub && \
    git checkout ${RELEASE} && \
    pip3 install -r requirements.txt

ENV PYTHONPATH $PYTHONPATH:/home/icub/pyicub
ENV YARP_COLORED_OUTPUT 1
ENV ICUB_SIMULATION true
ENV ICUB_USER icub
ENV ICUB_PSW icub
ENV ICUB_HOST icub-head
ENV ICUB_IP 10.0.0.2
ENV ICUBSRV_HOST=icubsrv
ENV ICUBSRV_IP=10.0.0.1
ENV ICUB_APPS=/usr/local/src/robot/applications
ENV PYICUB_LOGGING=true
ENV PYICUB_API=false
ENV PYICUB_API_BACKEND_HOST=9000
ENV PYICUB_API_BACKEND_PORT=9001
