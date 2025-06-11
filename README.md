[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.15636383.svg)](https://doi.org/10.5281/zenodo.15636383)
# NL2Code-PT Compiler

Este repositório contém o protótipo de um compilador híbrido que traduz linguagem natural em português para código, com validação semântica baseada em gramáticas de atributos e modelos de linguagem (LLMs).

## Estrutura do Projeto

- `src/interpreter/` - Módulo de interpretação baseado em LLMs (Python).
- `src/validator/` - Módulo de validação semântica (simulação).
- `src/generator/` - Módulo de geração e otimização de código.
- `data/` - Conjunto de prompts de entrada e exemplos.
- `eval/` - Scripts para avaliação do desempenho.
- `notebooks/` - Análises experimentais e bibliométricas.

## Como Executar

### 1. Instale as dependências

```bash
pip install -r requirements.txt
```

### 2. Execute os testes com prompts

```bash
python eval/run_tests.py
```

Gera um arquivo `eval/results.csv` com os códigos produzidos.

### 3. Valide um código manualmente

```bash
python src/validator/validator.py
```

### 4. Use o interpretador interativo

```bash
python src/interpreter/interpreter.py
```

Exemplo de entrada:
```
Crie uma função que calcule a média de uma lista de números
```

Saída esperada:
```python
def calcular_media(lista):
    return sum(lista) / len(lista)
```

### 5. Análise dos resultados com Jupyter

Abra o notebook:

```bash
jupyter notebook notebooks/rsl_analysis.ipynb
```

## Licença

MIT
