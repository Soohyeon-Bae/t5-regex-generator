import torch
from transformers import T5Tokenizer, T5ForConditionalGeneration

# Load trained model and tokenizer
model_path = "../models/t5_regex_model"
tokenizer = T5Tokenizer.from_pretrained(model_path)
model = T5ForConditionalGeneration.from_pretrained(model_path)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)
model.eval()

def generate_regex(input_text):
    """Generates a regular expression from a given input string."""
    input_ids = tokenizer(input_text, return_tensors="pt").input_ids.to(device)
    output_ids = model.generate(input_ids, max_length=50)
    return tokenizer.decode(output_ids[0], skip_special_tokens=True)

# Run a test example
test_input = "EMAIL: user@example.com"
print(f"Input: {test_input}")
print(f"Generated Regex: {generate_regex(test_input)}")

