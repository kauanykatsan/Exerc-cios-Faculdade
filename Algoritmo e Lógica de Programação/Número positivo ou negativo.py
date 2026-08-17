while True:
    try:
        numero = int(input("Digite um número: "))

        if numero >= 1:
            print("Positivo")
        else:
            print("Negativo")

    except ValueError:
        print("DIGITE APENAS NÚMEROS!")
