import pandas as pd
from glob import glob

df = pd.read_csv(r"Samsung Health\samsunghealth_juliamgebara_20251215221761\com.samsung.shealth.tracker.heart_rate.20251215221761.csv", sep=';', encoding="utf-8")


print(df.columns)
