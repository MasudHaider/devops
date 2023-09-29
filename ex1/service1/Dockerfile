FROM node:14

WORKDIR /usr/src/app

COPY package*.json ./

RUN npm install
RUN mkdir -p /usr/src/app/logs

COPY . .

EXPOSE 8001

CMD ["node", "service1.js"]