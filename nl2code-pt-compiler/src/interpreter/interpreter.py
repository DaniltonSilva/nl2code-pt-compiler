# interpreter.py
# Interpreta instruções em linguagem natural para uma estrutura de código inicial

def interpret(prompt):
    # Mapeamento simples para fins de exemplo (simulação de LLM)
    if "média" in prompt:
        return """
def calcular_media(lista):
    return sum(lista) / len(lista)
"""
    elif "fatorial" in prompt:
        return """
def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n-1)
"""
    else:
        return "# Código não reconhecido pelo interpretador simplificado"

if __name__ == "__main__":
    prompt = input("Digite uma instrução em linguagem natural: ")
    codigo = interpret(prompt)
    print("\nCódigo gerado:\n")
    print(codigo)
