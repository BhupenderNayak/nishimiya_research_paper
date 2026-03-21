from pydantic import BaseModel
from enum import Enum

class Viseme(str, Enum):
    OPEN = "open"
    CLOSED = "closed"
    NEUTRAL = "neutral"
    PUCKERED = "puckered"
    WIDE = "wide"

class TonguePosition(str, Enum):
    VELAR = "velar"
    PALATAL = "palatal"
    RETROFLEX = "retroflex"
    DENTAL = "dental"
    LABIAL = "labial"

class PhoneticState(BaseModel):
    char: str
    viseme: Viseme
    prana: bool
    ghosha: bool
    tongue: TonguePosition
    duration: float