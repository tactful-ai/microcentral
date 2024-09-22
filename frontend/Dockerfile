FROM node:alpine

WORKDIR /app
# Copy the package.json and package-lock.json files
COPY package*.json ./
# Install the dependencies
RUN npm install

COPY . .

RUN npm run build

EXPOSE 3000

CMD ["npm", "start"]