# Tentando construir uma função para permutação


def permutar(numero):

    while numero != 1:

          valor = numero * (numero - 1)
          numero -= 1

          lista = []
          lista.append(valor)
          total = sum(lista)


          return total

print(permutar(5))
