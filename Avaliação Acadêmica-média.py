nota1= float(input("Nota1:"))
nota2= float(input("Nota2:"))
nota3= float(input("Nota3:"))
media = (nota1 + nota2 + nota3)/3
if media >=6:
  print(f"Média: {media:.2f}""- APROVADO")
else:
   print(f"Média: {media:.2f}"" REPROVADO")