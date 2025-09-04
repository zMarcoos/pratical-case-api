from io import BytesIO
from pdfminer.high_level import extract_text


def extract_from_pdf(file_stream) -> str:
    if isinstance(file_stream, bytes):
        file_stream = BytesIO(file_stream)

    file_stream.seek(0)

    return extract_text(file_stream)
