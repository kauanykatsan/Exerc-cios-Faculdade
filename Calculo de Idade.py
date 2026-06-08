#Leia o ano de nascimento e calcule a idade aproximada considerando o ano atual.
import datetime
ano_atual = datetime.date.today().year
idade= int(input("Qual seu ano de nascimento? "))
#calculo
calculo= ano_atual-idade
print(f"Sua idade = {calculo}")
