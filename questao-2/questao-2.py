# questao_2.py
def contar_letra_a(string):
    # Converte a string para minúsculas para facilitar a contagem
    string = string.lower()
    # Conta a ocorrência da letra 'a'
    contagem = string.count('a')
    # Verifica se a letra 'a' está presente
    if contagem > 0:
        print(f"A letra 'a' aparece {contagem} vezes na string.")
    else:
        print("A letra 'a' não está presente na string.")

# Exemplo de uso
string = input("Digite uma string: ")
contar_letra_a(string)
