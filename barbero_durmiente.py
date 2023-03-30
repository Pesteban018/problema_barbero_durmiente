import threading
import time
import random

MAX_CLIENTES = 5
clientes = []  # lista que almacena los clientes

# creamos los semáforos y el lock
sem_clientes = threading.Semaphore(0)
sem_sillon = threading.Semaphore(0)
lock = threading.Lock()
print("Barbero durmiendo...")
# función que representa al barbero
def barbero():
    while True:
        
        sem_clientes.acquire()  # el barbero espera a que llegue un cliente
        lock.acquire()  # el barbero toma el lock para proteger la sección crítica
        cliente = clientes.pop(0)  # el barbero toma el primer cliente de la lista
        lock.release()  # el barbero libera el lock
        print(f"Barbero está cortando el pelo del cliente {cliente}")
        time.sleep(random.randint(1, 3))  # tiempo que tarda el barbero en cortar el pelo
        sem_sillon.release()  # el barbero libera el sillon para que el cliente se levante
        
# función que representa a un cliente
def cliente(num):
    global clientes
    time.sleep(random.randint(1, 5))  # tiempo que tarda en llegar un cliente
    print(f"El cliente {num} ha llegado")
    lock.acquire()  # el cliente toma el lock para proteger la sección crítica
    if len(clientes) < MAX_CLIENTES:  # si hay espacio, el cliente se sienta
        clientes.append(num)
        print(f"El cliente {num} se sienta en la sala de espera")
        lock.release()  # el cliente libera el lock
        sem_clientes.release()  # se despierta al barbero
        sem_sillon.acquire()  # el cliente espera a que el sillon esté libre
        print(f"El cliente {num} se levanta del sillon")
    else:  # si no hay espacio, el cliente se va
        print(f"La sala de espera está llena. El cliente {num} se va")
        lock.release()  # el cliente libera el lock

# creamos el hilo del barbero
barbero_hilo = threading.Thread(target=barbero)

# creamos los hilos de los clientes
clientes_hilos = [threading.Thread(target=cliente, args=(i,)) for i in range(10)]

# Creamos un objeto de tipo Thread que ejecutará la función barbero en un hilo separado. target=barbero indica que la función barbero será el objetivo (target) que se ejecutará en el hilo.
barbero_hilo.start()
for hilo in clientes_hilos:
    hilo.start()

# Iniciamos la ejecución de los hilos de los clientes en un bucle, llamando al método start() de cada objeto Thread en la lista clientes_hilos.
barbero_hilo.join()
for hilo in clientes_hilos:
    #Esperamos a que todos los hilos de los clientes terminen su ejecución, llamando al método join() de cada objeto Thread en la lista clientes_hilos
    hilo.join()
