#Calcula os melhores valores para quatro capacitores arranjados como uma série de dois paralelos, para se mostrar os melhores valores em relação à um de referência

from itertools import product

def series(C1,C2):
    if C1 == 0:
        return C2
    elif C2 == 0:
        return C1
    else:
        return (((C1*10**(-6))*(C2*10**(-6)))/((C1*10**(-6))+(C2*10**(-6))))

def parallel(C1,C2):
    return ((C1*10**(-6))+(C2*10**(-6)))

def show_result(result):
    print(str(result*10**(6)))

def module(n):
    if n < 0:
        return (-n)
    if n >= 0:
        return n

caps = [0, 0.1, 0.22, 0.33, 0.47, 0.56, 0.68, 1, 2.2, 3.3, 4.7, 10] #Valores comerciais dos resistores
capsPermList = []

genComb = product(caps, repeat=4) # aqui e onde tens de especificar o numero de chars que cada combinacao tenha
for subset in genComb:
    capsPermList.append(subset)

capacitanciaDesejada = 3.9*10**(-6)
diferencaMaximaDesejada = .05*10**(-6)


for conj in capsPermList:    
        r = module(capacitanciaDesejada - series(parallel(conj[0],conj[1]),parallel(conj[2],conj[3])))
        if r <= diferencaMaximaDesejada:
            print(f'{r} (R1,R2,R3,R4) = ({conj[0]},{conj[1]},{conj[2]},{conj[3]})') #(R1 || R2) - (R3 || R4)