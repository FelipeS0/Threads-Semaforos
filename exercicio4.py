#4. Você foi contratado para automatizar um treino de Fórmula 1. As regras estabelecidas pela
#direção da prova são simples:
#“No máximo 5 carros das 7 escuderias[equipes] (Cada escuderia tem 2 carros diferentes,
#portanto, 14 carros no total) presentes podem entrar na pista simultaneamente, mas apenas
#um carro de cada equipe. O segundo carro deve ficar à espera, caso um companheiro de
#equipe já esteja na pista. Cada piloto deve dar 3 voltas na pista. O tempo de cada volta deverá
#ser exibido.
import multiprocessing
import random
import time
import math

semáforo = None
semáforo_carro = None
carros = None
def init(sem,  sem_car, car):
 global semáforo
 global carros
 global semáforo_carro
 semáforo = sem
 semáforo_carro = sem_car
 carros = car
 
def treino_f1(id_car):
    time.sleep(random.uniform(0, 1))
    pista: int = 6300
    velocidade: int = 0
    vel_ms: int = 0
    dist_perc: int = 0
    tempos: int = [0]*3
    min: int = 0
    volta: int = 0
    equipe = math.ceil(id_car / 2)
    with semáforo:
        with semáforo_carro[equipe - 1]:
            print (f'O carro {id_car} da equipe {equipe} entrou na pista')
            for volta in range(3):
                dist_perc = 0
                while dist_perc < pista:
                 velocidade = random.randint(250, 315)
                 dist_perc+= velocidade
                vel_ms = (velocidade * 1000) / 3600 
                tempos [volta] = pista / vel_ms
                if tempos[volta] > 60:
                   min = 1
                   tempos[volta] = tempos[volta] - 60  
                   print (f'O carro {id_car} deu uma volta de {min}:{tempos[volta]:.2f} segundos')
            print (f'O carro {id_car} saiu da pista')    
                
def main():
    carros: int = 0
    param: int = [0]*14
    car: int = 0
    sem = None
    car = multiprocessing.Value('i', 0)
    
    for carros in range(14):
        param[carros] = carros + 1
    
    with multiprocessing.Manager() as manager:
        sem = manager.Semaphore(5)
        sem_car = [manager.Semaphore(1) for sem_car in range(7)]
        with multiprocessing.Pool(processes=14, initializer=init, initargs= (sem, sem_car, car)) as pool:
            pool.map(treino_f1, param)
            
if __name__ == '__main__':
    main()    