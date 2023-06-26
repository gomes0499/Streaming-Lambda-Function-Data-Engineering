import json
import time
import boto3
from faker import Faker

fake = Faker()

sns = boto3.client("sns")
topic_arn = "arn:aws:sns:us-east-1:222498481656:Topic-91af9c65"

while True:
    for _ in range(100):
        data = {
            "name": fake.name(),
            "email": fake.email(),
            "endereco": fake.address(),
        }
        sns.publish(TopicArn=topic_arn, Message=json.dumps(data))

    time.sleep(0.001)
