##################################################################
#  SENAC/RESILIA - Formação em Análise de Dados (FAD)            #
#  Projeto em Grupo - Módulo 2 -                                 #
#  !/usr/bin/env python3                                         #
# Criado por: Stephanie, Ana, Jorge, Lohan, Lenilson             #
#  Data de criação: 06/03/2023                                   #
#  versão = '3.11(64-bit)'                                       #
##################################################################
#

import csv
import datetime

class Entrevista:
    def __init__(self):
        self.data = []
        self.cabecalho = ["Idade", "Genero", "Voce esta empregado?", "Ha quanto tempo esta desempregado?", "Voce esta buscando recolocacao no mercado de trabalho?", "A vaga que voce procura possui experiencia?", "Data e Hora"]

    def dados(self):
        print("\n     Pesquisa sobre Desemprego   \n")
        while True:
            idade = input("Digite a idade: ")
            if idade == "00":
                break

            genero = input("Digite o gênero: ")
            pergunta1 = input("Você está empregado?  ")
            pergunta2 = input("Há quanto tempo está desempregado? ")
            pergunta3 = input("Você está buscando recolocação no mercado de trabalho? ")
            pergunta4 = input("A vaga que você procura possui experiência? ")

            now = datetime.datetime.now()
            data_hora = now.strftime("%d/%m/%Y %H:%M:%S")

            lista = [idade, genero, pergunta1, pergunta2, pergunta3, pergunta4, data_hora]
            self.data.append(lista)

        print(f"\n{len(self.data)} dados coletados para pesquisa.")

    def salvar_arquivo_csv(self, nome):
        with open(nome, "w", newline="") as arquivo:
            writer = csv.writer(arquivo)
            writer.writerow(self.cabecalho)
            writer.writerows(self.data)
        print(f"O arquivo {nome} foi salvo com sucesso.")

