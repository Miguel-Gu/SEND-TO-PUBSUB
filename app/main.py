from fastapi import FastAPI, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.logger import logger
from app.models import UsuarioEntrada
from app.publisher import publish_data

app = FastAPI()


@app.get("/")
def root():
    return {"message": "ok"}


@app.post("/novousuario")
def post_usuario(payload: UsuarioEntrada):
    try:
        payloadDict = jsonable_encoder(payload)
        logger.info(payloadDict)
        publish_data(payloadDict)

    except Exception as error:
        logger.warning(f"Error - {error}")

    return JSONResponse(status_code=status.HTTP_200_OK, content="Data send with sucess")
