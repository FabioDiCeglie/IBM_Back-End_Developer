# Image Deployment and Application Setup Guide

This guide will walk you through the process of deploying an image to an IBM Container Registry (ICR) and setting up an application on IBM Cloud Code Engine.

## Prerequisites

Before you begin, ensure you have the following:

- Access to an IBM Container Registry
- Docker installed on your local machine
- IBM Cloud CLI installed and configured
- A GitHub repository to store your code and documentation

## Steps

### 1. Determine Your IBM Container Registry Namespace

To find your IBM Container Registry namespace, execute the following command in your terminal:

```bash
echo ${SN_ICR_NAMESPACE}
```

### 2. Build the Docker Image

Build the Docker image using the provided Dockerfile:

```bash
docker build -t pictures .
```

### 3. Tag the Image

Tag the image with your IBM Container Registry namespace:

```bash
docker tag pictures us.icr.io/$SN_ICR_NAMESPACE/pictures:1
```

### 4. Push the Image to the Registry

Push the tagged image to your IBM Container Registry namespace:

```bash
docker push us.icr.io/$SN_ICR_NAMESPACE/pictures:1
```

### 5. Verify Image Push

Confirm that the image has been successfully pushed by listing images in your namespace:

```bash
ibmcloud cr images --restrict $SN_ICR_NAMESPACE
```

### 6. Deploy the Application on Code Engine

Create the application on IBM Cloud Code Engine, specifying the image from your IBM Container Registry and necessary configurations:

```bash
ibmcloud ce app create --name pictures --image us.icr.io/${SN_ICR_NAMESPACE}/pictures:1 --registry-secret icr-secret --port 3000
```

### 7. Access the Application

Once the application is deployed, you will receive a URL. Access this URL in your browser and append a valid path to test the microservice, e.g., `/count` or `/health`.

### 8. Retrieve Application URL

If you lose the application URL, you can retrieve it by listing all applications:

```bash
ibmcloud ce application list
```