from fastapi import FastAPI
from app.routers import user as ur
from app.routers import task as tr

app = FastAPI(swagger_ui_parameters={'tryItOutEnabled': True})


@app.get('/')
async def welcome():
    return {"message": "Welcome to the materials for solving tasks for the EGE  in computer science"}

app.include_router(tr.router)
app.include_router(ur.router)
