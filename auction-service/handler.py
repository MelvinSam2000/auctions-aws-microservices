import json
import datetime

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
        "title": req_body["title"],
        "status": "OPEN",
        "createdAt": datetime.datetime.now().isoformat()
    }

    response = {
        "statusCode": 201,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": auction
    }

    return json.dumps(response)

