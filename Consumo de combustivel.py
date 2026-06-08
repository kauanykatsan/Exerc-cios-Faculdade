#Um carro percorreu uma distância e gastou certa quantidade de combustível
distancia= int(input("Qual foi a distância percorrida em km? "))
altura= int(input("Quantos litros de combustível foram gastos nesse trajeto? "))
#calculo: km/litros
resultado = distancia / altura
print(f"Litros gastos por km: {resultado}")