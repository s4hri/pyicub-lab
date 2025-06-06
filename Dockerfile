# MIT License
#
# Copyright (c) 2025 Social Cognition in Human-Robot Interaction
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

ARG DOCKER_SRC=ubuntu:latest
FROM $DOCKER_SRC

ARG LOCAL_USER_UID=1000
ARG LOCAL_USER_GID=1000
ARG LOCAL_USER_NAME=icub
ARG ROBOT_CODE="/usr/local/src/robot"

ENV ROBOT_CODE=$ROBOT_CODE

USER root

# Install custom dependencies
# RUN apt-get update && \
#     apt-get install -y --no-install-recommends \
#     sudo \
#     rm -rf /var/lib/apt/lists/*


# Create group with specified GID
RUN if getent group "$LOCAL_USER_NAME" >/dev/null 2>&1; then \
        CURRENT_GID=$(getent group "$LOCAL_USER_NAME" | cut -d: -f3); \
        if [ "$CURRENT_GID" -ne "$LOCAL_USER_GID" ]; then \
            echo "Updating GID of $LOCAL_USER_NAME from $CURRENT_GID to $LOCAL_USER_GID"; \
            groupmod -g "$LOCAL_USER_GID" "$LOCAL_USER_NAME"; \
        fi; \
    else \
        echo "Creating group $LOCAL_USER_NAME with GID $LOCAL_USER_GID"; \
        groupadd -g "$LOCAL_USER_GID" "$LOCAL_USER_NAME"; \
    fi

# Create user with UID and assign to the correct GID
RUN if id "$LOCAL_USER_NAME" >/dev/null 2>&1; then \
        CURRENT_UID=$(id -u "$LOCAL_USER_NAME"); \
        if [ "$CURRENT_UID" -ne "$LOCAL_USER_UID" ]; then \
            echo "Updating UID of $LOCAL_USER_NAME from $CURRENT_UID to $LOCAL_USER_UID"; \
            usermod -u "$LOCAL_USER_UID" -g "$LOCAL_USER_GID" "$LOCAL_USER_NAME"; \
        fi; \
    else \
        echo "Creating user $LOCAL_USER_NAME with UID $LOCAL_USER_UID and GID $LOCAL_USER_GID"; \
        useradd -m -s /bin/bash -u "$LOCAL_USER_UID" -g "$LOCAL_USER_GID" "$LOCAL_USER_NAME"; \
    fi && \
    gpasswd -a "$LOCAL_USER_NAME" sudo && \
    gpasswd -a "$LOCAL_USER_NAME" audio && \
    echo "$LOCAL_USER_NAME ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers


ENV PATH=$PATH:/home/${LOCAL_USER_NAME}/.local/bin

RUN echo "Fixing permissions for /home/$LOCAL_USER_NAME"; \
    chown -R "$LOCAL_USER_UID:$LOCAL_USER_GID" "/home/$LOCAL_USER_NAME" && \
    chown -R "$LOCAL_USER_UID:$LOCAL_USER_GID" "$ROBOT_CODE"

USER $LOCAL_USER_NAME

CMD ["bash"]

