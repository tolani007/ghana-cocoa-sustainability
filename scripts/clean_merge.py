"""
clean_merge.py
---------------
Clean and merge cocoa yield, rainfall, and temperature datasets for Ghana (1961–2023)
"""

import pandas as pd

# === 1. Load the datasets ===
yield_df = pd.read_excel("data/annual_ghana_average_yield_dataset.xls", skiprows=0)
rain_df = pd.read_excel("data/annual_ghana_average_rain_dataset.xlsx", skiprows=0)
temp_df = pd.read_excel("data/annual_ghana_average_temperature_dataset.xlsx", skiprows=0)

# === 2. Transpose & Clean Rain and Temp ===
def reshape_climate(df, value_col):
    df = df.T.reset_index()
    df.columns = ['Year', value_col]
    df = df[df['Year'].str.contains("^\d{4}", regex=True)]  # Only keep rows with years
    df['Year'] = df['Year'].str[:4].astype(int)
    df[value_col] = pd.to_numeric(df[value_col], errors='coerce')
    df = df[df['Year'].between(1961, 2023)]  # ✅ filter by year
    return df

rain_df = reshape_climate(rain_df, "Precipitation_mm")
temp_df = reshape_climate(temp_df, "Avg_Temp_C")

# === 3. Clean Yield Dataset ===
yield_df = yield_df[["Year", "Value"]]
yield_df.columns = ["Year", "Yield_kg_per_ha"]
yield_df = yield_df[yield_df["Year"].between(1961, 2023)]  # ✅ apply same filter

# === 4. Merge all datasets ===
merged = yield_df.merge(rain_df, on="Year").merge(temp_df, on="Year")

# === 5. Export merged data ===
merged.to_csv("data/merged_cocoa_climate.csv", index=False)
print("✅ Merged data saved to /data/merged_cocoa_climate.csv (1961–2023)")
