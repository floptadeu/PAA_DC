import random
import time
import matplotlib.pyplot as plt

def max_increasing_subsequence(arr, low, high):
    if low == high:
        return [arr[low]]

    mid = (low + high) // 2

    left_subseq = max_increasing_subsequence(arr, low, mid)
    right_subseq = max_increasing_subsequence(arr, mid + 1, high)

    return max(max_left_right_subsequence(arr, mid), left_subseq, right_subseq, key=len)

def max_left_right_subsequence(arr, mid):
    left_seq = []
    right_seq = []

    # Subsequência crescente à esquerda do meio
    last = float('-inf')
    for i in range(mid, -1, -1):
        if arr[i] > last:
            left_seq.append(arr[i])
            last = arr[i]
        else:
            break
    left_seq.reverse()

    # Subsequência crescente à direita do meio
    last = float('inf')
    for i in range(mid + 1, len(arr)):
        if arr[i] > last:
            right_seq.append(arr[i])
            last = arr[i]
        else:
            break

    return left_seq + right_seq

# Exemplo de uso
#arr = [5, 2, 8, 6, 3, 6, 9, 7]
#print("Maior subsequência crescente contígua:", max_increasing_subsequence(arr, 0, len(arr) - 1))



def generate_random_sequence(length, min_value, max_value):
    """ Gera uma sequência aleatória de números dentro de um intervalo. """
    return [random.randint(min_value, max_value) for _ in range(length)]

def generate_increasing_sequence(length):
    """ Gera uma sequência estritamente crescente. """
    return [i for i in range(length)]

def generate_decreasing_sequence(length):
    """ Gera uma sequência estritamente decrescente. """
    return [i for i in range(length, 0, -1)]

def generate_alternating_sequence(length):
    """ Gera uma sequência alternando entre números baixos e altos. """
    return [random.randint(-100, 100) if i % 2 == 0 else random.randint(-10, 10) for i in range(length)]

def generate_test_cases():
    test_cases = {
        "Random Small": generate_random_sequence(100, -100, 100),
        "Random Medium": generate_random_sequence(1000, -1000, 1000),
        "Random Large": generate_random_sequence(5000, -5000, 5000),
        "Increasing": generate_increasing_sequence(1000),
        "Decreasing": generate_decreasing_sequence(1000),
        "Alternating": generate_alternating_sequence(1000)
    }
    return test_cases

# Gerar e imprimir test cases
test_cases = generate_test_cases()
#for name, case in test_cases.items():
#    print(f"{name} (Length {len(case)}): {case[:20]}...")  # Imprime os primeiros 20 números para visualização

'''

Random Small, Medium, Large: Sequências aleatórias de diferentes tamanhos. Isso testa como o algoritmo lida com entradas comuns de diferentes escalas.

Increasing: Uma sequência estritamente crescente. Este é um caso de teste interessante porque a resposta é a sequência inteira, o que pode ser desafiador para o algoritmo.

Decreasing: Uma sequência estritamente decrescente. Este é um caso extremo onde não existem subsequências crescentes além dos elementos individuais.

Alternating: Uma sequência que alterna entre valores baixos e altos. Este caso é projetado para desafiar o algoritmo a identificar corretamente pequenas subsequências crescentes em um contexto de variação alta.


'''

def is_increasing(subseq):
    """ Verifica se a subsequência é estritamente crescente. """
    for i in range(1, len(subseq)):
        if subseq[i] <= subseq[i - 1]:
            return False
    return True

def max_increasing_subsequence_brute_force(arr):
    n = len(arr)
    max_length = 0
    max_subseq = []

    # Percorre todas as subsequências possíveis
    for i in range(n):
        for j in range(i, n):
            subseq = arr[i:j + 1]
            if is_increasing(subseq) and len(subseq) > max_length:
                max_length = len(subseq)
                max_subseq = subseq

    return max_subseq

# Exemplo de uso
#arr = [5, 2, 8, 6, 3, 6, 9, 7]
#print("Maior subsequência crescente contígua:", max_increasing_subsequence_brute_force(arr))


#for name, case in test_cases.items():
#    start_time = time.time()
#    max_subseq = max_increasing_subsequence_brute_force(case)
#    end_time = time.time()
#    time_taken = end_time - start_time
#    print(f"{name} (Length {len(case)}): Executado em {time_taken:.4f} segundos")

#for name, case in test_cases.items():
#    start_time = time.time()
#    max_subseq = max_increasing_subsequence(case, 0, len(case) - 1)
#    end_time = time.time()
#    time_taken = end_time - start_time
#    print(f"{name} (Length {len(case)}): Executado em {time_taken:.4f} segundos. Subsequência: {max_subseq}")


def measure_execution_time(func, *args):
    start_time = time.time()
    func(*args)
    end_time = time.time()
    return end_time - start_time

# Supondo que `generate_test_cases` é a sua função que gera os casos de teste
test_cases = generate_test_cases()

# Dicionários para armazenar os tempos de execução
times_brute_force = {}
times_divide_conquer = {}

for name, case in test_cases.items():
    times_brute_force[name] = measure_execution_time(max_increasing_subsequence_brute_force, case)
    times_divide_conquer[name] = measure_execution_time(max_increasing_subsequence, case, 0, len(case) - 1)
    print(times_divide_conquer[name])



# Nomes dos testes
test_names = list(test_cases.keys())

# Tempos de execução para cada algoritmo
brute_force_times = [times_brute_force[name] for name in test_names]
divide_conquer_times = [times_divide_conquer[name] for name in test_names]


# Configuração da figura e dos subplots
plt.figure(figsize=(12, 10))

# Gráfico para o algoritmo de Força Bruta
plt.subplot(2, 1, 1)  # 2 linhas, 1 coluna, posição 1
plt.bar(test_names, brute_force_times, color='blue')
plt.xlabel('Casos de Teste')
plt.ylabel('Tempo de Execução (s)')
plt.title('Tempos de Execução do Algoritmo de Força Bruta')
plt.xticks(rotation=45)

# Gráfico para o algoritmo de Divisão e Conquista
plt.subplot(2, 1, 2)  # 2 linhas, 1 coluna, posição 2
plt.bar(test_names, divide_conquer_times, color='green')
plt.xlabel('Casos de Teste')
plt.ylabel('Tempo de Execução (s)')
plt.title('Tempos de Execução do Algoritmo de Divisão e Conquista')
plt.xticks(rotation=45)

# Ajustar layout e exibir os gráficos
plt.tight_layout()
plt.show()
