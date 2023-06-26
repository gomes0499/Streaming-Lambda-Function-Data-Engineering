import json
import boto3

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("dynamo-91af9c65")


def lambda_handler(event, context):
    for record in event["Records"]:
        sns_message = json.loads(record["Sns"]["Message"])
        table.put_item(Item=sns_message)

    return {"statusCode": 200, "body": json.dumps("Dados processados com sucesso!")}
