from fastapi import APIRouter, HTTPException
from api.lib.client import client_connection,bucket_name
from botocore.exceptions import ClientError
from fastapi.responses import StreamingResponse

router = APIRouter()

@router.get("/download/{file_name}")
async def download_file(file_name: str):
    try:
        s3_client = client_connection()
        file_obj = s3_client.get_object(Bucket=bucket_name, Key=file_name)
        return StreamingResponse(file_obj['Body'].iter_chunks(), media_type="application/octet-stream")
    except ClientError as e:
        if e.response['Error']['Code'] == 'NoSuchKey':
            raise HTTPException(status_code=404, detail="File not found")
        raise HTTPException(status_code=500, detail=str(e))