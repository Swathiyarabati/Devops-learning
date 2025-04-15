AWS Lambda Function and Pipeline Setup
Overview:
This README provides instructions for creating an AWS Lambda function and setting up a pipeline to manage and deploy the function. The steps include creating the Lambda function, configuring triggers, and setting up a CI/CD pipeline.

Prerequisites
AWS account with necessary permissions
AWS CLI installed and configured
Terraform installed
Azure DevOps account
Creating an AWS Lambda Function
### Step 1: Navigate to Lambda Service
Open the AWS Management Console.
Navigate to the Lambda service.

### Step 2: Create a Lambda Function
Click on "Create Function".
Provide a name for your function.
Select a runtime (e.g., Python, Node.js, Java, etc.).
Write or upload your code.

### Step 3: Configure Triggers
Configure triggers or test with a sample event.
Triggers can be events from AWS services like S3, API Gateway, EventBridge, etc.
### Step 4: Save and Deploy
Save and deploy the function.



![Screenshot 2025-04-10 200832](https://github.com/user-attachments/assets/45e7ec28-7e72-40be-8662-6789d086d2eb)





Setting Up a CI/CD Pipeline
### Step 1: Create a New Repository
Create a new repository in Azure DevOps.
Push your Terraform code into the repository.
### Step 2: Create a Build Pipeline
In Azure DevOps, create a new build pipeline.
Point the pipeline to the azure-pipelines.yml file in your repository.
### step 3: Deploy the Pipeline
Save and run the pipeline.
Monitor the pipeline for any errors and ensure the Docker containers and Kubernetes deployments are created successfully.





![Screenshot 2025-04-10 210706](https://github.com/user-attachments/assets/bb7626ef-3384-47a6-a3f5-433c56450e8b)

