# AWS Cloud Practitioner Certificate Preparation
## Identity and Access Management (IAM)
1. Users & Groups: Users are people within your organization, and can be grouped; Groups only contain users, not other groups; Users don't have to belong to a group, and user can be belong to multiple groups. 
2. Permissions: Users or Groups can be assigned JSON documents called policies (aka permissions); AWS apply the least privilege princie: don't give more permissons than a user needs. Policies are inheritance. 
3. AWS CLI <br> 
(1) A tool that enables users to interact with AWS services using commands in your command-line shell; <br> 
(2) Direct access to the public APIs of AWS services; <br> 
(3) Develop scripts to manage your resources; <br> 
(4) Open-source; <br> 
(5) Alternative to using AWS Management Console.
4. AWS SDK<br> 
(1) AWS Software Development Kit;<br> 
(2) Language-specific APIs (set of libraries); <br> 
(3) Enables you to access and manage AWS services programmatically; <br> 
(4) Embedded within your application. <br> 
5. IAM Roles for Services: Some AWS service will need to perform actions on user's behalf, users will assign permissions to AWS services within IAM Roles. Common roles are (1) EC2 Instance Roles; (2) Lambda Function Roles; (3) Roles for CloudFormtion.
7. IAM Security Tools: (1) IAM Credential Report (Account Level): A report that lists all your account's users and the status of their various credentials. (2) IAM Access Advisor (user-level): shows the service permissions granted to a user and when those services were last accessed.


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
5. Classic Prots: (1) 22 = SSH (Security Shell): Log into a linux instance; (2) 21 = FTP (File Transfer Protocol) - Upload files into a file share; (3) 22 = SFTP (Security File Transfer Protocol) - Upload files using SSH; (4) 80 = HTTP - access unsecured websites; (5) 443 = HTTPS - access secured websites; (6) 3389 = RDP (remote Desktop Protocol) - log into a Windows instance. 
6. EC2 Instance Purchasing Options: (1) On-Demand Instance; (2) Reserved; (3) Spot Instance; (4) Dedicated Hosts; (5) Dedicated Instances.
7. EC2 On Demand: (1) Pay for what you use; (2) Highest cost but no upfront payment; (3) No long-term commitment. Use for short-term and un-interrupted workloads. 
8. EC2 Reserved Instances: (1) Cheaper; (2) Reservation period: one year or 3 year; (3) Purchasing options (no upfront, partial upfront, all upfront); (4) Reserve a specific type; (5) Recommended for steady-state usage applications (database); Also have Convertible Reserved Instance and Scheduled Reserved Instances. 
9. EC2 Spot Instances: (1) Cheapest; (2) Instances that you can 'lose' at any time point of time if your max price is less than the current spot price; (3) The most cost-efficient instances in AWS. Usefor for workloads that are resilient to failure (data Analysis, batch jobs, image processing, distributed works) and not suitable for critical jobs or databases.
10. EC2 Dedicated Hosts: (1) A physical server with EC2 instance capacity fully dedicated to your use. Dedicated hosts can address **complianace requirements** and reduce costs by allowing users to **use your existing server-bound software license**. (2) Allocate for the account for a 3-year period reservation; (3) More expensive; (4) Useful for software that have complicated licensing model (Bring your own license); (5) For companies that have strong regulatory or compliance needs. 
11. EC2 Dedicated Instances: (1) Instances running on hardware that's dedicated to you; (2) May share hardware with other instance in same account; (3) No control over instance placement (can move hardware after stop/start).
12. Shared responsibility model for EC2: For AWS: (1) Infrastructure (global network security); (2) Isolation on physical hosts; (3) Replacing faulty hardware; (4) Compliance validation. For Users: (1) Security Groups rules; (2) Operating-system patches and updates; (3) Software and utilities installed on the EC2 instance; (4) IAM roles assigned to EC2 &IAM user access management; (4) Data security on your instance.
13. EC2 Summary <br>
(1) EC2 Instance: AMI(OS) + Instance Size (CPU + RAM) + Storage + security groups + EC2 User data.<br>
(2) Securtiy Groups: Firewall attached to the EC2 instance.<br>
(3) EC2 user data: Script launched at the first start of an instance.<br>
(4) SSH: Start a terminal into our EC2 Instances (port 22).<br>
(5) EC2 Instance Role: Link to IAM roles.<br>
(6) Purchasing Options: On-Demand, Spot, Reserved (Standard + Convertible + Sceduled), Dedicated Host, Dedicate Instance.


