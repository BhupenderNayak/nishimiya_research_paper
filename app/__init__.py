"""
Project Nishimiya: Phonetic Decomposition Backend
An AI-driven visual speech therapy tool for Indic languages.

This module handles the Grapheme-to-Phoneme (G2P) conversion,
mapping Devanagari text to an accurate 4-attribute visual state machine.
"""

__version__ = "1.0.0"
__author__ = "Bhupender Nayak"

# You can optionally expose key components at the top level of the package, 
# though it's not strictly necessary for our current FastAPI setup.
from .models import PhoneticState, Viseme, TonguePosition