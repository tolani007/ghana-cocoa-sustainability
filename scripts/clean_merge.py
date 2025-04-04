"""
clean_merge.py
---------------
Clean and merge cocoa yield, rainfall, and temperature datasets for Ghana (1961–2023)
"""

import pandas as pd

#  1. Load the datasets 
yield_df = pd.read_excel("data/annual_ghana_average_yield_dataset.xls")
rain_df = pd.read_excel("data/annual_ghana_average_rain_dataset.xlsx")
temp_df = pd.read_excel("data/annual_ghana_average_temperature_dataset.xlsx")

#  2. Reshape climate data 
def reshape_climate(df, value_col):
    df = df.drop(columns=["code", "name"])  # Drop metadata columns
    df = df.T.reset_index()  # Transpose years to rows
    df.columns = ["Date", value_col]  # Rename
    df["Year"] = df["Date"].str.extract(r"(\d{4})").astype(int)
    df = df[df["Year"].between(1961, 2023)]
    df[value_col] = pd.to_numeric(df[value_col], errors="coerce")
    return df[["Year", value_col]]

rain_clean = reshape_climate(rain_df, "Rainfall_mm")
temp_clean = reshape_climate(temp_df, "AvgTemp_C")

#  3. Clean yield data 
yield_clean = yield_df[["Year", "Value"]].copy()
yield_clean = yield_clean[yield_clean["Year"].between(1961, 2023)]
yield_clean.rename(columns={"Value": "Yield_kg_per_ha"}, inplace=True)

#  4. Merge all data 
merged = yield_clean.merge(rain_clean, on="Year").merge(temp_clean, on="Year")

#  5. Save merged file
merged.to_csv("data/merged_cocoa_climate.csv", index=False)
print("✅ Merged data saved to /data/merged_cocoa_climate.csv (1961–2023)")
