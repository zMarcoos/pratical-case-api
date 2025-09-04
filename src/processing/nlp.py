import re
from unidecode import unidecode

SIGNATURE_LINES = ("atenciosamente", "enviado do meu",
                   "confidencial", "att", "grato", "obrigado")


def preprocess(text: str = "") -> str:
    formatted_text = re.sub(r'\s+', ' ', text.strip())
    formatted_text_lower = formatted_text.lower()

    for signature in SIGNATURE_LINES:
        index = formatted_text_lower.rfind(signature)
        if index != -1:
            formatted_text = formatted_text[:index]
            break

    return unidecode(formatted_text)
