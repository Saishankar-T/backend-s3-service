from fastapi import APIRouter, HTTPException
from api.lib.client import client_connection,bucket_name
from botocore.exceptions import ClientError
from fastapi.responses import JSONResponse

router = APIRouter()

@router.delete("/delete/{file_name}")
async def delete_file(file_name: str):
    try:
        s3_client = client_connection()
        s3_client.delete_object(Bucket=bucket_name, Key=file_name)
        return JSONResponse(status_code=200, content="Successfully deleted")
    except ClientError as e:
        if e.response['Error']['Code'] == 'NoSuchKey':
            raise HTTPException(status_code=404, detail="File not found")
        raise HTTPException(status_code=500, detail=str(e))