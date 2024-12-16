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

"""
@app.get('/service/{service_name}')
async def get_Service(service_name:str,req:Request,instance:int = 1):
    
    #check si la requête parvient d'un load balancer ou d'un service enregistrer
    x_forwarded_for = req.headers.get("X-Forwarded-For")
    x_from_load_balancer = req.headers.get('X-From-Load-Balancer')
    
    #alors si l'une des deux existe ca signifie que c'est un load balancer
    if x_forwarded_for or x_from_load_balancer:
        return

    #l'instance est declarer par defaut 1 ce qui signifie si le serveur n'a pas d'instance duplique vous aurez le premier element enregistrer  
    required_service = get_service(service_name,instance)

    if not required_service:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="No Service with such name")

    return required_service

@app.post('/register/{service_name}',status_code=status.HTTP_200_OK)
async def register_service(address:str , service_name:str):

    instance = get_service_instances(service_name) #valeur  par defaut 1
    service_instance = f"{service_name}:{instance}"

    return add_service(service_instance,address,instance) 

@app.post('/refresh/{service_name}',status_code=status.HTTP_202_ACCEPTED)
async def refresh_Status(service_name:str,instance:int = 1):
    
    service_instance = f"{service_name}:{instance}"
    refresh_service(service_instance)

    return {"message":f"service {service_instance} refreshed"} """

## la methode est deprycate on peut utiliser lifespan a travers une injection de depandence
## mais puique ce n'est qu'un test je vais utiliser on_event
@app.on_event("startup")
async def startup_event():
    asyncio.create_task(listen_to_redis()) 