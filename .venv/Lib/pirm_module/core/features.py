import librosa
import numpy as np

def get_pirm_features(audio_path, n_mfcc=40):
    """Extracts 40-dimensional MFCCs to capture spectral envelopes."""
    y, sr = librosa.load(audio_path, sr=16000)
    # Extract MFCCs [cite: 97]
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=n_mfcc)
    # Return the mean across time frames for a single feature vector
    return np.mean(mfccs.T, axis=0)