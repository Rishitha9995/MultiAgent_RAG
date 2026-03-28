#download_legal_dataset.py
from datasets import load_dataset
import os

print("Downloading better legal dataset...")

dataset = load_dataset("lex_glue", "ledgar")

os.makedirs("data/legal_cases", exist_ok=True)

count = 0

for item in dataset["train"]:

    text = item["text"]

    with open(f"data/legal_cases/legal_{count}.txt", "w", encoding="utf-8") as f:
        f.write(text)

    count += 1

    if count == 2000:   # limit size so VS Code does not freeze
        break

print("Legal dataset ready:", count, "documents")
