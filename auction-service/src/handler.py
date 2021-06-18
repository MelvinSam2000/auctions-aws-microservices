import json
import datetime
import boto3
import uuid

dynamodb = boto3.client("dynamodb")

def createAuction(event, context):

    req_body = json.loads(event["body"])

    if not "title" in req_body:
        return json.dumps({
            "statusCode": 201,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": {
                "error": "No Auction title provided"
            }
        })

    auction = {
        "id": {
            "S": str(uuid.uuid4())
        },
        "title": {
            "S": req_body["title"]
        },
        "status": {
            "S": "OPEN"
        },
        "createdAt": {
            "S": datetime.datetime.now().isoformat()
        },
    }

    dynamodb.put_item(
        TableName="AuctionsTable",
        Item=auction
    )

    response = {
        "statusCode": 201,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": auction
    }

    return json.dumps(response)

