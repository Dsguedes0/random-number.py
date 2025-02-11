import random

v1 = int(input("Máximo de numeros que serão sorteados? (ex:10)"))
    

if v1 < 100:
    numeros = list(range(1, v1 + 1))
    print(random.choice(numeros))
    
elif v1 == 100:
    print("100")
    
elif v1 > 100:
    numeros = list(range(101, v1 + 1))
    print(random.choice(numeros))
    
else: 
    print("Não foi possivel sortear")
    