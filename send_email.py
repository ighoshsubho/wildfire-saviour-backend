import boto3
from botocore.exceptions import ClientError
from dotenv import load_dotenv, find_dotenv
from getLocation import getLocation
import os
# Replace sender@example.com with your "From" address.
# This address must be verified with Amazon SES.

load_dotenv(find_dotenv())

def send_message():
    SENDER = "SENDER EMAIL"
    TO = "SENDING EMAIL"
    AWS_REGION = "ap-south-1"
    SUBJECT = "Wild Fire Detected!"
    BODY_TEXT = ("Wildfire Detected!!\r\n"
                "Here are the Coordinates! "
                "Lat and Long - {}".format(getLocation())
                )
    BODY_HTML = f"""<html>
                    <head></head>
                    <body>
                    <h1>WildFire Detected! Track the coordinates here!</h1>
                    <p>Your coordinate location is - {getLocation()}</p>
                    </body>
                    </html>
            """  
    CHARSET = "UTF-8"
    client = boto3.client('ses',region_name=AWS_REGION, aws_access_key_id=f"{os.getenv('AWS_ACCESS_KEY_ID')}",
            aws_secret_access_key= f"{os.getenv('AWS_SECRET_ACCESS_KEY')}")
    try:
        response = client.send_email(
            Destination={
                'ToAddresses': [
                    TO,
                ],
            },
            Message={
                'Body': {
                    'Html': {
                        'Charset': CHARSET,
                        'Data': BODY_HTML,
                    },
                    'Text': {
                        'Charset': CHARSET,
                        'Data': BODY_TEXT,
                    },
                },
                'Subject': {
                    'Charset': CHARSET,
                    'Data': SUBJECT,
                },
            },
            Source=SENDER,
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print("Email sent! Message ID:"),
        print(response['MessageId'])

send_message()
