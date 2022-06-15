# MIT License
#
# Copyright (c) 2022 Social Cognition in Human-Robot Interaction
#                    Author: Nicola Severino Russi (nicola.russi@iit.it)
#                            Davide De Tommaso (davide.detommaso@iit.it)
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

FROM node:14.16.1

RUN mkdir /app
WORKDIR /app

# Create react app
RUN npx create-react-app pyicub-frontend

# Define work directory
WORKDIR /app/pyicub-frontend

RUN npm ci
RUN npm install @mui/material @emotion/react @emotion/styled
RUN npm install bootstrap@3
RUN npm install react-iframe
RUN npm install react-router-dom@6
RUN npm i react-icons
RUN npm install http-proxy-middleware --save

RUN mkdir -p /root/.vscode-server /root/.vscode-server-insiders
RUN git clone https://github.com/s4hri/pyicub-frontend -b master tmp
RUN cd tmp && git checkout ${RELEASE}
RUN cp -a tmp/. /app/pyicub-frontend/
RUN rm -rf tmp

CMD ["npm", "start"]
