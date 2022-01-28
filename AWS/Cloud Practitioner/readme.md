# AWS Cloud Practitioner Certificate Preparation
## Identity and Access Management (IAM)
1. Users & Groups: Users are people within your organization, and can be grouped; Groups only contain users, not other groups; Users don't have to belong to a group, and user can be belong to multiple groups. 
2. Permissions: Users or Groups can be assigned JSON documents called policies (aka permissions); AWS apply the least privilege princie: don't give more permissons than a user needs. Policies are inheritance. 
3. AWS CLI: (1) A tool that enables users to interact with AWS services using commands in your command-line shell; (2) Direct access to the public APIs of AWS services; (3) Develop scripts to manage your resources; (4) Open-source; (5) Alternative to using AWS Management Console.
4. AWS SDK: (1) AWS Software Development Kit; (2) Language-specific APIs (set of libraries); (3) Enables you to access and manage AWS services programmatically; (4) Embedded within your application. 
5. IAM Roles for Services: Some AWS service will need to perform actions on user's behalf, users will assign permissions to AWS services within IAM Roles. Common roles are (1) EC2 Instance Roles; (2) Lambda Function Roles; (3) Roles for CloudFormtion.
6. IAM Security Tools: (1) IAM Credential Report (Account Level): A report that lists all your account's users and the status of their various credentials. (2) IAM Access Advisor (user-level): shows the service permissions granted to a user and when those services were last accessed.

## EC2 - Elastic Compute Cloud
1. EC2 mainly covers: (1) Renting Virtual Machines (EC2); (2) Storing data on virtul drives (EBS); (3) Distributing load across machines (ELB); (4) Scaling the services using an auto-scaling group (ASG). 
2. EC2 naming convention: m5.2xlarge, m represents the instance class; 5 represents generation; 2xlagre represents the size within the instance class.
3. EC2 types: 
(1) General Purpose: Great for a diversity of workloads such as web servers or code respositories; 
(2) Computed Optimized: Great for compute-intesive task that require high performance processors (eg: Batch processing workloads, media transcoding, high performance XX, scientific modeling and machine learning). 
(3) Memory Optimized: Fast performance for workloads that process large data sets in memory (eg: distributed web scale cahces stores, in-memory databases optimized for BI); 
(4) Storage optimized: Great for storage-intensive tasks that required high, sequential read and write access to large data sets on local storage (eg: Relational & NoSQL databases, data warehouse applications)
4. Security Groups: 
(1) control how traffic is allowed into or out of our EC2 instances; Only contain allow rules; Can reference by IP or by security group.
(2) Security groups act as "firewall" on EC2 instances. They regulate: (a) Access to Ports; (b) Authorised IP ranges -- IPv4 and IPv6; (c) Control opf inbound network (from other to the instance); (d) Control of outbound network (From the instance to other). (3) Security Groups (a) Can be attached to multiple instances; (b) Locked doiwn to a region/VPC combination; (c) Does live "outside" the EC2; (d) Good to maintain one separate security group for SSH access; (d) If the application is not accessible (time out), then it is a security group issue; (e) If your application gives a "connection refused" error, it is an applicationa error or not launched; (f) All inbound traffic is blocked by defaultu; (g) All outbound traffic is authorised by default. 
