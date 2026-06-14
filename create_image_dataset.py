import pandas as pd

data = {
    "Model Name": [
        "GPT Image 2",
        "GPT Image 1.5",
        "HiDream-O1-Image-1.5",
        "Nano Banana 2 (Gemini 3.1 Flash Image)",
        "Nano Banana Pro (Gemini 3 Pro Image)",
        "Seedream 4.0",
        "Flux 2 Pro",
        "Grok Imagine",
        "Imagen 4 Ultra",
        "Ideogram 3.0",
        "Recraft V4",
        "Imagen 4 Fast",
        "Midjourney v7"
    ],
    "Company": [
        "OpenAI",
        "OpenAI",
        "HiDream",
        "Google",
        "Google",
        "ByteDance",
        "Black Forest Labs",
        "xAI",
        "Google",
        "Ideogram",
        "Recraft",
        "Google",
        "Midjourney"
    ],
    "Arena Elo": [
        1338,
        1266,
        1264,
        1258,
        1218,
        1202,
        1181,
        1178,
        1173,
        1132,
        1119,
        1064,
        1228
    ],
    "Cost per Image (USD)": [
        0.02,
        0.05,
        0.03,
        0.02,
        0.13,
        0.03,
        0.04,
        0.02,
        0.06,
        0.03,
        0.04,
        0.02,
        0.10
    ],
    "Max Resolution": [
        "4K",
        "4K",
        "2K",
        "2K",
        "4K",
        "4K",
        "4K",
        "2K",
        "2K",
        "2K",
        "4K",
        "2K",
        "2K"
    ],
    "Weights": [
        "Proprietary",
        "Proprietary",
        "Open",
        "Proprietary",
        "Proprietary",
        "Proprietary",
        "Proprietary",
        "Proprietary",
        "Proprietary",
        "Proprietary",
        "Proprietary",
        "Proprietary",
        "Proprietary"
    ]
}

df = pd.DataFrame(data)
df.to_csv("image_models_dataset.csv", index=False)
print(df.to_string())
