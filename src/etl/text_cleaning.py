import re

def clean_text(text):
    text = str(text).lower().strip()
    text = re.sub(r"[^a-z0-9áéíóúãõâêôç\s]", " ", text)
    return re.sub(r"\s+", " ", text)
