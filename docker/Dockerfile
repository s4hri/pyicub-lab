ARG DOCKER_SRC

FROM $DOCKER_SRC

LABEL maintainer="Davide De Tommaso <davide.detommaso@iit.it>"

ARG PYICUB_VER

USER icub

RUN cd ${HOME} && mkdir pyicub-lab;


RUN cd ${HOME}/pyicub-lab && \
    git clone https://github.com/s4hri/pyicub -b ${PYICUB_VER};

RUN cd ${HOME}/pyicub-lab && \
    git clone https://github.com/s4hri/yarp-python-tutorials

ENV PATH=$PATH:/home/icub/.local/bin
ENV PYTHONPATH $PYTHONPATH:${HOME}/pyicub-lab/pyicub
ENV YARP_COLORED_OUTPUT 1

CMD ["/bin/bash", "-c", "terminator & bash /home/icub/init.sh"]
