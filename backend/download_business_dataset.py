#download_business_dataset.py
from datasets import load_dataset
import os

print("Downloading business dataset...")

dataset = load_dataset("yahma/alpaca-cleaned")

os.makedirs("data/business_docs", exist_ok=True)

count = 0

for item in dataset["train"]:

    instruction = item["instruction"]
    output = item["output"]

    text = instruction + "\n" + output

    # save only business-related data
    keywords = ["business","startup","company","market","finance","management"]

    if any(k in text.lower() for k in keywords):

        with open(f"data/business_docs/business_{count}.txt", "w", encoding="utf-8") as f:
            f.write(text)

        count += 1

    if count == 3000:
        break

print("Business dataset ready:", count, "documents")
