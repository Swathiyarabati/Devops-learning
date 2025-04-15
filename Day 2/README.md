## demo app - developing with Docker

This demo app shows a simple user profile app set up using 
- index.html with pure js and css styles
- nodejs backend with express module
- mongodb for data storage

All components are docker-based

### With Docker

#### To start the application

Step 1: Create docker network

    docker network create mongo-network 

Step 2: start mongodb 

    docker run -d -p 27017:27017 -e MONGO_INITDB_ROOT_USERNAME=admin -e MONGO_INITDB_ROOT_PASSWORD=password --name mongodb --net mongo-network mongo    

Step 3: start mongo-express
    
    docker run -d -p 8081:8081 -e ME_CONFIG_MONGODB_ADMINUSERNAME=admin -e ME_CONFIG_MONGODB_ADMINPASSWORD=password --net mongo-network --name mongo-express -e ME_CONFIG_MONGODB_SERVER=mongodb mongo-express   

_NOTE: creating docker-network in optional. You can start both containers in a default network. In this case, just emit `--net` flag in `docker run` command_

Step 4: open mongo-express from browser

    http://localhost:8081

Step 5: create `user-account` _db_ and `users` _collection_ in mongo-express

Step 6: Start your nodejs application locally - go to `app` directory of project 

    cd app
    npm install 
    node server.js
    
Step 7: Access you nodejs application UI from browser

    http://localhost:3000

### With Docker Compose

#### To start the application

Step 1: start mongodb and mongo-express

    docker-compose -f docker-compose.yaml up
    
_You can access the mongo-express under localhost:8080 from your browser_
    
Step 2: in mongo-express UI - create a new database "my-db"

Step 3: in mongo-express UI - create a new collection "users" in the database "my-db"       
    
Step 4: start node server 

    cd app
    npm install
    node server.js
    
Step 5: access the nodejs application from browser 

    http://localhost:3000

#### To build a docker image from the application

    docker build -t my-app:1.0 .       
    
The dot "." at the end of the command denotes location of the Dockerfile.


![Screenshot 2025-04-08 215402](https://github.com/user-attachments/assets/236ddc5e-3ed2-496f-a87a-1added248415)





# Kubernetes Deployment for MongoDB and Web Application

## Overview
This project demonstrates how to deploy MongoDB and a web application using Kubernetes. The deployment includes configuration files for MongoDB and the web application, ensuring they are properly set up and connected within the Kubernetes cluster.

## Prerequisites
- Kubernetes cluster set up and running
- kubectl installed and configured to interact with your Kubernetes cluster

## Project Structure
The project consists of the following YAML files:
- **mongo-deployment.yaml**: Defines the MongoDB deployment.
- **mongo-service.yaml**: Defines the service for MongoDB.
- **mongo-config.yaml**: Contains configuration settings for MongoDB.
- **mongo.yaml**: Combines MongoDB deployment and service configurations.
- **weapp.yaml**: Defines the deployment and service for the web application.

## Steps to Deploy MongoDB and Web Application

### Step 1: Deploy MongoDB
1. **Create MongoDB Deployment**:
   - Apply the `mongo-deployment.yaml` file to create the MongoDB deployment.
   ```sh
   kubectl apply -f mongo-deployment.yaml
   ```
   Create MongoDB Service:

2.Apply the mongo-service.yaml file to create the service for MongoDB.

Configure MongoDB:
Apply the mongo-config.yaml file to set up the necessary configurations for MongoDB.

Combined MongoDB Setup:
Alternatively, you can apply the mongo.yaml file which combines the deployment and service configurations for MongoDB.

### Step 2: Deploy Web Application
Create Web Application Deployment and Service:
Apply the weapp.yaml file to deploy the web application and create its service.

### Step 3: Verify Deployments
Check MongoDB Deployment:
Verify that the MongoDB deployment is running successfully.

Check MongoDB Service:
Verify that the MongoDB service is running and accessible.

Check Web Application Deployment:
Verify that the web application deployment is running successfully.

Check Web Application Service:
Verify that the web application service is running and accessible.

### Step 4: Access the Application
Access MongoDB:

MongoDB will be accessible within the cluster through the service defined in mongo-service.yaml.
Access Web Application:

The web application will be accessible through the service defined in weapp.yaml. You can use the external IP or port specified in the service configuration to access the application.
### Conclusion
This project demonstrates how to deploy MongoDB and a web application using Kubernetes.


![Screenshot 2025-04-15 130224](https://github.com/user-attachments/assets/8a3775fa-991c-4a23-a4b6-93dc4d3f0a0a)
