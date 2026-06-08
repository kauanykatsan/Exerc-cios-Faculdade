#Maior entre Dois Números 

while True:
    try: 
     numero1=int(input("Digite o primeiro número:"))
     numero2=int(input("Digite o segundo número:"))
    except ValueError:
      print("DIgite apennas números inteiros")
      continue 
    if numero1>numero2:
      print("O maior número é:", numero1)
    elif numero2>numero1:
      print("O maior número é:", numero2)
    else:
      print("Os números são iguais")
         