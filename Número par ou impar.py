while True:
    try:
        numero = int(input("Digite um número: "))

        if numero % 2==0 :
            print("Par")
        else:
            print("Impar")

    except ValueError:
        print("DIGITE APENAS NÚMEROS!")