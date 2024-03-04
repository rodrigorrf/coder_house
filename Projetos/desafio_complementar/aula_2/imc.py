peso = float(input("Digite seu peso: "))
altura = float(input("""\nDigite sua altura, usando ".", 
                     \rExemplo: 1.70
                     \rAltura: """))

imc = peso / (altura ** 2)
print(f"\nSeu imc é: {imc:,.2f}")

if imc < 18.5:
    print("Abaixo do peso")
elif imc >= 18.5 and imc <= 24.9:
    print("Peso normal")
elif imc >= 25.0 and imc <= 29.9:
    print("Sobrepeso")
elif imc >= 30.0 and imc <= 39.9:
    print("Obesidade")
else:
    print("Obesidade grave")