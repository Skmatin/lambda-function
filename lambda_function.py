import boto3
import os
from datetime import datetime
from zoneinfo import ZoneInfo

ec2 = boto3.client("ec2", region_name=os.environ.get("AWS_Region", "us-east-1"))

BUSINESS_START = int(os.environ.get("BUSINESS_START", 9))
BUSINESS_END = int(os.environ.get("BUSINESS_END", 18))
TIMEZONE = os.environ.get("TIMEZONE", "Asia/Kolkata")

def lambda_handler(event, context):
    now = datetime.now(ZoneInfo(TIMEZONE))
    current_hour = now.hour
    print(f"Current time: {now}, Hour: {current_hour}")

    if current_hour < BUSINESS_START or current_hour >= BUSINESS_END:
        print("Outside business hours. Checking for instances to stop...")
        filters = [
            {"Name": "tag:AutoStop", "Values": ["true"]},
            {"Name": "instance-state-name", "Values": ["running"]}
        ]

        resp = ec2.describe_instances(Filters=filters)
        instance_ids = [
            i["InstanceId"]
            for r in resp.get("Reservations", [])
            for i in r.get("Instances", [])
        ]

        if instance_ids:
            print(f"Stopping instances: {instance_ids}")
            ec2.stop_instances(InstanceIds=instance_ids)
        else:
            print("No running instances found with AutoStop tag.")
    else:
        print("Within business hours. No action taken.")

    return {"status": "success"}                                                                                                                        else:
                                                                                                                                    print("Within business hours. No action taken.")

                                                                                                                                        return {"status": "success"}

