# `DVA-C02`

# `AWS Well-Architected Framework`

- Operational excellence
- Security
- Reliability	
- Performance efficiency
- Cost optimization
- Sustainability

## The Shared Responsibility Model
**CUSTOMER** (Responsible for the security *in* the cloud)

- Customer Data
- Platform, Apps, IAM
- OS, Network & Firewall Configuration
- Client-side data encryption & data integrity authentication
- Server-side encryption
- Network Traffic Protection

**AWS** (Responsible for the security *of* the cloud)

- Software
- Compute, Storage, Database, Networking
- Hardware
- Regions, AZs, Edge locations

# `Identity & Access Management`

- Offers a centralized hub of control within AWS and integrates with all other AWS Services 
- Allows you to manage users and their level of access to the AWS console.

>When you create a new account the *root user* will be created which will have all permissions and access to all the resources. 
**It's very important to secure your root user**

- `User` : Individual AWS user.
    - 5000 IAM users limit per account.
    - Any IAM user can only be member of 10 groups.

- `Groups` : Collection of similar people with shared permissions & users will inherit permissions from the group.

    **It's best to inherit permissions from groups so that you don't have to manage them individually**

- `Roles` : Any software service that needs to be granted permissions to do its job. 

    It's similar to IAM user, however instead of being assiciated with one person , a role is intended to be assumed by anyone who needs it. Roles are temporary. Also generate temporary credentials for the user.

    *Two types of policies are attached to a role :*
    - Trust Policy : Who can assume this role?
    - Permission Policy : What can they do after assuming the role?

- `Policies` : A policy is an JSON file in AWS that, when associated with an identity or resource, defines their permissions.
    - Inline : Assign policy individually
    - Managed : Assign different identities to single policy.

- `ARN` : Amazon Resource Name
    - arn:partition:service:region:account-id:resource-id
    - arn:partition:service:region:account-id:resource-type:resource-id
    - arn:partition:service:region:account-id:resource-type:resource-id

#### Permission Priority
>*Explicit Deny > Explicit Allow > Default(Implicit Deny)*

#### IAM Security Tools
- **IAM Credentials Report** (account-level) - lists all of the users and the status of their credentials
- **IAM Access Advisor** (user-level) - shows the service permissions granted to a user and when those services were last accessed.

# `Elastic Compute Cloud`

It's just VMs with on-demand price and scalable compute capacity option.
>You will be charged for the AMI, Instance Type, EBS Volume, Networking, IOs, Snapshots.

**Creating KeyPair for ec2 does not cost anything*

**Pricing Options** : 
- *On-Demand Instance* : 
    - No upfront payment or long-term commitment, just pay by the hour.
    - Used for Application with short-term , spiky or unpredictable workloads that cannot be interrupted.
- *Spot Instance* : 
    - Uses spare EC2 capacity that is available for less than the On-Demand price.
    - The Spot price of each instance type in each Availability Zone is set by Amazon EC2, and is adjusted gradually based on the long-term supply of and demand for Spot Instances.
    - Your Spot Instance runs whenever capacity is available.
        >To terminate your spot instances you need to first cancel the spot request and then terminate the instances.
```
                            |<----------- Start <-------------------- Stop
                            |                                           ^
                            |  |-------- Interrupt -------------------| |                            
                            |  |                                      | |
           Create req ---> Spot req -----------> Launch-instances ---> VMs
                            |                                           |
                            |                                           |
                         Request                                     Interrupt
                         failed
```
- *Dedicated Hosts* : 
    - An Amazon EC2 Dedicated Host is a physical server fully dedicated for your use.
    - Amazon EC2 Dedicated Hosts allow you to use your eligible software licenses from vendors such as Microsoft and Oracle on Amazon EC2, so that you get the flexibility and cost effectiveness of using your own licenses, but with the resiliency, simplicity and elasticity of AWS. 

## Instance States
| Instance state  | Description                                                                                                                                                                                 | Billing                                                           |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| `pending`       | The instance is preparing to enter the `running` state. An instance enters the pending state when it launches for the first time, or when it is started after being in the `stopped` state. | Not billed                                                        |
| `running`       | The instance is running and ready for use.                                                                                                                                                  | Billed                                                            |
| `stopping`      | The instance is preparing to be stopped or stop-hibernated.                                                                                                                                 | Not billed if preparing to stop. Billed if preparing to hibernate |
| `stopped`       | The instance is shut down and cannot be used. The instance can be started at any time.                                                                                                      | Not billed                                                        |
| `shutting-down` | The instance is preparing to be terminated.                                                                                                                                                 | Not billed                                                        |
| `terminated`    | The instance has been permanently deleted and cannot be started.                                                                                                                            | Not billed                                                        |

# `Simple Storage Service`

**S3 billing factors :**
- Amount of data(in GiB) stored.
- No. of data retrieval options that you execute(Ex: GET, POST etc).
- Data Transfer modes and regions.
- Type of Storage Management and Analytics tool that you choose to adopt.
- Replication.
- No. of transition from diff classes.
- Amount of data processed by S3 Object Lambda.
- What region or AZ you choose to run your workload in.

>*Get 5GB s3 storage if free tier eligible*

# `CloudFormation`

Provisions resources based on the template you provide.

*JSON & YAML are used to create CloudFormation templates.*

> Resource is the mandatory field in the template.

**Template ex :**
```yaml
AWSTemplateFormatVersion: "version date"

Description:
    String(Free Text)
Metadata:
    template metadata
Parameters:
    set of parameters
Mappings:
    set of mappings
Conditions:
    set of conditions
Transform:
    set of transforms
Resources:
    set of resources
Outputs:
    set of outputs
```

A stack is a collection of AWS resources that you create and manage as a single unit using a CloudFormation template.

***when you upload a yaml template file then it creates a new s3 bucket and stores the template in the cloud**

# `CloudWatch`

Amazon CloudWatch is basically a metrics repository. 

An AWS service puts metrics into the repository, and you retrieve statistics based on those metrics. 

If you put your own custom metrics into the repository, you can retrieve statistics on these metrics as well.

---
**High Availability :** Minimize any outages

**Fault Tolerance :** Operate through faults

**Disaster Recovery :** Used when HA & FT don't work

---
# `Domain Name Server`

DNS Client : your laptop, phone, tablet etc.

Resolver : software on your device, or a server which queries DNS on your behalf

Zone : A part of DNS Database 

Zonefile : physical database for a zone 

Nameserver : where zonefiles are located 

Root Hints : config points at the root servers IPs and addresses

Root Server : hosts the DNS root zone 

Root Zone : points at TLD authoritative servers

gTLD : generic top level domain (.com .org)

ccTLD : country-code top level domain (.au .in)
