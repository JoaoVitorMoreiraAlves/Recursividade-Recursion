def fat(num):
    #Calcular o fatorial utilizando da recursividade
    if num == 0: return 1
    return num * fat(num-1)