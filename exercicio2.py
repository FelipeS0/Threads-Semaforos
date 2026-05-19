#2. Quatro pessoas caminham, cada uma em um corredor diferente. Os 4 corredores terminam
#em uma única porta. Apenas 1 pessoa pode cruzar a porta, por vez. Considere que cada
#corredor tem 200m. e cada pessoa anda de 4 a 6 m/s. Cada pessoa leva de 1 a 2 segundos
#para abrir e cruzar a porta. Faça uma aplicação que simule essa situação.
import multiprocessing
import random
import time
semaforo = None
pessoa = None
def init(sem, pes):
 global pessoa
 global semaforo
 semaforo = sem
 pessoa = pes
 
def caminhar(id):
    time.sleep(random.uniform(0, 1))
    global pessoa 
    dist: int = 200
    dist_perc: int = 0
    rand: int = random.randint(4, 6)
    temp: int = random.randint(1, 2)
    while dist_perc < dist: 
        dist_perc+= rand
    with semaforo:
        pessoa.value+= 1
        print (f'A pessoa {id} foi a {pessoa.value}ª que passou na porta')
        time.sleep(temp)
        
def main():
 pessoas: int = 0    
 param: int = [0]*4
 pes: int = 0
 sem = None
 
 pes = multiprocessing.Value('i', 0)
 
 for pessoas in range(4):
     param[pessoas] = (pessoas + 1)
    
 with multiprocessing.Manager() as manager:
      sem = manager.Semaphore(1)
      with multiprocessing.Pool(processes= 4, initializer= init, initargs=(sem, pes)) as pool:
          pool.map(caminhar, param)
         
    
if __name__ == '__main__':
    main()