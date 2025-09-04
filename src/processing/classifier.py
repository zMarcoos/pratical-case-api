from transformers import pipeline
import re

zero_shot_classifier = None


def load_model():
    global zero_shot_classifier
    zero_shot_classifier = pipeline(
        "zero-shot-classification",
        model="joeddav/xlm-roberta-large-xnli",
        device=-1
    )


IMPRODUCTIVE_KEYWORDS = [
    r"\bfeliz natal\b", r"\bfeliz ano novo\b", r"\bboas festas\b",
    r"\bobrigad[oa]\b", r"\bagradec", r"\bparab[eé]ns\b",
    r"\bestou de f[eé]rias\b", r"\bfora do escrit[oó]rio\b", r"\bout of office\b"
]


def rule_improductive(text: str) -> bool:
    text_lower = text.lower()
    return any(re.search(keyword, text_lower) for keyword in IMPRODUCTIVE_KEYWORDS)


def classify(text: str) -> tuple[str, float]:
    if rule_improductive(text):
        return "Improdutivo", 0.95

    labels = ["Produtivo", "Improdutivo"]
    result = zero_shot_classifier(
        text,
        candidate_labels=labels,
        hypothesis_template="Este email é {}."
    )
    return result["labels"][0], float(result["scores"][0])
