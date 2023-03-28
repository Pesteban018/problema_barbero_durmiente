# Problema del barbero durmiente

## Diagrama de flujo
[Hacer clic para haceder ah la img](https://drive.google.com/file/d/1Bv_bkh8quZ9Ymurjqzo0vZCQ5-nKR88c/view?usp=sharing)

## Codigo del problema


````
import threading 
import time 
import random

clientes = threading.Semaphore(0) 
sillas = threading.Semaphore(5) 
mutex = threading.Semaphore(1) 

class Barbero(threading.Thread): 
    def __init__(self): 
        threading.Thread.__init__(self) 
        
    def run(self): 
        while True: 
            clientes.acquire()  
            sillas.release()    
            mutex.acquire()     
            print("El barbero está cortando el pelo de un cliente") 
            mutex.release()     
            time.sleep(random.uniform(0.5, 1.5))  


class Cliente(threading.Thread): 
        def __init__(self, id): 
        threading.Thread.__init__(self) 
        self.id = id 
    def run(self): 
        print(f"El cliente {self.id} ha llegado a la barbería"
        mutex.acquire()    
        if sillas.acquire(False): 
            print(f"El cliente {self.id} está sentado esperando") 
            clientes.release()    
            sillas.release()        
            mutex.release()         
            clientes.acquire()      
            print(f"El cliente {self.id} ha salido de la barbería"
        else:
            print(f"El cliente {self.id} se fue porque no había sillas de espera")
            mutex.release()         

````
