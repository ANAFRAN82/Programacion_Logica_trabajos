import pandas as pd
df = pd.read_csv('datasets/TotalFeatures-ISCXFlowMeter.csv')

df_half = df.sample(frac=0.5, random_state=42)

df_half.to_csv('reduced.csv', index=False)