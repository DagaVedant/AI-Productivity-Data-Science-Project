import pandas as pd

data = {
    "Model Name": [
        "GPT-4o",
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
        "OpenAI",
        "Google",
        "Google",
        "Anthropic",
        "Anthropic",
        "Anthropic",
        "xAI"
    ],
    "Release Year": [
        2024,
        2026,
        2025,
        2026,
        2026,
        2026,
        2026,
        2026
    ],
    "Estimated Training Cost (USD Millions)": [
        100,
        500,
        250,
        350,
        200,
        500,
        750,
        500
    ],
    "Input Token Cost (USD per 1M Tokens)": [
        2.50,
        5.00,
        1.25,
        2.00,
        3.00,
        5.00,
        10.00,
        1.25
    ],
    "Output Token Cost (USD per 1M Tokens)": [
        10.00,
        30.00,
        10.00,
        12.00,
        15.00,
        25.00,
        50.00,
        2.50
    ],
    "Coding Productivity Score": [
        38.8,
        88.7,
        63.8,
        80.6,
        79.6,
        88.6,
        95.0,
        70.8
    ],
    "Data Analysis Productivity Score": [
        54.3,
        93.2,
        84.0,
        94.3,
        74.1,
        93.6,
        95.0,
        90.1
    ],
    "Literature Research Productivity Score": [
        88.7,
        92.4,
        89.8,
        90.1,
        91.8,
        92.0,
        91.5,
        91.0
    ]
}

df = pd.DataFrame(data)
df.to_csv("ai_models_dataset.csv", index=False)
print(df.to_string())