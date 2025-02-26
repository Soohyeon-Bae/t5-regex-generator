import pandas as pd
from torch.utils.data import Dataset

class RegexDataset(Dataset):
    def __init__(self, file_path, tokenizer, max_len=128):
        self.data = pd.read_csv(file_path)
        self.tokenizer = tokenizer
        self.max_len = max_len

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        input_text = self.data.iloc[index]["input"]
        target_text = self.data.iloc[index]["output"]

        # Tokenize input and target texts
        input_enc = self.tokenizer(input_text, max_length=self.max_len, padding="max_length", truncation=True, return_tensors="pt")
        target_enc = self.tokenizer(target_text, max_length=self.max_len, padding="max_length", truncation=True, return_tensors="pt")

        return {
            "input_ids": input_enc["input_ids"].squeeze(),
            "attention_mask": input_enc["attention_mask"].squeeze(),
            "labels": target_enc["input_ids"].squeeze()
        }

