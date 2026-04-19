import os
from fastapi import FastAPI
import uvicorn

from app.exception.exception_handler import ExceptionHandler
from app.router import routers
from app.router.state import router as state_router

app = FastAPI()
app.include_router(state_router)
ExceptionHandler.initiate_exception_handlers(app)

# add routers
for router_module in routers:
    app.include_router(router_module.router)

if __name__ == '__main__':
    port = int(os.getenv("APP_PORT", 8080))  #порт из ENV
    uvicorn.run(app, host="0.0.0.0", port=port)  #слушаем все интерфейсы
