from io import BytesIO
from typing import Optional
from fastapi import APIRouter, Form, HTTPException, UploadFile, status
from models import classify
from utils import file_util
from processing import nlp, replies, classifier

router = APIRouter()

@router.post("/", response_model=classify.ClassifyResponse)
async def classify_email(
    text: Optional[str] = Form(default=None),
    file: Optional[UploadFile] = None
):
    if not text and not file:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Envie texto no campo 'text' ou um arquivo .txt/.pdf no campo 'file'.",
        )

    try:
        content = text or ""

        if file:
            content_bytes = await file.read()

            file_name = file.filename.lower()
            if file_name.endswith(".txt"):
                content = content_bytes.decode("utf-8", "ignore")
            elif file_name.endswith(".pdf"):
                pdf_stream = BytesIO(content_bytes)
                content = file_util.extract_from_pdf(pdf_stream)
            else:
                content = content_bytes.decode("utf-8", "ignore")
    except HTTPException:
        raise
    except Exception as exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Falha ao ler o arquivo/texto: {type(exception).__name__}"
        )

    clean = nlp.preprocess(content)
    category, confidence = classifier.classify(clean)
    suggested = replies.reply_productive(
    ) if category == "Produtivo" else replies.reply_unproductive()

    return classify.ClassifyResponse(
        category=category,
        confidence=confidence,
        suggested_reply=suggested
    )
