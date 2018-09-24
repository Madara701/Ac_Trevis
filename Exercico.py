'''def Div():
    a = input("Primeiro numero: ")
    b = input("Segundo numero: ")
    try:
        a = int(a)
        b = int(b)
        print(a/b)
    except ValueError:
            print("Vc não digitou um numero!")
    except ZeroDivisionError:
            print("vc digitou zero!")
    finally:
            print("Muito Obrigado!")

        

Div()'''
lista = ["a","b","c","d","e","f","g","h"]
lista2 = []
for x in range(0,len(lista),2):
    lista2.append(lista[x])
    print(x)
print(lista2)


