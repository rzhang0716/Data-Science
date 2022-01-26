# AWS Cloud Practitioner Certificate Preparation
## Identity and Access Management (IAM)
1. Users & Groups: Users are people within your organization, and can be grouped; Groups only contain users, not other groups; Users don't have to belong to a group, and user can be belong to multiple groups. 
2. Permissions: Users or Groups can be assigned JSON documents called policies (aka permissions); AWS apply the least privilege princie: don't give more permissons than a user needs. Policies are inheritance. 
3. AWS CLI: (1) A tool that enables users to interact with AWS services using commands in your command-line shell; (2) Direct access to the public APIs of AWS services; (3) Develop scripts to manage your resources; (4) Open-source; (5) Alternative to using AWS Management Console.
4. AWS SDK: (1) AWS Software Development Kit; (2) Language-specific APIs (set of libraries); (3) Enables you to access and manage AWS services programmatically; (4) Embedded within your application. 
5. IAM Roles for Services: Some AWS service will need to perform actions on user's behalf, users will assign permissions to AWS services within IAM Roles. Common roles are (1) EC2 Instance Roles; (2) Lambda Function Roles; (3) Roles for CloudFormtion.
