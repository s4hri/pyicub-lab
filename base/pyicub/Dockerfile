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

ARG PYICUB_URL=https://github.com/s4hri/pyicub
ARG PYICUB_BRANCH=master
ARG PYICUB_VERSION=master

ARG PYICUB_APPS_URL=https://github.com/s4hri/pyicub-apps
ARG PYICUB_APPS_BRANCH=master
ARG PYICUB_APPS_VERSION=master

WORKDIR /home/icub

USER icub

ENV PATH=$PATH:/home/icub/.local/bin

RUN cd /home/icub && \
    git clone ${PYICUB_URL} -b ${PYICUB_BRANCH} && \
    cd pyicub && \
    git checkout ${PYICUB_VERSION} && \
    pip3 install -r requirements.txt

RUN cd /home/icub && \
    git clone ${PYICUB_APPS_URL} -b ${PYICUB_APPS_BRANCH} && \
    cd pyicub-apps && \
    git checkout ${PYICUB_APPS_VERSION}

ENV PYTHONPATH $PYTHONPATH:/home/icub/pyicub