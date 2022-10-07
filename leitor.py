import os
import sys

print("Escolha o Modelo de Gabarito: ")
print("Regular (1)" "\n" 'Adaptada (2)' '\n'"Olimpiada (3)" '\n' "Olimpiada Adapatada (4)")

gab = input('Informe o modelo de Gabarito: ')
gab = int(gab)

gabarito_regular = "Modelo de Gabarito: REGULAR"
gabarito_regular_adaptado = "Modelo de Gabarito: REGULAR ADAPTADO"
gabarito_olimpiada = "Modelo de Gabarito: OLIMPIADA"
gabarito_olimpiada_adaptado = "Modelo de Gabarito: OLIMPIADA ADAPTADO"
gabarito_linguagens = "Modelo de Gabarito: LÍNGUA ESTRANGEIRA"

if (gab == 1):
    gabarito_regular

if(gab > 5):
   sys.exit("Programa encerrado por digitar um valor invalido!!")
else:
    caminho = input("Origem do arquivo: ")
    destino = input("Destino do arquivo ")

    while True:
        print("################################################")
        print(f'Editor de TXT de Gabaritos')
        print(f'  *** COLÉGIO MASTER ***')
        print(f'Origem: {caminho}')
        print(f'Destino: {destino}')

        if (gab == 1):
            print(gabarito_regular)
        elif (gab == 2):
            print(gabarito_regular_adaptado)
        elif (gab == 3):
            print(gabarito_olimpiada)
        elif (gab == 4):
            print(gabarito_olimpiada_adaptado)
        else:
            print(gabarito_linguagens)
        print("#################################################")

        doc = input("Nome do txt: ")
        arquivo = open(caminho + "\\" + doc + ".txt")
        leitura = arquivo.readlines()


        lista = []
        nlista = []
        nova = []
        proc = []

        for valor in leitura:
            lista.append(valor)

        #TODO: GABARITO REGULAR
        if (gab == 1):

            for item in lista:
                nova = item[0:19] + ";" + item[19:29] + ";A;" + item[29:]
                proc.append(nova)

            with open(destino + "\\" + doc + '.txt', 'w') as arquivo:
                for valor in proc:
                    arquivo.write(valor.strip() + '\n')
            os.system('cls')

        #TODO: GABARITO REGULAR ADAPTADO
        elif(gab == 2):

            for item in lista:
                nova = item[0:19] + "A;" + item[19:29] + ";A;" + item[29:]
                proc.append(nova)

            with open(destino + "\\" + doc + '.txt', 'w') as arquivo:
                 for valor in proc:
                    arquivo.write(valor.strip() + '\n')
            os.system('cls')

        #TODO: GABARITO DE OLIMPIADA
        elif (gab == 3):

            for item in lista:
                nova = item[0:20] + ";" + item[20:30] + ";A;" + item[30:]
                proc.append(nova)

            with open(destino + "\\" + doc + '.txt', 'w') as arquivo:
                for valor in proc:
                    arquivo.write(valor.strip() + '\n')
            os.system('cls')

        #TODO: GABARITO DE OLIMPIADA ADAPTADA
        elif (gab == 4):
           
            for item in lista:
                nova = item[0:20] + "A;" + item[20:30] + ";A;" + item[30:]
                proc.append(nova)

            with open(destino + "\\" + doc + '.txt', 'w') as arquivo:
                for valor in proc:
                    arquivo.write(valor.strip() + '\n')
            os.system('cls')

        #TODO: GABARITO DE LINGUAS ESTRANGEIRAS
        elif (gab == 5):
            for item in leitura:

                asterisco = item[0:30]

                if (asterisco[29] == "*"):
                    asterisco = asterisco.replace("*", ";")
                    asterisco = asterisco[0:19] + ";" + asterisco[19:29] + ";" + item[30:33] + ";" + "A;" + item[33:]
                    proc.append(asterisco)
                else:
                    asterisco = item[0:19] + ";" + item[19:29] + ";" + item[29:32] + ";" + "A;" + item[32:]
                    proc.append(asterisco)

                with open(destino + "\\" + doc + '.txt', 'w') as arquivo:
                    for valor in proc:
                        arquivo.write(valor.strip() + '\n')
                os.system('cls')


