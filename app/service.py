from __future__ import annotations

import unicodedata
from typing import List

try:
    from app.models import PhoneticState
    from app.data import (
        PHONETIC_MAP,
        MATRA_MAP,
        HALANT,
        INDEPENDENT_TOKENS,
        DIACRITIC_SIGNS,
        SKIP_CHARS,
    )
except ModuleNotFoundError:
    from models import PhoneticState
    from data import (
        PHONETIC_MAP,
        MATRA_MAP,
        HALANT,
        INDEPENDENT_TOKENS,
        DIACRITIC_SIGNS,
        SKIP_CHARS,
    )

MAX_TOKEN_LEN = max(len(token) for token in PHONETIC_MAP.keys())
SPECIAL_TOKENS = INDEPENDENT_TOKENS | DIACRITIC_SIGNS
CONSONANTAL_TOKENS = set(PHONETIC_MAP.keys()) - SPECIAL_TOKENS

LONG_VOWELS = {"आ", "ई", "ऊ", "ए", "ऐ", "ओ", "औ", "ॠ"}
SHORT_VOWELS = {"अ", "इ", "उ", "ऋ", "अं", "अः", "ं", "ँ", "ः"}


def _make_state(token: str, duration: float) -> PhoneticState:
    data = PHONETIC_MAP[token]
    return PhoneticState(char=token, duration=duration, **data)


def _match_longest_token(text: str, start: int) -> str | None:
    remaining = len(text) - start
    for size in range(min(MAX_TOKEN_LEN, remaining), 0, -1):
        candidate = text[start : start + size]
        if candidate in PHONETIC_MAP:
            return candidate
    return None


def _duration_for_token(token: str) -> float:
    if token in LONG_VOWELS:
        return 0.20
    if token in SHORT_VOWELS:
        return 0.10
    if token in {"क्ष", "त्र", "ज्ञ", "श्र"}:
        return 0.12
    return 0.10


def get_phonetic_sequence(text: str) -> List[PhoneticState]:
    text = unicodedata.normalize("NFC", text)
    sequence: List[PhoneticState] = []

    i = 0
    while i < len(text):
        char = text[i]

        if char in SKIP_CHARS or char.isspace():
            i += 1
            continue

        matched = _match_longest_token(text, i)
        if matched:
            sequence.append(_make_state(matched, _duration_for_token(matched)))
            i += len(matched)

            if matched in CONSONANTAL_TOKENS:
                if i < len(text):
                    next_char = text[i]

                    if next_char == HALANT:
                        i += 1
                    elif next_char in MATRA_MAP:
                        vowel = MATRA_MAP[next_char]
                        if vowel in PHONETIC_MAP:
                            sequence.append(_make_state(vowel, _duration_for_token(vowel)))
                        i += 1
                    else:
                        sequence.append(_make_state("अ", _duration_for_token("अ")))
            continue

        if char in PHONETIC_MAP:
            sequence.append(_make_state(char, _duration_for_token(char)))
            i += 1
            continue

        i += 1

    return sequence