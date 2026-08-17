#Leia a velocidade de um carro
while True:
  try:
     velocidade= int(input("Qual a velocidade do carro?"))
  except ValueError:
    print("Digite apenas números inteiros!")
  

  
  if velocidade > 80:
    print("Multado")
  else:
    print("Dentro do limite de velocidade permitido")
            
