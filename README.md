## Problema del barbero durmiente

El problema consiste en una barbería en la que trabaja un barbero que tiene un único sillón de barbero y varias sillas para esperar. Cuando no hay clientes, el barbero se sienta en una silla y se duerme. Cuando llega un nuevo cliente, éste o bien despierta al barbero o —si el barbero está afeitando a otro cliente— se sienta en una silla (o se va si todas las sillas están ocupadas por clientes esperando). El problema consiste en realizar la actividad del barbero sin que ocurran condiciones de carrera. La solución implica el uso de semáforos y objetos de exclusión mutua para proteger la sección crítica. 

## Diagrama de flujo
![Sin título_0](https://user-images.githubusercontent.com/107761268/228122564-c9c4295f-a822-43a4-9516-1e9193e25ce9.jpg)

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
## Video de explicacion

[Hacer clic para haceder a video](https://drive.google.com/file/d/1Bv_bkh8quZ9Ymurjqzo0vZCQ5-nKR88c/view?usp=sharing)


## Creador
Nombre: Esteban Pacheco

Matricula: 2021-1076
