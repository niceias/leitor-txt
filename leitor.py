import os
import sys

print("Escolha o Modelo de Gabarito: ")
print("Regular (1)" "\n" 'Adaptada (2)' '\n'"Olimpiada (3)" '\n' "Olimpiada Adapatada (4)")

gab = input('Informe o modelo de Gabarito: ')
gab = int(gab)

if(gab > 4):
   sys.exit("Programa encerrado por digitar um valor invalido!!")
else:
    caminho = input("digite o caminho do arquivo: ")
    destino = input("Informe o destino do arquivo ")

    while True:
        print("################################################")
        print(f'Origem: {caminho}')
        print(f'Destino: {destino}')
        print("################################################")
        doc = input("Nome do txt: ")
        arquivo = open(caminho + "\\" + doc + ".txt")
        leitura = arquivo.readlines()


        lista = []
        nlista = []
        nova = []
        proc = []

        for valor in leitura:
            lista.append(valor)


        if (gab == 1):
            for item in lista:
                a = item[0:19]
                b = item[19:29]
                c = item[29:]
                car = ';A;'
                ponto = ';'
                nova = (a + ponto + b + car + c)
                proc.append(nova)


            with open(destino + "\\" + doc + '.txt', 'w') as arquivo:
                for valor in proc:
                    arquivo.write(valor.strip() + '\n')
            os.system('cls')

        elif(gab == 2):
            for item in lista:
                a = item[0:19]
                b = item[19:29]
                c = item[29:]
                car = ';A;'
                caradp = 'A;'
                ponto = ';'
                nova = (a + caradp + b + car + c)
                proc.append(nova)


            with open(destino + "\\" + doc + '.txt', 'w') as arquivo:
                for valor in proc:
                    arquivo.write(valor.strip() + '\n')
            os.system('cls')

        elif (gab == 3):
                for item in lista:
                    a = item[0:20]
                    b = item[20:30]
                    c = item[30:]
                    car = ';A;'
                    ponto = ';'
                    nova = (a + ponto + b + car + c)
                    proc.append(nova)


                with open(destino + "\\" + doc + '.txt', 'w') as arquivo:
                    for valor in proc:
                       arquivo.write(valor.strip() + '\n')
                os.system('cls')

        elif (gab == 4):
            for item in lista:
                a = item[0:20]
                b = item[20:30]
                c = item[30:]
                car = ';A;'
                caradp = 'A;'
                ponto = ';'
                nova = (a + caradp + b + car + c)
                proc.append(nova)


            with open(destino + "\\" + doc + '.txt', 'w') as arquivo:
                for valor in proc:
                    arquivo.write(valor.strip() + '\n')
            os.system('cls')

