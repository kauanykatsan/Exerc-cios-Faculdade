#Cálculo de IMC
peso=float(input("Informe seu peso:"))
altura=float(input("Informe sua altura:"))
imc = peso/(altura*altura)
print(f"Seu IMC é: {imc}")
if imc<18.5:
  print("Abaixo do peso")
elif 18.5 <= imc < 24.9:
  print("Peso normal")
elif 25 <= imc < 29.9:
  print("Sobrepeso")
elif 30<= imc < 39.9:
  print("Obesidade Grau 1")
elif imc > 40:
  print("Obesidade Grau 2")
else:
  print("Obesidade Grau 3")