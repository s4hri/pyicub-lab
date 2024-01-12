# MIT License
#
# Copyright (c) 2023 Social Cognition in Human-Robot Interaction
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

FROM node:21
ARG PYICUB_FRONTEND_VERSION=master
RUN mkdir /app
WORKDIR /app
 
RUN git clone https://github.com/s4hri/pyicub-frontend -b master tmp
 
RUN cd tmp && git checkout ${PYICUB_FRONTEND_VERSION}
RUN cp -a tmp/. /app/pyicub-frontend/
RUN rm -rf tmp
# Define work directory
WORKDIR /app/pyicub-frontend
RUN npm install
 
CMD npm run production -- --port ${PYICUB_API_FRONTEND_PORT}