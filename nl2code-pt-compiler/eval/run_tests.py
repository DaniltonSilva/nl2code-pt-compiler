# run_tests.py
import pandas as pd
from src.interpreter.interpreter import interpret

def run_tests():
    df = pd.read_csv("data/prompts_pt.csv")
    results = []

    for index, row in df.iterrows():
        prompt = row["Prompt"]
        code = interpret(prompt)
        result = {
            "ID": row["ID"],
            "Prompt": prompt,
            "GeneratedCode": code.strip()
        }
        results.append(result)

    results_df = pd.DataFrame(results)
    results_df.to_csv("eval/results.csv", index=False)
    print("Testes concluídos. Resultados salvos em eval/results.csv")

if __name__ == "__main__":
    run_tests()
