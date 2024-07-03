import boto3
from os import environ
from dotenv import load_dotenv

load_dotenv()

# Debug: Print environment variables
aws_access_key_id = environ.get("AWS_ACCESS_KEY_ID")
aws_secret_access_key = environ.get("AWS_SECRET_ACCESS_KEY")
aws_region = environ.get("AWS_REGION")
bucket_name = environ.get("S3_BUCKET_NAME")

# Initialize the S3 client
def client_connection():
    try:
        s3_client = boto3.client(
            "s3",
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            region_name=aws_region
        )
        return s3_client
    except ValueError as e:
        print(f"Error creating S3 client: {e}")
        return e