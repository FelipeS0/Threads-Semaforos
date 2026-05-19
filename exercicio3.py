#Fazer uma aplicação de uma corrida de sapos, com 5 Threads, cada Thread controlando 1 
#sapo. Deve haver um tamanho máximo para cada pulo do sapo (em centímetros) e a distância 
#máxima para que os sapos percorram. A cada salto, um sapo pode dar um salto de 0 até o 
#tamanho máximo do salto (valor aleatório entre 1 e 5 cm.). Após dar um salto, a Thread, para 
#cada sapo, deve mostrar no console, qual foi o tamanho do salto e quanto o sapo percorreu. 
#Assim que o sapo percorrer a distância máxima, a Thread deve apresentar a posição que 
#o sapo chegou.

import multiprocessing 
import time
import random

semáforo = None
sapos = None
def init(sem, sap):
   global semáforo
   global sapos
   semáforo = sem
   sapos = sap   

def corrida(id): 
    time.sleep(random.uniform(0, 1))
    global sapos
    pulo: int = 0
    dist_perc: int = 0
    dist: int = 250
    while dist_perc < dist:
        pulo = random.randint(1, 5)
        dist_perc+= pulo
        print (f'O sapo {id} pulou {pulo} e percorreu {dist_perc} metros')
    with semáforo:
        sapos.value+= 1
        print (f'o sapo {id} chegou na posição {sapos.value}')
def main():
  sapos: int = 0
  param: int = [0]*5
  sem: int = 0      
      
  sap = multiprocessing.Value('i', 0)
  
  for sapos in range(5):
      param[sapos] = sapos + 1
  
  with multiprocessing.Manager() as manager:
      sem = manager.Semaphore(1)
      with multiprocessing.Pool(processes=5, initializer= init, initargs= (sem, sap)) as pool:
          pool.map(corrida, param)          

if __name__ == '__main__':
    main()