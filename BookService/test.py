from dotenv import load_dotenv  
import os
import requests
import time
import threading


load_dotenv('.env',override=True)

def register(func):
    async def inner(*args,**kwargs):
        try:
            load_dotenv('.env',override=True)
            
            register_service:str = os.getenv("DISCOVERY_REGISTERY_URL")
            service_name:str = os.getenv("APPLICATION_NAME")
            port:int = os.getenv("PORT")
            file_path:str = os.getenv("INSTANCE_PATH")
            
            request:str = f"{register_service}"
            
            demande = {
            "service_name":service_name,
            "address":f"http://localhost:{port}"
            }

            response  = requests.post(request,timeout=5,json=demande)
            data = response.json()
            
            write_instance(file_path,data["instance"])
        
            print("Registring to the discovery service")
            if response.status_code != 200:
                raise Exception("The discovery service is down")

            if not register_service:
                raise Exception("the app is lacking the registery service url")

            print("Votre service est bien registrer")
            await func()
        except Exception as e:
            print(e)
            return 
        return "Hello World"
    return inner

def send_request():
    while True: 
        try:  
            time.sleep(20)
            url = "http://localhost:8761/service/refresh"

            service_name = os.getenv("APPLICATION_NAME")
            
            instance = read_instance()

            demande = {
                "service_name":service_name,
                "instance":instance
            }

            response = requests.post(url,timeout=5,json=demande)
            print(f"Requête envoyée, statut: {response.status_code}")

            if response.status_code != 200:
                raise Exception("The discovery service is down")
        except Exception as e:
            print(e)
            return

def start_background_thread():
    thread = threading.Thread(target=send_request, daemon=True)
    thread.start()



#####" utilities" ########

def write_instance(file_path:str="instance.txt",instance:int=1) -> None:
    if not os.path.exists(file_path):
        with open(file_path, 'w') as file:
            file.write(f"instance={instance}")
            print(f"Le fichier {file_path} a été créé avec des données vides.")
        return
    file.write(f"instance={instance}")
    return

def read_instance(file_path:str) -> int:
    if not os.path.exists(file_path):
        print("le fichier d'instance a ete supprimer")
        return
    with open(file_path, 'r') as file:
        data = file.read() 
        return int(data)