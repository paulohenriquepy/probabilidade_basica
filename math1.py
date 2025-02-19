# Tentando construir uma função para permutação


def permutar(numero):

    fatorial = []

    # Adiciona os números de 1 até numero na lista
    for elemento in range(1, numero + 1):
        fatorial.append(elemento)

    # Inicializa resultado antes do loop
    resultado = 1
    for valor in fatorial:
        resultado = resultado * valor

    total = []
    total.append(resultado)
    valor_final = total[-1]

    return valor_final


print(permutar(5))


