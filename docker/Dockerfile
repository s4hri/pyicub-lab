ARG DOCKER_SRC

FROM $DOCKER_SRC

LABEL maintainer="Davide De Tommaso <davide.detommaso@iit.it>"

ARG PYICUB_VER

USER icub

RUN cd /home/icub && mkdir pyicub-lab;


RUN cd /home/icub/pyicub-lab && \
    git clone https://github.com/s4hri/pyicub -b ${PYICUB_VER} && \
    cd pyicub && \
    pip3 install -r requirements.txt;

ENV PATH=$PATH:/home/icub/.local/bin
ENV PYTHONPATH $PYTHONPATH:/home/icub/pyicub-lab/pyicub
ENV YARP_COLORED_OUTPUT 1
ENV YARP_FORWARD_LOG_ENABLE 1

CMD ["/bin/bash", "-c", "terminator & bash /home/icub/init.sh"]
