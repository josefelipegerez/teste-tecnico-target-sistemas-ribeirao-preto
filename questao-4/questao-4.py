# questao_4.py

'''
a) 1, 3, 5, 7, 9
Lógica: adiciona 2.

b) 2, 4, 8, 16, 32, 64, 128
Lógica: Multiplicação por 2.

c) 0, 1, 4, 9, 16, 25, 36, 49
Lógica: Quadrados perfeitos (n²).

d) 4, 16, 36, 64, 100
Lógica: Quadrados perfeitos, múltiplos de 4 (2², 4², 6², 8², 10²).

e) 1, 1, 2, 3, 5, 8, 13
Lógica: Sequência de Fibonacci.

f) 2, 10, 12, 16, 17, 18, 19, 20
Lógica: Sequência numérica sem múltiplos de 3 após 10.
'''

# código de exemplo

def completar_sequencias():
    # Parte (a)
    seq_a = [1, 3, 5, 7]
    seq_a.append(seq_a[-1] + 2)
    print(f"Próximo número da sequência (a): {seq_a[-1]}")

    # Parte (b)
    seq_b = [2, 4, 8, 16, 32, 64]
    seq_b.append(seq_b[-1] * 2)
    print(f"Próximo número da sequência (b): {seq_b[-1]}")

    # Parte (c)
    seq_c = [0, 1, 4, 9, 16, 25, 36]
    seq_c.append((len(seq_c))**2)
    print(f"Próximo número da sequência (c): {seq_c[-1]}")

    # Parte (d)
    seq_d = [4, 16, 36, 64]
    seq_d.append(100)  # Próximo número é 100
    print(f"Próximo número da sequência (d): {seq_d[-1]}")

    # Parte (e)
    seq_e = [1, 1, 2, 3, 5, 8]
    seq_e.append(seq_e[-1] + seq_e[-2])
    print(f"Próximo número da sequência (e): {seq_e[-1]}")

    # Parte (f)
    seq_f = [2, 10, 12, 16, 17, 18, 19]
    seq_f.append(20)
    print(f"Próximo número da sequência (f): {seq_f[-1]}")

completar_sequencias()
