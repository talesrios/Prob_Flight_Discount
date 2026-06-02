# T2 — Flight Discount (CSES 1195)

**Disciplina:** Algoritmos e Estrutura de Dados  
**Grupo:** G  
**Problema:** [CSES 1195 — Flight Discount](https://cses.fi/problemset/task/1195)  
**Referência:** [T2.md — Repositório Carubbi/T290](https://github.com/carubbi/T290/blob/main/trabalhos/und3/T2/T2.md)

---

## Descrição do Problema

Dado um grafo dirigido com **N** cidades e **M** voos, encontrar o menor custo de viagem da cidade **1** até a cidade **N**, sendo obrigatório usar exatamente **um cupom de desconto de 50%** em um dos voos do caminho.

---

## Estratégia de Solução

O problema é modelado como um **grafo dirigido ponderado** com **dois estados** por vértice:

- **Estado 0:** chegou ao vértice sem ter usado o cupom ainda  
- **Estado 1:** chegou ao vértice com o cupom já utilizado

Isso transforma o problema em encontrar o caminho mínimo em um **grafo de estados expandido** com `2 × N` nós, resolvido com o **Algoritmo de Dijkstra modificado**.

---

## Complexidade

| Componente | Complexidade |
|---|---|
| Tempo | O((N + M) log N) |
| Espaço | O(N + M) |

---

## Como Executar

```bash
# Compilar/executar com entrada padrão
python3 src/main.py < dados/entradas_do_problema.txt
```

---

## Estrutura do Repositório

```
T2/
├── README.md
├── src/
│   └── main.py
├── evidencias/
│   └── accepted.png
├── apresentacao/
│   └── apresentacao.pdf
└── dados/
    └── entradas_do_problema.txt
```
