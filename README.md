# <REPLACE_PROJECT_NAME>

## Introduction
Run npm install and then navigate to pipeline/readme for next steps

## Architecture Diagrams

![architecture](./readme-resources/<REPLACE_ARCHITECTURE>)

## Dependencies
### This Project Requires the Use of Several Resources
Serverless: npm install -g serverless@3.39.0 & npm install serverless@3.39.0
## Git Management

With proper setup, the CI/CD process should be automated. This process requires managing sourcecode through git and the use of webhooks to trigger that automation through the AWS CodePipeline. 

## Serverless Commands

### Full Deploy

You can deploy the serverless project by merging changes into your CI/CD targeted github branch or manually in your cli.<br>
`serverless deploy`<br>
**NOTE:** you will need your AWS_PROFILE that you setup in the CI/CD Pipeline instructions.

### Partial Deploy

At times during development you may wish to deploy changes to just one lambda. To do this run the following:<br>
`serverless deploy -f <REPLACE_FUNCTION_NAME>`<br>

