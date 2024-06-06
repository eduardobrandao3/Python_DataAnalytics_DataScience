"""Faça um programa que receba o nome e a temperatura máxima de várias cidades e ao longo de uma semana e armazene essas informações em 
um dicionário, onde a chave é o nome da cidade e o valor é a temperatura máxima (pare de receber informações quando o usuário digitar 
"goiabada" no nome da cidade). O programa deve retornar em quantos graus a maior temperatura supera a média das temperaturas."""

def media(dic):
    return sum(dicionario.values())/len(dic)

def maior (dic):
    return sorted(list(dic.values()), reverse=True)[0]

print("Digite goiabada para parar")
cidade = input("Digite o nome da cidade: ").strip()
temp = float(input("Digite a temperatura: "))

dicionario = dict()

while cidade != 'goiabada':
    dicionario[cidade] = temp
    cidade = input("Digite o nome da cidade: ").strip()
    if(cidade == 'goiabada'):
        break
    temp = float(input("Digite a temperatura máxima: "))

print(f"A maior temperatura ({maior(dicionario)}) supera a media das temperaturas em {maior(dicionario) - media(dicionario)}")