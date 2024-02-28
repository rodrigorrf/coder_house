list_frase = [input("Digite uma frase \n")]
list = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

print("Tamanho da frase digitada: ", len(list_frase))
print("Tamanho da lista de vogais: ", len(list))

for i in range(len(list_frase)):
    for j in range(len(list)):
        list_frase[i] = list_frase[i].replace(list[j], "*")

print(list_frase)