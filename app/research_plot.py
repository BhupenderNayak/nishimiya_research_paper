import requests
import time
import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from urllib.parse import quote
import os

BASE_URL = "http://127.0.0.1:8000/process_speech/"
OUTPUT_DIR = "research_outputs"

# ----------------------------
# INPUT DESIGN
# ----------------------------

HINDI_CHARS = list("कखगघचछजझटठडढतथदधनपफबभमयरलवशषसह")

CATEGORIES = {
    "simple": ["क", "ग", "त", "न", "प"],
    "matra": ["का", "की", "कु", "के", "को"],
    "complex": ["कक्षा", "प्रश्न", "श्रद्धा", "दृष्टि"]
}

def random_word(length):
    return "".join(random.choice(HINDI_CHARS) for _ in range(length))


# ----------------------------
# CORE API CALL
# ----------------------------

def call_api(text):
    url = BASE_URL + quote(text)
    
    start = time.perf_counter()
    response = requests.get(url)
    total_time = (time.perf_counter() - start) * 1000

    if response.status_code != 200:
        return None

    backend_time = float(response.headers.get("X-Process-Time", total_time))
    output_states = len(response.json())

    return {
        "length": len(text),
        "latency": backend_time,
        "output_states": output_states
    }


# ----------------------------
# BENCHMARK
# ----------------------------

def warmup():
    for _ in range(5):
        requests.get(BASE_URL + "नमस्ते")


def states_benchmark():
    data = []
    print("Running states benchmark...")

    for length in range(1, 51):
        for _ in range(15):  # controlled iterations
            text = random_word(length)
            res = call_api(text)
            if res:
                data.append(res)

    return pd.DataFrame(data)


def category_benchmark():
    data = []
    print("Running category benchmark...")

    for cat, words in CATEGORIES.items():
        for word in words:
            for _ in range(20):
                res = call_api(word)
                if res:
                    res["category"] = cat
                    data.append(res)

    return pd.DataFrame(data)


# ----------------------------
# PLOT 1: STATES (BINNED)
# ----------------------------

def plot_states(df):
    # BINNING → removes noisy dips
    df["state_bin"] = (df["output_states"] // 2) * 2

    grouped = df.groupby("state_bin")["latency"].median()

    plt.figure(figsize=(10, 6))

    plt.plot(grouped.index, grouped.values, marker="o", linewidth=2)

    plt.xlabel("Phonetic State Count (Binned)")
    plt.ylabel("Latency (ms)")
    plt.title("Latency vs  Generated Phonetic State Complexity")
    plt.grid(True)

    plt.savefig(f"{OUTPUT_DIR}/states_latency.png", dpi=300)
    plt.close()


# ----------------------------
# PLOT 2: CATEGORY
# ----------------------------

def plot_category(df):
    categories = ["simple", "matra", "complex"]
    data = [df[df["category"] == c]["latency"] for c in categories]

    plt.figure(figsize=(10, 6))

    plt.boxplot(data, tick_labels=categories, showfliers=False)

    plt.xlabel("Input Category")
    plt.ylabel("Latency (ms)")
    plt.title("Latency by Linguistic Complexity")
    plt.grid(True)

    plt.savefig(f"{OUTPUT_DIR}/category_latency.png", dpi=300)
    plt.close()


# ----------------------------
# MAIN
# ----------------------------

if __name__ == "__main__":
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    warmup()

    states_df = states_benchmark()
    category_df = category_benchmark()

    states_df.to_csv(f"{OUTPUT_DIR}/states_data.csv", index=False)
    category_df.to_csv(f"{OUTPUT_DIR}/category_data.csv", index=False)

    plot_states(states_df)
    plot_category(category_df)

    print("✅ Final paper graphs generated in 'research_outputs/'")