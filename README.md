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

* **Estado 0:** chegou ao vértice sem ter usado o cupom ainda  
* **Estado 1:** chegou ao vértice com o cupom já utilizado

Isso transforma o problema em encontrar o caminho mínimo em um **grafo de estados expandido** com `2 × N` nós, resolvido com o **Algoritmo de Dijkstra modificado**.

---

## Complexidade

| Componente | Complexidade |
| :--- | :--- |
| **Tempo** | O((N + M) log N) |
| **Espaço** | O(N + M) |

---

## Como Executar Localmente (VS Code)

O código foi projetado para facilitar testes locais sem a necessidade de digitar entradas manualmente no terminal ou colar os dados a cada teste.

1. Certifique-se de que sua entrada de teste está salva no arquivo `dados/entradas_do_problema.txt`.
2. Estando na pasta raiz do projeto, execute o código com o Python:

```bash
python main.py
```

O programa exibirá a saída correspondente diretamente no terminal.

---

## Diferença entre Execução Local (VS Code) e Submissão no CSES

Para evitar o trabalho de ter que alterar o código toda vez que for testá-lo ou submetê-lo, foi implementado um "truque" nas últimas linhas do arquivo `main.py`:

```python
if os.path.exists('dados/entradas_do_problema.txt'):
    sys.stdin = open('dados/entradas_do_problema.txt', 'r')
```

### 💻 No VS Code (Local)

Quando você clica em "Run" na sua máquina, o Python verifica se a pasta `dados` e o arquivo de texto existem. Como eles existem no seu projeto, o programa muda a "chave" de leitura e começa a puxar os dados diretamente do arquivo de texto. Isso automatiza os seus testes.

### 🌐 No Site CSES (Juiz Online)

Quando você copia o código e submete no site, ele roda dentro do servidor do CSES (em um ambiente limpo). Lá, a sua pasta `dados` não existe. Sendo assim, o comando `os.path.exists` retorna falso e o Python ignora o bloco de código acima. O código então faz a leitura normal da entrada padrão (`sys.stdin`), que é exatamente o que o CSES espera para injetar os casos de teste escondidos deles.

> **Resumo:** Você pode testar confortavelmente no VS Code lendo de arquivos e, quando terminar, basta copiar e colar o arquivo inteiro no CSES que ele passará direto!

---

## Estrutura do Repositório

```
T2/
├── README.md
├── main.py
├── evidencias/
│   └── accepted.png
├── apresentacao/
│   └── apresentacao.pdf
└── dados/
    └── entradas_do_problema.txt
```
