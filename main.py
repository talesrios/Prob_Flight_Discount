# import sys
# import heapq

# def resolver_flight_discount():
#     # Leitura otimizada de todas as entradas do terminal
#     input_data = sys.stdin.read().split()
#     if not input_data:
#         return
    
#     # N: número de cidades (vértices), M: número de voos (arestas)
#     n = int(input_data[0])
#     m = int(input_data[1])
    
#     # Construção do Grafo usando Lista de Adjacência
#     # Cada posição armazena uma lista de tuplas: (vizinho, preço_do_voo)
#     grafo = [[] for _ in range(n + 1)]
    
#     idx = 2
#     for _ in range(m):
#         u = int(input_data[idx])
#         v = int(input_data[idx+1])
#         w = int(input_data[idx+2])
#         grafo[u].append((v, w))
#         idx += 3
        
#     # Representação de Infinito para inicialização das distâncias
#     INF = float('inf')
    
#     # Tabelas de distâncias para os dois estados do algoritmo:
#     # dist_sem_desconto[i] -> menor custo para chegar à cidade 'i' SEM usar nenhum cupom.
#     # dist_com_desconto[i] -> menor custo para chegar à cidade 'i' tendo usado o cupom em ALGUM voo anterior.
#     dist_sem_desconto = [INF] * (n + 1)
#     dist_com_desconto = [INF] * (n + 1)
    
#     # A cidade de partida (1) começa com custo zero no estado "sem desconto"
#     dist_sem_desconto[1] = 0
    
#     # Fila de Prioridade (Min-Heap) para gerenciar o processo do Dijkstra
#     # Elemento da fila: (custo_atual, cidade_atual, flag_cupom_usado)
#     # flag_cupom_usado: 0 significa "não usou", 1 significa "já usou"
#     fila_prioridade = [(0, 1, 0)]
    
#     while fila_prioridade:
#         custo_atual, u, cupom_usado = heapq.heappop(fila_prioridade)
        
#         # Poda: se o custo atual já é maior que o registrado, ignorar
#         if cupom_usado == 0 and custo_atual > dist_sem_desconto[u]:
#             continue
#         if cupom_usado == 1 and custo_atual > dist_com_desconto[u]:
#             continue
            
#         # Otimização: chegou ao destino com cupom já utilizado
#         if u == n and cupom_usado == 1:
#             break
            
#         # Explorar vizinhos (relaxamento de arestas)
#         for v, peso in grafo[u]:
#             if cupom_usado == 0:
#                 # Opção A: Avançar sem gastar o cupom neste voo atual
#                 if dist_sem_desconto[u] + peso < dist_sem_desconto[v]:
#                     dist_sem_desconto[v] = dist_sem_desconto[u] + peso
#                     heapq.heappush(fila_prioridade, (dist_sem_desconto[v], v, 0))
                    
#                 # Opção B: Gastar o cupom especificamente neste voo atual (peso // 2)
#                 if dist_sem_desconto[u] + (peso // 2) < dist_com_desconto[v]:
#                     dist_com_desconto[v] = dist_sem_desconto[u] + (peso // 2)
#                     heapq.heappush(fila_prioridade, (dist_com_desconto[v], v, 1))
                    
#             else:
#                 # Cupom já foi usado: apenas pagar preço integral
#                 if dist_com_desconto[u] + peso < dist_com_desconto[v]:
#                     dist_com_desconto[v] = dist_com_desconto[u] + peso
#                     heapq.heappush(fila_prioridade, (dist_com_desconto[v], v, 1))
                    
#     # Resposta: menor custo para chegar à cidade N com cupom obrigatoriamente utilizado
#     print(dist_com_desconto[n])

# if __name__ == '__main__':
#     resolver_flight_discount()



import sys
import heapq
import os

def resolver_flight_discount():
    # Leitura otimizada de todas as entradas do terminal ou do arquivo
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    # N: número de cidades (vértices), M: número de voos (arestas)
    n = int(input_data[0])
    m = int(input_data[1])
    
    # Construção do Grafo usando Lista de Adjacência
    # Cada posição armazena uma lista de tuplas: (vizinho, preço_do_voo)
    grafo = [[] for _ in range(n + 1)]
    
    idx = 2
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        w = int(input_data[idx+2])
        grafo[u].append((v, w))
        idx += 3
        
    # Representação de Infinito para inicialização das distâncias
    INF = float('inf')
    
    # Tabelas de distâncias para os dois estados do algoritmo:
    # dist_sem_desconto[i] -> menor custo para chegar à cidade 'i' SEM usar nenhum cupom.
    # dist_com_desconto[i] -> menor custo para chegar à cidade 'i' tendo usado o cupom em ALGUM voo anterior.
    dist_sem_desconto = [INF] * (n + 1)
    dist_com_desconto = [INF] * (n + 1)
    
    # A cidade de partida (1) começa com custo zero no estado "sem desconto"
    dist_sem_desconto[1] = 0
    
    # Fila de Prioridade (Min-Heap) para gerenciar o processo do Dijkstra
    # Elemento da fila: (custo_atual, cidade_atual, flag_cupom_usado)
    # flag_cupom_usado: 0 significa "não usou", 1 significa "já usou"
    fila_prioridade = [(0, 1, 0)]
    
    while fila_prioridade:
        custo_atual, u, cupom_usado = heapq.heappop(fila_prioridade)
        
        # Poda: se o custo atual já é maior que o registrado, ignorar
        if cupom_usado == 0 and custo_atual > dist_sem_desconto[u]:
            continue
        if cupom_usado == 1 and custo_atual > dist_com_desconto[u]:
            continue
            
        # Otimização: chegou ao destino com cupom já utilizado
        if u == n and cupom_usado == 1:
            break
            
        # Explorar vizinhos (relaxamento de arestas)
        for v, peso in grafo[u]:
            if cupom_usado == 0:
                # Opção A: Avançar sem gastar o cupom neste voo atual
                if dist_sem_desconto[u] + peso < dist_sem_desconto[v]:
                    dist_sem_desconto[v] = dist_sem_desconto[u] + peso
                    heapq.heappush(fila_prioridade, (dist_sem_desconto[v], v, 0))
                    
                # Opção B: Gastar o cupom especificamente neste voo atual (peso // 2)
                if dist_sem_desconto[u] + (peso // 2) < dist_com_desconto[v]:
                    dist_com_desconto[v] = dist_sem_desconto[u] + (peso // 2)
                    heapq.heappush(fila_prioridade, (dist_com_desconto[v], v, 1))
                    
            else:
                # Cupom já foi usado: apenas pagar preço integral
                if dist_com_desconto[u] + peso < dist_com_desconto[v]:
                    dist_com_desconto[v] = dist_com_desconto[u] + peso
                    heapq.heappush(fila_prioridade, (dist_com_desconto[v], v, 1))
                    
    # Resposta: menor custo para chegar à cidade N com cupom obrigatoriamente utilizado
    print(dist_com_desconto[n])

if __name__ == '__main__':
    # Caminho exato para o seu arquivo local
    caminho_arquivo = 'Dados/entradas_do_problema.txt'
    
    # Se o arquivo existir localmente, o Python redireciona a entrada para ler dele.
    # No site de submissão, essa pasta não existe, então ele usa a entrada padrão do juiz online.
    if os.path.exists(caminho_arquivo):
        sys.stdin = open(caminho_arquivo, 'r')
        
    resolver_flight_discount()