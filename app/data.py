# The complete 52-character mapping translated to a Python dictionary
PHONETIC_MAP = {
    "अ": {"viseme": "neutral", "prana": False, "ghosha": True, "tongue": "velar"},
    "आ": {"viseme": "open", "prana": False, "ghosha": True, "tongue": "velar"},
    "इ": {"viseme": "wide", "prana": False, "ghosha": True, "tongue": "palatal"},
    "ई": {"viseme": "wide", "prana": False, "ghosha": True, "tongue": "palatal"},
    "उ": {"viseme": "puckered", "prana": False, "ghosha": True, "tongue": "labial"},
    "ऊ": {"viseme": "puckered", "prana": False, "ghosha": True, "tongue": "labial"},
    "ए": {"viseme": "wide", "prana": False, "ghosha": True, "tongue": "palatal"},
    "ऐ": {"viseme": "wide", "prana": False, "ghosha": True, "tongue": "palatal"},
    "ओ": {"viseme": "puckered", "prana": False, "ghosha": True, "tongue": "labial"},
    "औ": {"viseme": "puckered", "prana": False, "ghosha": True, "tongue": "labial"},
    "क": {"viseme": "neutral", "prana": False, "ghosha": False, "tongue": "velar"},
    "ख": {"viseme": "neutral", "prana": True, "ghosha": False, "tongue": "velar"},
    "ग": {"viseme": "neutral", "prana": False, "ghosha": True, "tongue": "velar"},
    "घ": {"viseme": "neutral", "prana": True, "ghosha": True, "tongue": "velar"},
    "ङ": {"viseme": "neutral", "prana": False, "ghosha": True, "tongue": "velar"},
    "च": {"viseme": "neutral", "prana": False, "ghosha": False, "tongue": "palatal"},
    "छ": {"viseme": "neutral", "prana": True, "ghosha": False, "tongue": "palatal"},
    "ज": {"viseme": "neutral", "prana": False, "ghosha": True, "tongue": "palatal"},
    "झ": {"viseme": "neutral", "prana": True, "ghosha": True, "tongue": "palatal"},
    "ञ": {"viseme": "neutral", "prana": False, "ghosha": True, "tongue": "palatal"},
    "ट": {"viseme": "neutral", "prana": False, "ghosha": False, "tongue": "retroflex"},
    "ठ": {"viseme": "neutral", "prana": True, "ghosha": False, "tongue": "retroflex"},
    "ड": {"viseme": "neutral", "prana": False, "ghosha": True, "tongue": "retroflex"},
    "ढ": {"viseme": "neutral", "prana": True, "ghosha": True, "tongue": "retroflex"},
    "ण": {"viseme": "neutral", "prana": False, "ghosha": True, "tongue": "retroflex"},
    "त": {"viseme": "neutral", "prana": False, "ghosha": False, "tongue": "dental"},
    "थ": {"viseme": "neutral", "prana": True, "ghosha": False, "tongue": "dental"},
    "द": {"viseme": "neutral", "prana": False, "ghosha": True, "tongue": "dental"},
    "ध": {"viseme": "neutral", "prana": True, "ghosha": True, "tongue": "dental"},
    "न": {"viseme": "neutral", "prana": False, "ghosha": True, "tongue": "dental"},
    "प": {"viseme": "closed", "prana": False, "ghosha": False, "tongue": "labial"},
    "फ": {"viseme": "closed", "prana": True, "ghosha": False, "tongue": "labial"},
    "ब": {"viseme": "closed", "prana": False, "ghosha": True, "tongue": "labial"},
    "भ": {"viseme": "closed", "prana": True, "ghosha": True, "tongue": "labial"},
    "म": {"viseme": "closed", "prana": False, "ghosha": True, "tongue": "labial"},
    "य": {"viseme": "wide", "prana": False, "ghosha": True, "tongue": "palatal"},
    "र": {"viseme": "neutral", "prana": False, "ghosha": True, "tongue": "retroflex"},
    "ल": {"viseme": "neutral", "prana": False, "ghosha": True, "tongue": "dental"},
    "व": {"viseme": "puckered", "prana": False, "ghosha": True, "tongue": "labial"},
    "श": {"viseme": "neutral", "prana": True, "ghosha": False, "tongue": "palatal"},
    "ष": {"viseme": "neutral", "prana": True, "ghosha": False, "tongue": "retroflex"},
    "स": {"viseme": "neutral", "prana": True, "ghosha": False, "tongue": "dental"},
    "ह": {"viseme": "open", "prana": True, "ghosha": True, "tongue": "velar"},
    "क्ष": {"viseme": "neutral", "prana": True, "ghosha": False, "tongue": "retroflex"},
    "त्र": {"viseme": "neutral", "prana": True, "ghosha": False, "tongue": "retroflex"},
    "ज्ञ": {"viseme": "neutral", "prana": False, "ghosha": True, "tongue": "palatal"},
    "श्र": {"viseme": "neutral", "prana": True, "ghosha": False, "tongue": "palatal"},
    "अं": {"viseme": "neutral", "prana": False, "ghosha": True, "tongue": "velar"},
    "अः": {"viseme": "open", "prana": True, "ghosha": False, "tongue": "velar"}
}

MATRA_MAP = {
    'ा': 'आ', 'ि': 'इ', 'ी': 'ई', 'ु': 'उ', 'ू': 'ऊ',
    'े': 'ए', 'ै': 'ऐ', 'ो': 'ओ', 'ौ': 'औ', 'ृ': 'र' 
}

HALANT = '्'

PHONETIC_MAP.update({
    "ऋ": {"viseme": "neutral", "prana": False, "ghosha": True, "tongue": "retroflex"},
    "ॠ": {"viseme": "neutral", "prana": False, "ghosha": True, "tongue": "retroflex"},
    "ं": {"viseme": "neutral", "prana": False, "ghosha": True, "tongue": "velar"},
    "ँ": {"viseme": "neutral", "prana": False, "ghosha": True, "tongue": "velar"},
    "ः": {"viseme": "open", "prana": True, "ghosha": False, "tongue": "velar"},
})

MATRA_MAP = {
    'ा': 'आ', 'ि': 'इ', 'ी': 'ई', 'ु': 'उ', 'ू': 'ऊ',
    'े': 'ए', 'ै': 'ऐ', 'ो': 'ओ', 'ौ': 'औ', 'ृ': 'ऋ'
}

INDEPENDENT_TOKENS = {
    "अ", "आ", "इ", "ई", "उ", "ऊ", "ए", "ऐ", "ओ", "औ",
    "ऋ", "ॠ", "अं", "अः"
}

DIACRITIC_SIGNS = {"ं", "ँ", "ः"}

SKIP_CHARS = set(" \t\n\r.,;:!?।॥…-–—()[]{}<>/\\|\"'“”‘’")