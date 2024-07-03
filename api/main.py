from fastapi import FastAPI
from api.routers import add,download,delete,list
from api.lib.logger import LoggingMiddleware
from starlette.middleware.cors import CORSMiddleware

app = FastAPI(title='''S3 Service''',version="1.0.0",description="We can upload,download and delete a file")

# Add custom logging middleware
app.add_middleware(LoggingMiddleware)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

app.include_router(router=list.router,tags=["List Files"])
app.include_router(router=add.router,tags=["Upload File"])
app.include_router(router=download.router,tags=["Download File"])
app.include_router(router=delete.router,tags=["Delete File"])


