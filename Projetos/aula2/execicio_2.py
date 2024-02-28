list = ['abacaxi', 'banana', 'maracuja', 'uva', 'melao']
fruta = input("Digite uma fruta: ")

for i in range(len(list)):
    if list[i] == fruta:
        print("Fruta está na lista. \n" , "\rIndice da fruta na lista:" , i)
