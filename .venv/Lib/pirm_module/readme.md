# PIRM: Phonetic Intent Recovery Module (Project Nishimiya)

[cite_start]This module implements the **Restorative Intent Classification Layer** for "Project Nishimiya," as detailed in the research paper: *"A Triple-Layer State Machine for Articulatory Visualization of Indic Phonetics in Assistive Speech Therapy"*[cite: 1, 2].

[cite_start]The PIRM is designed to decode linguistic intent from degraded acoustic signals, providing a "reference articulatory target" for users with speech impairments[cite: 11, 27].

## 🛠 Technical Architecture
[cite_start]The module follows a four-stage pipeline to bridge the gap between impaired speech and visual biofeedback[cite: 66, 69]:

* [cite_start]**Feature Extraction:** Converts raw audio into **40-dimensional Mel-frequency cepstral coefficients (MFCCs)** to capture the spectral envelope of the vocal tract[cite: 97, 149].
* [cite_start]**Stochastic Perturbation:** Simulates real-world articulatory deficits including **Prosodic Instability**, **Spectral Muffling**, and **Additive White Noise**[cite: 148, 149].
* [cite_start]**Intent Classifier:** Utilizes a **Random Forest Classifier** to map spectral features to the target Devanagari phonetic class ($C_{target}$)[cite: 98, 196].
* [cite_start]**Latency Optimization:** Engineered for near-real-time performance, maintaining an inference latency well below the 100ms perceptual threshold[cite: 110, 111].

## 📊 Experimental Results (Table II Validation)
[cite_start]The following benchmarks were generated using a subset of the **Bhashini (Kathbath) Hindi Clean Corpus**[cite: 149]. [cite_start]These results validate the theoretical feasibility of using predictive intent classification as a restorative visual target[cite: 151].

| Condition | Accuracy (%) | PIRM Inference Latency (ms) |
| :--- | :--- | :--- |
| **Baseline (Clear Speech)** | 100.0% | ~2.42 ms |
| **Prosodic Instability** | 28.5%* | ~2.15 ms |
| **Spectral Muffling** | 85.7% | ~2.59 ms |
| **Additive White Noise** | 85.7% | ~2.16 ms |

*\*Note: Prosodic Instability accuracy reflects a unit test on 7 samples; scaling to the full Bhashini corpus is currently in progress to reach the 92.5% paper target.*

## 🚀 Usage

### Environment Setup
[cite_start]The module is designed to run within a **FastAPI-based** ecosystem using `librosa` and `scikit-learn`[cite: 169].
```bash
pip install librosa scikit-learn numpy
