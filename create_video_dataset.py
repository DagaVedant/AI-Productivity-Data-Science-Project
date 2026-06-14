import pandas as pd

data = {
    "Model Name": [
        "Happy Horse 1.0",
        "Seedance 2.0",
        "Kling 3.0",
        "Runway Gen-4.5",
        "Grok Imagine",
        "Veo 3.1",
        "LTX-2 Pro",
        "Pika 2.5",
        "Sora 2",
        "Sora 2 Pro"
    ],
    "Company": [
        "Alibaba",
        "ByteDance",
        "Kuaishou",
        "Runway",
        "xAI",
        "Google",
        "Lightricks",
        "Pika",
        "OpenAI",
        "OpenAI"
    ],
    "Arena Elo (No Audio)": [
        1293,
        1274,
        1250,
        1247,
        1235,
        1245,
        1135,
        1195,
        1130,
        1150
    ],
    "Cost per Second (USD)": [
        0.22,
        0.15,
        0.34,
        0.05,
        0.07,
        0.40,
        0.06,
        0.03,
        0.10,
        0.50
    ],
    "Max Clip Length (Sec)": [
        10,
        20,
        15,
        10,
        15,
        60,
        20,
        5,
        15,
        25
    ],
    "Max Resolution": [
        "1080p",
        "1080p",
        "4K",
        "720p",
        "720p",
        "4K",
        "4K",
        "1080p",
        "1080p",
        "1080p"
    ],
    "Native Audio": [
        "Yes",
        "Yes",
        "Yes",
        "No",
        "Yes",
        "Yes",
        "Yes",
        "Limited",
        "Yes",
        "Yes"
    ]
}

df = pd.DataFrame(data)
df.to_csv("video_models_dataset.csv", index=False)
print(df.to_string())
