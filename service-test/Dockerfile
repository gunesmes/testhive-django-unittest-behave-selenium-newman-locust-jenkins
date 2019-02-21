FROM node:6.5.0-slim

RUN npm install newman
RUN npm install newman-reporter-html

RUN mkdir /newman
WORKDIR /newman


ENTRYPOINT ["/node_modules/.bin/newman"]