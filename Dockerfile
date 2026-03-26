FROM node:18-alpine

WORKDIR /app

COPY package*.json ./
RUN npm install --omit=dev

COPY . .

RUN mkdir -p /data && chmod 777 /data

EXPOSE 3000

CMD ["node", "app.js"]
