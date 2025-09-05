import os
import re
import requests
from dotenv import load_dotenv
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

load_dotenv()

HF_API_TOKEN = os.getenv("HF_API_TOKEN")
HF_MODEL = os.getenv("HF_MODEL", "joeddav/xlm-roberta-large-xnli")
HF_URL = f"https://api-inference.huggingface.co/models/{HF_MODEL}"

IMPRODUCTIVE_KEYWORDS = [
    r"\bfeliz natal\b", r"\bfeliz ano novo\b", r"\bboas festas\b",
    r"\bobrigad[oa]\b", r"\bagradec", r"\bparab[eé]ns\b",
    r"\bestou de f[eé]rias\b", r"\bfora do escrit[oó]rio\b", r"\bout of office\b"
]
TIMEOUT = (5, 120)

session = requests.Session()
session.headers.update({"Authorization": f"Bearer {HF_API_TOKEN}"})

retry = Retry(
    total=3,
    backoff_factor=1.5,
    status_forcelist=(502, 503, 504),
    allowed_methods=("POST",),
    raise_on_status=False,
)
adapter = HTTPAdapter(max_retries=retry)
session.mount("https://", adapter)
session.mount("http://", adapter)


def rule_improductive(text: str) -> bool:
    text_lower = text.lower()
    return any(re.search(keyword, text_lower) for keyword in IMPRODUCTIVE_KEYWORDS)


def classify(text: str) -> tuple[str, float]:
    if rule_improductive(text):
        return "Improdutivo", 0.95

    payload = {
        "inputs": text,
        "parameters": {
            "candidate_labels": ["Produtivo", "Improdutivo"],
            "hypothesis_template": "Este email é {}."
        },
        "options": {
            "wait_for_model": True,
            "use_cache": True
        }
    }

    response = session.post(HF_URL, json=payload, timeout=TIMEOUT)
    if response.status_code == 401:
        raise RuntimeError(
            "Hugging Face 401: verifique HF_API_TOKEN/carregamento do .env.")

    response.raise_for_status()

    data = response.json()
    if isinstance(data, dict) and "error" in data:
        raise RuntimeError(f"Hugging Face erro: {data['error']}")

    label = data["labels"][0]
    score = float(data["scores"][0])
    
    return label, score
