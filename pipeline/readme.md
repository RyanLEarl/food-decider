# CI/CD Pipeline

## Overview

The Pipeline service provides cloudformation templates for creating an AWS CodePipeline setup for managing CI/CD. The CI/CD process will:
  - Build and deploy services
  - Update Cloudformation stacks
  - Sync log files with S3 buckets for learning documents and CI/CD artifacts

## Sub-Prod Environments

1.  Replace the project name in the **template.yml** file. Configure any additional permissions needed for project, if you need more than the defaults. You can also remove any unecessary ones.
2.  From the root folder, build the CI/CD by running this command: `npm run build-cicd --stage={env}`  (WINDOWS run `npm run build-cicd-windows --stage={env}`)
3.  If after building the CI/CD you change anything in the template.yml, you can update the CI/CD by running: `npm run update-cicd --stage={env}`  (WINDOWS run `npm run update-cicd-windows --stage={env}`)
   
**NOTE:** *You will need aws-cli setup and configured locally. Documentation: https://docs.aws.amazon.com/polly/latest/dg/setup-aws-cli.html.*
**NOTE:** *If you are experiencing issues, try running the commands in Git Bash*

