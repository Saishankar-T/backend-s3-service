from fastapi import APIRouter, UploadFile, File, HTTPException
from api.lib.client import client_connection,bucket_name
from botocore.exceptions import NoCredentialsError, ClientError

router = APIRouter()

@router.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    try:
        s3_client = client_connection()
        s3_client.upload_fileobj(file.file, bucket_name, file.filename)
        return {"filename": file.filename}
    except NoCredentialsError:
        raise HTTPException(status_code=401, detail="Credentials not available")
    except ClientError as e:
        raise HTTPException(status_code=500, detail=str(e))