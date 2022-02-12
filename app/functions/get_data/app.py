import boto3
import json
import os
import sys
from logging import getLogger, StreamHandler, DEBUG

logger = getLogger(__name__)
handler = StreamHandler()
handler.setLevel(DEBUG)
logger.setLevel(DEBUG)
logger.addHandler(handler)
logger.propagate = False

local_flag = os.getenv("LOCAL_FLAG")
table_name = os.getenv("TABLE_NAME")

if local_flag:
    dynamodb = boto3.resource("dynamodb", endpoint_url="http://dynamodb-local:8000")
    table_name = "local-table"
else:
    dynamodb = boto3.resource("dynamodb")

table = dynamodb.Table(table_name)


def lambda_handler(event, context):

    if "Name" in event["headers"]:
        name = event["headers"]["Name"]
    else:
        logger.info("Specific header is not found.")
        sys.exit()

    resp = table.get_item(Key={"Name": name})

    return {
        "statusCode": 200,
        "body": json.dumps(
            {
                "message": resp,
            }
        ),
    }
