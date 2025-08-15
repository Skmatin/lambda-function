# Auto-Stop EC2 Lambda Function

This AWS Lambda function automatically stops EC2 instances outside business hours if they are tagged with `AutoStop=true`.

## Environment Variables

- `AWS_REGION`: Default `us-east-1`
- `BUSINESS_START`: Default `9` (9 AM)
- `BUSINESS_END`: Default `18` (6 PM)
- `TIMEZONE`: Default `Asia/Kolkata`

## IAM Permissions Required

- `ec2:DescribeInstances`
- `ec2:StopInstances`

## How to Deploy

You can deploy this using:
- AWS Console
- AWS CLI + ZIP file

