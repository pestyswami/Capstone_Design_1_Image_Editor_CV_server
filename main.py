from fastapi import FastAPI, File, UploadFile
import uuid
import os
from fastapi.responses import FileResponse
import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as img


app = FastAPI()


@app.get("/")
async def root():
    path = os.getcwd()
    print(path)
    return {"message": "Hello World!"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.post("/image/sharpening")
async def create_upload_file(file: UploadFile):
    content = await file.read()
    filename = f"{str(uuid.uuid4())}.jpg"  # uuid로 유니크한 파일명으로 변경
    with open(os.path.join('./image', filename), "wb") as fp:
        fp.write(content)  # 서버 로컬 스토리지에 이미지 저장 (쓰기)
    return {"filename": filename}


@app.get("/download/{name_file}")
def get_file(name_file: str):
    return FileResponse(path='./image' + "/" + name_file)

