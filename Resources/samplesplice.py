# shared for reference only - using the original 2Gb file not included
# on GitHub due to size restrictions

import pandas as pd

path = "Climate_Twitter.csv"

df = pd.read_csv(path)

cols = ["created_at", "lat", "lng", "sentiment", "topic", "stance", "gender", "aggressiveness"]

df_cut = df[cols]

sample = df_cut.sample(frac = 0.05)

print(sample.shape)

sample.to_csv("sample_05.csv", index=False)