## EC2 Instance Storage Section
1. EBS (Elastic Block Store) Volume is a network drive you can attach to your instances while running.
2. EBS allow your instances to persist data, even after instances termination.
3. EBS can only be mounted to ons instance at a time.
4. EBS are bound to a specific availability zone.
5. Delete on Termination attribute of EBS is to use to preserve root volume when instance is terminated. 
6. EBS Snapshots: (1) Backup of your EBS valume at a point in time; (2) Not neccessary to detach volume to do snapshot, but recommended; (3) Can copy snapshots accross AZ or Region. 
7. AMI (Amazon Machine Image) are customization of an EC2 Instance (add own software, configuration, operating system; faster boot/configuration as required software is pre-package. 
8. AMI are built for a specific region (and can be copied accoss regions).
9. AMI type (use to launch EC2 instances): (1) Public AMI: AWS provided; (2) Own AMI: Own make and maintain; (3) AWS Marketplace AMI: Someone else make/sell.
10. AMI Process (from an EC2 instance): (1) Start an EC2 instance and customize it; (2) Stop the instance (for data integrity); (3) Build an AMI - also create EBS snapshots; (4) Lauch instances from other AMIs. 
11. EC2 Image Builder: (1) Used to automated the creation of Virtual Machines or container images; (2) Automate the creation, maintain, validate and test EC2 AMIs; (3) Can be run on a schedule; (4) Free service. 
12. EC2 Instance Store: (1) Larger valoume compared to the EBS volumes with better performance, especially when you need a high-performance hardware disk; (2) Better I/O performance; (3) EC2 Instance Store lose their storage if they're stopped; (4) Good for buffer/cache/scratch data/temporary content; (5) Risk of data loss if hardware fails; (6) Backups and Replication are users' responsibilities.
13. EFS (Elastic File System): (1) Managed NFS (network file system) that can be mounted on 100s of EC2; (2) EFS only works with Linux EC2 instance in multi-AZ; (3) Highly available, scalable, expensive, pay per use, no capacity planning.
14. EFS-IA (EFS Infrequent Access): is a storage class that is cost-optimized for files not accessed everyday; (1) Up to 92% lower cost compared to EFS standard; (2) EFS will automatically move your files to EFS-IA based on the last time accessed; (3) Enable EFS-IA with a lifecycle policy; (4) Transparent to the applications accessing EFS. 
15. Amazon FSx: Launch 3rd party high-performance file systems on AWS; Fully managed service. 
16. Summary <br> 
(1) EBS vloumes: (1) Network drives attached to one EC2 instance at a time; (2) Mapped to an Availability Zones; (3) Can use EBS Snapshots for backups/transferring EBS volumes across AZ. <br> 
(2) AMI: create ready-to-use EC2 instance with our customizations.<br> 
(3) EC2 Image Builder: Automatically build, test and distribute AMIs.<br> 
(4) EC2 Instance Storage: (1) High Performance hardware disk attached to our EC2; (2) Lost if our instance is stopped/terminated.<br> 
(5) EFS: network file system, can be attached to 100s of instances in a region.<br> 
(6) EFS-IA: cost-optimized storage class for infrequent accessed files.<br> 
(7) FSx For Windows: Network File System for Windows servers.<br> 
(8) FSx for Lustre: High Performance Computing Linux File system.


## Elastic Load Balancing & Auto Scaling Groups Section
1. Scalability: Represents that an application/system can handle greater loads by adapting.
2. Vertical Scalability: Increase the size of the instance; very common for nondistributed systems (such as database); usally a limit to how much you can vertically scale (hardware limit). 
3. Horizontal Scalability: Increasing the number of instances/systems for your application; Implies distributed systems and very common for web applications/morden applications. (Easy on AWS EC2) 
4. High Availability: (1) Hands in hand with horizaontal scaling; (2) High availability means running your application/system in at leaset 2 availability zones; Goal of high availabity is to survive a data center loss (disaster). 
5. High Availability & Scaliability for EC2 (1) Vertical Scaling: Increase instance size. (= scale up/down); (2) Horizontal Scaling: Increase number of instance (= scale out/in) -- Autoscaling Group and Load Balancer; (3) High Availability: Run instances for the same application across multi AZ: AUtp Scaling Group multi AZ and LOad Balancer multi AZ.
6. Scalability vs Elasticity vs Agility <br>
(1) Scalability: ability to accommodate a larger load by making the hardware stronger (scale up), or by adding nodes (scale out); <br>
(2) Elasticity: once a system is scalable, elasticity means that there will be some "auto-scaling" so that the system can scale based on the load.<br>
(3) Agility: new IT resources are only a clikc away, which means that you reduce the time to make those resources available to your developers from weeks to just minutes.
7. Load Balancers: Servers tjat fprward omtermet traffic to multiple servers (EC2 Instances) downstream.
8. Why choose Load Balancer:
(1) Spread load across multiple downstream instansce. <br>
(2) Expose a single point of access (DNS) to your application. <br>
(3) Seamlessly handle failures of downstream instances. <br>
(4) Do regular health checks to your instance. <br>
(5) Provide SSL termination (HTTPS) for your webstie. <br>
(6) High availability across zones. <br>
9. Why choose Elastic Load Balancer
(1) An ELB s a managed load balancer (a) AWS gurantees that it will be working. (b) AWS take care of upgrades, maintenace, high availability. (c) AWS provides only a few configuration knobs<br>
(2) It costs less if set up your own load balancer buyt it will be a lot more effort on your end (maintenance, integrations).<br>
(3) 3 kinds of load balancers offered by AWS: (a) Application Load Balancer (HTTP/HTTPS only) - Layer 7; (b) Network Load Balancer (ultra-high performance allows for TCP) - Layer 4; (c) Classic Load Balancer (slowly retireing) - Layer 4 & 7. 
10.Auto Scaling Group: In really life, the load on your websites and application can change; In the cloud, you can create and get rid of servers very quickly.
11. 
