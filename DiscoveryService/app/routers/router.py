# routers/example.py
from fastapi import APIRouter,Request,status , HTTPException
from services.services import add_service,listen_to_redis,get_service,refresh_service,get_service_instances


router = APIRouter()

@router.get('/service_name}')
async def get_Service(service_name:str,req:Request,instance:int = 1):
    
    service_instance = f"{service_name}:{instance}"

    x_forwarded_for = req.headers.get("X-Forwarded-For")
    x_from_load_balancer = req.headers.get('X-From-Load-Balancer')
    
    if x_forwarded_for or x_from_load_balancer:
        return

    required_service = get_service(service_instance)

    if not required_service:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="No Service with such name")

    return required_service

@router.post('/register/{service_name}',status_code=status.HTTP_200_OK)
async def register_service(address:str , service_name:str):

    instance = get_service_instances(service_name) #valeur  par defaut 1
    service_instance = f"{service_name}:{instance}"

    return add_service(service_instance,address,instance) 

@router.post('/refresh/{service_name}',status_code=status.HTTP_202_ACCEPTED)
async def refresh_Status(service_name:str,instance:int = 1):
    
    service_instance = f"{service_name}:{instance}"
    refresh_service(service_instance)

    return {"message":f"service {service_instance} refreshed"}

@router.get("/")
async def read_root():
    return {"message": "Welcome to the example router"}




