# Project Nishimiya

Project Nishimiya is a structured Hindi phonetic decomposition pipeline built to transform text into interpretable phonetic states for downstream use in animation, speech visualization, and assistive systems.

The project also includes a benchmark module that evaluates how backend latency scales with phonetic complexity.

## Overview

The system maps Hindi text into a structured phonetic representation using linguistic rules such as matra handling, halant processing, inherent vowel insertion, and conjunct recognition.

Each output state contains attributes such as viseme, prana, ghosha, and tongue position. This makes the output useful for rendering and other language-aware applications.

## Motivation

Most text-processing systems operate on raw characters. For applications like lip-sync animation, accessibility tools, and speech-based interfaces, that is not enough.

This project focuses on phonetic structure instead of plain text length. The main idea is that processing cost depends more on phonetic expansion than on raw character count.

## System Pipeline

Input Text  
→ Phonetic Decomposition (FastAPI backend)  
→ Structured Phonetic States  
→ Planned Rendering / Animation Layer  
→ Final Output

## Key Results

The benchmark results show two main patterns.

Latency increases as the number of generated phonetic states increases. This indicates that the computational cost is driven by internal phonetic expansion.

Latency also varies across linguistic categories. Simple inputs are faster, while matra-bearing and conjunct-heavy inputs show higher latency and slightly wider variation.

## Project Structure

project_nishimiya/
├── app/
│   ├── main.py
│   ├── service.py
│   ├── data.py
│   ├── models.py
│   └── research_plot.py
├── research_outputs/
├── requirements.txt
└── README.md

## Running the Project

Install dependencies:

```bash
pip install -r requirements.txt




This generates:

- `states_latency.png`
- `category_latency.png`

---

## 🔬 Research Insight

A key observation from this work:

> Latency is governed by phonetic state expansion rather than raw input length.

This highlights the importance of structured linguistic processing in real-world systems.

---

## 🧪 Future Work

- OpenCV-based phonetic rendering
- Real-time animation pipeline
- Optimization for large-scale inputs
- Integration with speech systems

---

## 📄 Paper

This work is being prepared as a Work-in-Progress (WIP) submission for IEEE INDICON under the AI for Social Impact track.

---

## 👤 Author

Bhupender Nayak  
DTU CSE

