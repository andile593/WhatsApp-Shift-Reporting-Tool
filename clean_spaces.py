input_path = "whatsapp_shift_report.py"
output_path = "whatsapp_shift_report_clean.py"

with open(input_path, "r", encoding="utf-8") as file:
    content = file.read()

# Replace non-breaking space with normal space
content = content.replace('\u00A0', ' ')

with open(output_path, "w", encoding="utf-8") as file:
    file.write(content)

print(f"Cleaned file saved to {output_path}")