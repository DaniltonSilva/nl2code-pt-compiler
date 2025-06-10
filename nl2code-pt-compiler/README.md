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

1. Instale os pacotes necessários:

```bash
pip install -r requirements.txt
```

2. Execute os testes:

```bash
python eval/run_tests.py
```

3. Valide os códigos manualmente com:

```bash
python src/validator/validator.py
```

4. Analise os resultados no notebook:

Abra `notebooks/rsl_analysis.ipynb` com Jupyter.

## Licença

MIT
