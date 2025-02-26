import torch
from transformers import T5Tokenizer, T5ForConditionalGeneration, AdamW
from torch.utils.data import DataLoader
from dataset import RegexDataset

# Load model and tokenizer
model_name = "t5-small"
tokenizer = T5Tokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)

# 2Load dataset
dataset = RegexDataset("../data/regex_data.csv", tokenizer)
dataloader = DataLoader(dataset, batch_size=4, shuffle=True)

# Set training configurations
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)
model.train()
optimizer = AdamW(model.parameters(), lr=5e-5)

# Training loop
epochs = 3
for epoch in range(epochs):
    total_loss = 0
    for batch in dataloader:
        optimizer.zero_grad()
        input_ids, attention_mask, labels = batch["input_ids"].to(device), batch["attention_mask"].to(device), batch[
            "labels"].to(device)

        outputs = model(input_ids=input_ids, attention_mask=attention_mask, labels=labels)
        loss = outputs.loss
        loss.backward()
        optimizer.step()

        total_loss += loss.item()

    print(f"Epoch {epoch + 1}, Loss: {total_loss / len(dataloader)}")

# 5️⃣ Save trained model
model.save_pretrained("../models/t5_regex_model")
tokenizer.save_pretrained("../models/t5_regex_model")

