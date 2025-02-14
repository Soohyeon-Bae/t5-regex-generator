import re
import pandas as pd

def process_text_and_save(input_file, output_txt, output_excel):
    with open(input_file, "r", encoding="utf-8") as f:
        text = f.read()

    # Normalize spaces to a single space
    text = re.sub(r"\s+", " ", text).strip()

    # Remove sheet headers (e.g., "--- SheetX ---" format)
    text = re.sub(r"--- Sheet\d+ ---", "", text).strip()

    # Automatically split text only if it starts with a number
    lines = re.split(r"(?=\b\d+\.\d+)", text)

    # Remove unnecessary empty strings
    lines = [line.strip() for line in lines if line.strip()]

    # Save the cleaned text
    with open(output_txt, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    # Process data for Excel storage (split based on "AA")
    data = []
    for line in lines:
        # If "AA" exists, separate class and regex
        match = re.search(r"\b(AA.*)", line)
        if match:
            class_part = line[:match.start()].strip()
            regex_part = match.group(1).strip()
        else:
            class_part = line.strip()
            regex_part = ""  # If "AA" is not found, leave regex empty

        data.append([class_part, regex_part])

    # Create DataFrame and save to Excel
    df = pd.DataFrame(data, columns=["class", "regex"])
    df.to_excel(output_excel, index=False)

    print(f"Cleaned text saved: {output_txt}")
    print(f"Excel file saved: {output_excel}")

# Example execution
process_text_and_save("input.txt", "output.txt", "output.xlsx")
