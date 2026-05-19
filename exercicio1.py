#Para tal, usar uma variável sentido, que será alterado pela Thread que controla cada carro (4 carros)
#com a movimentação do carro. Quando a Thread tiver a possibilidade de ser executada, ela
#deve imprimir em console o sentido que o carro está passando. Só pode passar um carro por
#vez no cruzamento.
import multiprocessing
import random
import time

sem = None
sentido: int = 0
def init(s, sent):
    global sem
    global sentido
    sem = s
    sentido = sent
    
def cruzamento(id):
    time.sleep(random.uniform(0, 1))
    dist_perc: int = 0
    cruzamento: int = 0
    direção: str = ''
    cruzamento = random.randint(1000, 3000)      
    while dist_perc < cruzamento:
        dist_perc = dist_perc + 16.67
    with sem:
        if id == 1:
            direção = 'Norte'
        if id == 2:
            direção = 'Sul'
        if id == 3:
            direção = 'Leste'
        if id == 4:
            direção = 'Oeste'       
        print (f'O carro {id} passou no cruzamento no sentido {direção}')
        time.sleep(1)
    
    

def main():
    params: int = [0]*4
    for sentido in range(4):
        params[sentido] = (sentido + 1)
    sent = multiprocessing.Value('i', 0)
    
    with multiprocessing.Manager() as manager:
        sem = manager.Semaphore(1)
        with multiprocessing.Pool(processes= 4, initializer= init, initargs=(sem, sent)) as pool:
            pool.map(cruzamento, params)
            
if __name__ == '__main__':
    main()            
    