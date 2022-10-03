import os

caminho = input("digite o caminho do arquivo: ")

while True:
    doc = input("Nome do txt: ")
    arquivo = open(caminho + doc)
    leitura = arquivo.readlines()


    lista = []
    nlista = []
    nova = []
    proc = []

    for valor in leitura:
        lista.append(valor)

    for item in lista:
        a = item[0:19]
        b = item[19:29]
        c = item[29:]
        car = ';A;'
        ponto = ';'
        nova = (a + ponto + b + car + c)
        proc.append(nova)

    #novoarq = input('Nome: ')
    with open ("C:\\Users\\Niceias\\Desktop\\limpos\\" + doc + '.txt', 'w') as arquivo:
        for valor in proc:
            arquivo.write(valor.strip() + '\n')