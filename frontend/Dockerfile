FROM node:18

WORKDIR /app

COPY package*.json ./
RUN npm install
RUN npm install axios

COPY . .

CMD ["npm", "start"]
