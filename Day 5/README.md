Terraform Setup and Usage
Overview:
This README provides instructions for setting up and using Terraform to provision and manage cloud resources. The steps include installing Terraform, creating configuration files, initializing and applying configurations, and managing state.

Prerequisites
Terraform installed
Cloud provider account (e.g., AWS, Azure, GCP)
Necessary permissions to create and manage resources
Installing Terraform
### Step 1: Download Terraform
Go to the An external link was removed to protect your privacy..
Download the appropriate package for your operating system.
### Step 2: Install Terraform
Extract the downloaded package.
Move the terraform binary to a directory included in your system's PATH.
### Step 3: Verify Installation
Open a terminal.
Run the following command to verify the installation:
terraform --version


Creating Terraform Configuration Files
### Step 1: Create a Directory
Create a new directory for your Terraform project.
Navigate to the directory.
### Step 2: Create a Configuration File
Create a new file named main.tf.
Define the provider and resources.

Initializing and Applying Configurations
### Step 1: Initialize Terraform
Open a terminal and navigate to your project directory.
Run the following command to initialize Terraform:
terraform init

### Step 2: Plan the Configuration
Run the following command to see the execution plan:
terraform plan

### Step 3: Apply the Configuration
Run the following command to apply the configuration:
terraform apply

Confirm the action when prompted.

Managing State
### Step 1: Check State
Run the following command to view the current state:
terraform show

### Step 2: Refresh State
Run the following command to refresh the state:
terraform refresh

### Step 3: Destroy Resources
Run the following command to destroy the resources:
terraform destroy


Confirm the action when prompted.


![Screenshot 2025-04-14 151638](https://github.com/user-attachments/assets/4da70938-a252-48b8-bcd2-82954db4cbae)


