import librosa
import numpy as np

def apply_prosodic_instability(y, sr=16000):
    # Pitch shifting (+/- 3 semitones) [cite: 149]
    return librosa.effects.pitch_shift(y, sr=sr, n_steps=3)

def apply_spectral_muffling(y):
    # Simulates low-pass filtering by rolling off high frequencies
    return np.convolve(y, np.ones(5)/5, mode='same')

def apply_white_noise(y, noise_level=0.005):
    # Additive White Gaussian Noise [cite: 149]
    noise = np.random.randn(len(y))
    return y + noise_level * noise