from fastapi import HTTPException , status
from redis.exceptions import WatchError
import asyncio
from typing import Dict, List
from database.db import redis_client

services: Dict[str, List[str]] = {}

def get_service(service_instance:str):
    
    required_service_instance = redis_client.hgetall(service_instance)

    return required_service_instance if service_instance else None


def get_service_instances(service_name:str)->int:
    service = services.get(service_name)

    if isinstance(service,list):
        instance = len(service) + 1
        services[service_name].append(f"{service_name}:{instance}")
        return instance

    services[service_name] = [f"{service_name}:1"]
    return 1

def refresh_service(service_instance:str):
    
    service = redis_client.hgetall(service_instance)

    if not service:
        return False

    redis_client.expire(service_instance,30)

    return True

def add_service(service_instance:str,service_address:str,instance:int):
    #pour savoir l'instance actuel

    try:

        with redis_client.pipeline() as pipe:
            pipe.multi()
            pipe.hset(service_instance,mapping={"address":service_address,"healthy":"healthy","instance":str(instance)})
            pipe.expire(service_instance,30)
            #je peux logger les reponses pour debuger
            responses = pipe.execute()
        
        return {'message':f"service {service_instance} registered succefully","instance":instance} 
    
    except WatchError as msg:
        # JE VAIS AJOUTER DU LOGS
        print(msg)
        HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Error while registring ")
    except Exception as e:
        return e


async def listen_to_redis():
    
    def listen():
        pubsub = redis_client.pubsub()
        pubsub.subscribe("__keyevent@0__:expired")  
        print("Listening to Redis topic: __keyevent@0__:expired")
        for message in pubsub.listen():
            if message["type"] == "message":
                print(message)
                print(f"Received message: {message['data']}")
                """ ser_n, inst = message['data'].split(':')
                services[ser_n].remove(f"{ser_n}:{inst}") """
                print("Deleted from the registered services")

    # Run the blocking function in a thread
    await asyncio.to_thread(listen)