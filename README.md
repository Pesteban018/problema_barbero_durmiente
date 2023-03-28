## Problema del barbero durmiente

El problema consiste en una barbería en la que trabaja un barbero que tiene un único sillón de barbero y varias sillas para esperar. Cuando no hay clientes, el barbero se sienta en una silla y se duerme. Cuando llega un nuevo cliente, éste o bien despierta al barbero o —si el barbero está afeitando a otro cliente— se sienta en una silla (o se va si todas las sillas están ocupadas por clientes esperando). El problema consiste en realizar la actividad del barbero sin que ocurran condiciones de carrera. La solución implica el uso de semáforos y objetos de exclusión mutua para proteger la sección crítica. 

## Diagrama de flujo
![Sin título_0](https://user-images.githubusercontent.com/107761268/228122564-c9c4295f-a822-43a4-9516-1e9193e25ce9.jpg)

## Codigo del problema



````
import threading
import time
import random

MAX_CLIENTES = 5
clientes = []  

sem_clientes = threading.Semaphore(0)
sem_sillon = threading.Semaphore(0)
lock = threading.Lock()
print("Barbero durmiendo...")
def barbero():
    while True:
        
        sem_clientes.acquire()  
        lock.acquire()  
        cliente = clientes.pop(0)
        lock.release() 
        print(f"Barbero está cortando el pelo del cliente {cliente}")
        time.sleep(random.randint(1, 3))  
        sem_sillon.release()  
        
def cliente(num):
    global clientes
    time.sleep(random.randint(1, 5)) 
    print(f"El cliente {num} ha llegado")
    lock.acquire()  
    if len(clientes) < MAX_CLIENTES: 
        clientes.append(num)
        print(f"El cliente {num} se sienta en la sala de espera")
        lock.release()  
        sem_clientes.release() 
        sem_sillon.acquire()  
        print(f"El cliente {num} se levanta del sillon")
    else: 
        print(f"La sala de espera está llena. El cliente {num} se va")
        lock.release()  

barbero_hilo = threading.Thread(target=barbero)

clientes_hilos = [threading.Thread(target=cliente, args=(i,)) for i in range(10)]

barbero_hilo.start()
for hilo in clientes_hilos:
    hilo.start()

barbero_hilo.join()
for hilo in clientes_hilos:
   clientes_hilos
    hilo.join()
       

````
## Video de explicacion

[Hacer clic para haceder a video](https://drive.google.com/file/d/1VZuJ6VfyiozN0FQQ6qD9Rts2otAsU5Mj/view?usp=share_link)


## Creador
Nombre: Esteban Pacheco

Matricula: 2021-1076
