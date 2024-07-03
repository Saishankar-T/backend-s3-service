from fastapi import APIRouter, HTTPException
from api.lib.client import client_connection,bucket_name
from botocore.exceptions import ClientError
from fastapi.responses import StreamingResponse

router = APIRouter()
@router.get("/list-files/")
async def list_files():
    try:
        s3_client = client_connection()
        response = s3_client.list_objects_v2(Bucket=bucket_name)
        if 'Contents' in response:
            files = [obj['Key'] for obj in response['Contents']]
        else:
            files = []
        return {"files": files}
    except ClientError as e:
        raise HTTPException(status_code=500, detail=str(e))