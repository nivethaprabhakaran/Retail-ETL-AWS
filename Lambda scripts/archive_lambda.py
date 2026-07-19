import boto3
from datetime import datetime

s3=boto3.client("s3")

BUCKET_NAME="<S3_BUCKET_NAME>"
CURATED_PREFIX="curated/"
ARCHIVE_PREFIX="archive/"
RAW_PREFIX="raw/sales/"
RAW_ARCHIVE_PREFIX="raw/archive/"
PROCESSED_PREFIX="processed/"

def lambda_handler(event, context):
    # TODO: Archive curated files
    # TODO: Archive raw files
    # TODO: Delete processed files
    # TODO: Recreate raw/sales/.keep
    timestamp=datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    return {"status":"SUCCESS","archive_timestamp":timestamp}
