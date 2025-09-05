# 📧 PraticalCaseAPI

API desenvolvida em **FastAPI** para classificação automática de e-mails, com suporte a NLP, rotas REST e documentação automática.

---

## ✨ Funcionalidades

* 🔍 **Classificação de e-mails** via NLP
* ⚡ **FastAPI**: framework moderno, rápido e tipado
* 🌍 **CORS liberado** para integração com qualquer frontend
* 📑 **Rotas REST** bem organizadas
* 🛡️ **Tratamento de erros** centralizado

---

## ⚙️ Como Rodar Localmente

### 1. Clonar o projeto

```bash
git clone https://github.com/seu-usuario/pratical-case-api.git
cd pratical-case-api
```

### 2. Instalar o Poetry

Para instalar o [Poetry](https://python-poetry.org/):

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

Adicione ao seu `~/.bashrc` ou `~/.zshrc`:

```bash
export PATH="$HOME/.local/bin:$PATH"
```

Depois recarregue o shell:

```bash
source ~/.bashrc
```

Verifique se está instalado:

```bash
poetry --version
```

### 3. Criar ambiente com Poetry (Python 3.13)

```bash
poetry env use python3.13
poetry install
```

### 4. Rodar servidor local

```bash
poetry run python -m uvicorn src.application:application --host 0.0.0.0 --port 8000
```

Acesse em: [http://localhost:8000](http://localhost:8000)
Documentação automática: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🎥 Vídeo Explicativo

👉 \[Adicione aqui o link para o vídeo demonstrativo no YouTube/Vimeo/etc.]

---

## 🛠️ Tecnologias Utilizadas

* [FastAPI](https://fastapi.tiangolo.com/)
* [Uvicorn](https://www.uvicorn.org/)
* [Poetry](https://python-poetry.org/)

---

## 📜 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
