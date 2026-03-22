import logging
import time
from typing import List

from fastapi import FastAPI, Request

from app.models import PhoneticState
from app.service import get_phonetic_sequence

logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger("ResearchLogger")

app = FastAPI(title="Project Nishimiya")


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.perf_counter()
    response = await call_next(request)
    process_time = (time.perf_counter() - start_time) * 1000

    if request.url.path.startswith("/process_speech/"):
        input_text = request.path_params.get("text", "")
        logger.info(f"{len(input_text)},{process_time:.4f}")

    response.headers["X-Process-Time"] = f"{process_time:.4f}"
    return response


@app.get("/process_speech/{text}", response_model=List[PhoneticState])
async def process_speech(text: str):
    return get_phonetic_sequence(text)

