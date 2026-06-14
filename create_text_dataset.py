import pandas as pd

data = {
    "Model Name": [
        "GPT-5.5",
        "Gemini 2.5 Pro",
        "Gemini 3.1 Pro",
        "Claude Sonnet 4.6",
        "Claude Opus 4.8",
        "Claude Fable 5",
        "Grok 4.3"
    ],
    "Company": [
        "OpenAI",
        "Google",
        "Google",
        "Anthropic",
        "Anthropic",
        "Anthropic",
        "xAI"
    ],
    "Release Year": [
        2026,
        2025,
        2026,
        2026,
        2026,
        2026,
        2026
    ],
    "Estimated Training Cost (USD Millions)": [
        500,
        250,
        350,
        200,
        500,
        750,
        500
    ],
    "Input Token Cost (USD per 1M Tokens)": [
        5.00,
        1.25,
        2.00,
        3.00,
        5.00,
        10.00,
        1.25
    ],
    "Output Token Cost (USD per 1M Tokens)": [
        30.00,
        10.00,
        12.00,
        15.00,
        25.00,
        50.00,
        2.50
    ],
    "Coding Productivity Score": [
        88.7,
        63.8,
        80.6,
        79.6,
        88.6,
        95.0,
        70.8
    ],
    "Data Analysis Productivity Score": [
        93.2,
        84.0,
        94.3,
        74.1,
        93.6,
        95.0,
        90.1
    ],
    "Literature Research Productivity Score": [
        92.4,
        89.8,
        90.1,
        91.8,
        92.0,
        91.5,
        91.0
    ],
    "AA Intelligence Index": [
        60,
        35,
        57,
        52,
        61,
        65,
        53
    ],
    "Context Window (Tokens)": [
        1000000,
        1000000,
        1000000,
        1000000,
        1000000,
        1000000,
        1000000
    ],
    "Output Speed (Tokens per Sec)": [
        53.2,
        127.7,
        110.1,
        44.5,
        57.5,
        60.3,
        143.5
    ],
    "Knowledge Cutoff": [
        "December 2025",
        "January 2025",
        "January 2025",
        "August 2025",
        "January 2026",
        "January 2026",
        "December 2025"
    ]
}

df = pd.DataFrame(data)
df.to_csv("text_models_dataset.csv", index=False)
print(df.to_string())
