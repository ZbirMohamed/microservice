from fastapi import FastAPI 
import asyncio
from concurrent.futures import ThreadPoolExecutor
from routers.router import router
from services.services import listen_to_redis
executor = ThreadPoolExecutor()


app = FastAPI()

app.include_router(router, prefix="/service", tags=["discovery_service"])

@app.get('/')
async def get_health():
    return {"health":"healthy","status":200}


## la methode est deprycate on peut utiliser lifespan a travers une injection de depandence
## mais puique ce n'est qu'un test je vais utiliser on_event
@app.on_event("startup")
async def startup_event():
    asyncio.create_task(listen_to_redis()) 