import time
import os
import librosa
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# 1. Import your core modules (Ensure these files exist in the same folder)
from core.features import get_pirm_features
from core.augment import apply_white_noise, apply_spectral_muffling, apply_prosodic_instability

# Path provided by you
BASE_PATH = r"C:\fastapi_project\nishimiya_reserch_paper\.venv\Lib\pirm_module\data\raw"

# Files from your screenshot
filenames = [
    "844424930501837-229-f.wav",
    "844424930526976-229-f.wav",
    "844424930552419-229-f.wav",
    "844424930553861-229-f.wav",
    "844424930594715-929-m.wav",
    "844424930599278-3-f.wav",
    "844424930600457-888-f.wav"
]

audio_paths = [os.path.join(BASE_PATH, f) for f in filenames]

# Mock labels for 7 files (Replace with actual character classes if known)
# E.g., [0, 0, 1, 1, 2, 3, 4] representing different phonemes
labels = [0, 1, 2, 3, 4, 5, 6] 

def extract_features_from_array(y, sr=16000, n_mfcc=40):
    """Helper to extract MFCCs from an audio array (needed for augmented audio)"""
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=n_mfcc)
    return np.mean(mfccs.T, axis=0)

def run_pirm_validation():
    # --- TRAINING PHASE ---
    print("Extracting baseline features for training...")
    X_train = [get_pirm_features(p) for p in audio_paths]
    
    # Initialize Random Forest as specified in your paper
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train, labels)
    
    print("\n" + "="*90)
    print("   PIRM VALIDATION: TABLE II - ACCURACY & LATENCY RESULTS")
    print("="*90)
    print(f"{'Condition':<30} | {'Accuracy':<12} | {'Pipeline (ms)':<15} | {'PIRM Inference (ms)':<15}")
    print("-"*90)

    # --- TESTING CONDITIONS ---
    # Define augmentation functions with proper parameter handling
    conditions = {
        "Baseline (Clear)": None,  # No augmentation
        "Prosodic Instability": apply_prosodic_instability,
        "Spectral Muffling": apply_spectral_muffling,
        "Additive White Noise": apply_white_noise
    }

    results = []
    
    for name, transform_func in conditions.items():
        # PHASE 1: Load, augment, and extract features (measured for pipeline latency)
        pipeline_start = time.perf_counter()
        X_test = []
        
        for path in audio_paths:
            y, sr = librosa.load(path, sr=16000)
            
            # Apply augmentation with proper parameter passing
            if transform_func is None:
                # Baseline: no transformation
                y_transformed = y
            elif name == "Prosodic Instability":
                # This function requires both y and sr
                y_transformed = transform_func(y, sr)
            elif name == "Spectral Muffling":
                # This function only takes y
                y_transformed = transform_func(y)
            elif name == "Additive White Noise":
                # This function takes y and optional noise_level
                y_transformed = transform_func(y)
            
            # Extract features from augmented audio
            features = extract_features_from_array(y_transformed, sr)
            X_test.append(features)
        
        pipeline_end = time.perf_counter()
        pipeline_latency_total = (pipeline_end - pipeline_start) * 1000  # Convert to ms
        pipeline_latency_per_sample = pipeline_latency_total / len(audio_paths)
        
        # PHASE 2: Measure PIRM Inference ONLY (clf.predict)
        inference_start = time.perf_counter()
        preds = clf.predict(X_test)
        inference_end = time.perf_counter()
        
        # Calculate inference latency per sample
        inference_latency_total = (inference_end - inference_start) * 1000  # Convert to ms
        inference_latency_per_sample = inference_latency_total / len(audio_paths)
        
        # Calculate metrics
        accuracy = accuracy_score(labels, preds) * 100
        
        results.append({
            'condition': name,
            'accuracy': accuracy,
            'pipeline_latency': pipeline_latency_per_sample,
            'inference_latency': inference_latency_per_sample
        })
        
        print(f"{name:<30} | {accuracy:>6.2f}%       | {pipeline_latency_per_sample:>6.3f}         | {inference_latency_per_sample:>6.3f}           ")
    
    print("="*90)

if __name__ == "__main__":
    run_pirm_validation()