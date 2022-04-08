ARG DOCKER_SRC

FROM $DOCKER_SRC

LABEL maintainer="Davide De Tommaso <davide.detommaso@iit.it>"

ARG PYICUB_VER

WORKDIR /home/icub

USER icub

RUN cd /home/icub && git clone https://github.com/s4hri/pyicub-apps
