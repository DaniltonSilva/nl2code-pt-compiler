# validator.py
# Validação sintática e semântica simulada do código gerado

def validate(code):
    if "def " in code and "(" in code and ")" in code and ":" in code:
        return True, "Código validado com sucesso."
    else:
        return False, "Erro de sintaxe detectado."

if __name__ == "__main__":
    exemplo = """def exemplo(x):\n    return x"""
    valido, mensagem = validate(exemplo)
    print(mensagem)
