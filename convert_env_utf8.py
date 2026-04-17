from pathlib import Path

p = Path(r"C:/Users/user/.env")
text = p.read_text(encoding="utf-16")
p.write_text(text, encoding="utf-8")
print("Converted .env to utf-8")
