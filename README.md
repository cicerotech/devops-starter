## Overview

This repository contains a starter code for DevOps excercise

## Setup
**Note**: If you are using Cicero provided laptop, this is already setup for you ! Skip to `Excercise` 

1. Install `brew` -> `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`
1. Run `brew update`
1. Install required applications 
 `brew install --cask google-chrome firefox iterm2 visual-studio-code docker rectangle` 
1. Install `mise` -> `curl https://mise.run | sh` Follow instructions to make it available in all shells. `mise doctor` to verify installation
1. Install default python & node `mise use -g python@3.10` & `mise use -g node@22` 
1. Install [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)


## Excercise
You are tasked with containerizing and deploying a Python-based REST API application that manages a book inventory system to AWS. The application consists of a FastAPI backend service and a PostgreSQL database.

### Time Allocation (2.5 hours total)

- Setup and familiarization: 20 minutes
- Exercise completion: 90 minutes
- Present and discuss solution: 30 minutes

### Deliverables

- Working containerized application deployed on AWS
- Infrastructure as Code  - Please pick whichever IaC is required eg: Pulumi / Terraform / AWS CDK
- CI/CD pipeline configuration

### Notes
- Focus on building a production-ready solution
- Make reasonable assumptions where requirements are unclear
- Feel free to ask questions or discuss with the team during the exercise
- Document any assumptions made

### Starting Point
You are provided with:

1. A Python application using FastAPI framework
2. Unit and integration tests
3. Basic documentation of the API endpoints
4. Access to necessary AWS credentials. Ask a team member for help to login if session expires
  - `aws sso login --sso guest-user-sso`
  - use profile `--profile guest-power-user` for aws commands. for eg, `aws s3 ls --profile guest-power-user` 

### Running the application
1. 


