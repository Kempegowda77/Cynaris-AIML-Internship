"""
W1D2 - Pandas Data Manipulation

Loads Indian census demographic and population datasets,
cleans numeric fields, performs Pandas transformations,
and exports the cleaned dataset to CSV and Parquet.
"""

import os
from pathlib import Path

import pandas as pd


DATA_DIR = Path("data")
DEMOGRAPHICS_FILE = DATA_DIR / "census_demographics.csv"
POPULATION_FILE = DATA_DIR / "census_population.csv"


print("=" * 60)
print("W1D2 - Pandas Data Manipulation")
print("=" * 60)

# Validate that the required dataset files exist before loading.
for file_path in [DEMOGRAPHICS_FILE, POPULATION_FILE]:
    if not file_path.exists():
        raise FileNotFoundError(f"Dataset not found: {file_path}")

# Load both Indian Census CSV datasets using UTF-8 encoding.
demographics = pd.read_csv(DEMOGRAPHICS_FILE, encoding="utf-8")
population = pd.read_csv(POPULATION_FILE, encoding="utf-8")

# Remove accidental whitespace from column names.
demographics.columns = demographics.columns.str.strip()
population.columns = population.columns.str.strip()

print("\n--- Dataset Information ---")
print("Demographics shape:", demographics.shape)
print("Demographics dtypes:\n", demographics.dtypes)
print("Demographics head(10):\n", demographics.head(10))

print("\nPopulation shape:", population.shape)
print("Population dtypes:\n", population.dtypes)

# Clean numeric columns by removing formatting characters and converting safely.
demographics["Growth"] = pd.to_numeric(
    demographics["Growth"].astype(str).str.rstrip("%"),
    errors="coerce",
)

population["Area_km2"] = pd.to_numeric(
    population["Area_km2"].astype(str).str.replace(",", ""),
    errors="coerce",
)

population["Population"] = pd.to_numeric(
    population["Population"].astype(str).str.replace(",", ""),
    errors="coerce",
)

# Check for missing values created during numeric conversion.
numeric_columns = ["Growth", "Sex_Ratio", "Literacy"]
print("\n--- Missing Value Check ---")
missing_values = demographics[numeric_columns].isna().sum()
print(missing_values[missing_values > 0])

population_missing = population[["Area_km2", "Population"]].isna().sum()
print(population_missing[population_missing > 0])

# FILTER: Select districts with literacy above 90%.
filtered = demographics.loc[demographics["Literacy"] > 90].copy()

if filtered.empty:
    raise ValueError("No districts passed the literacy filter.")

print("\n--- Filter: Literacy > 90 ---")
print(filtered[["District", "State", "Literacy"]].head(10))

# GROUPBY: Calculate state-level average literacy, average growth,
# and number of districts.
state_grouped = (
    demographics.groupby("State")
    .agg(
        average_literacy=("Literacy", "mean"),
        average_growth=("Growth", "mean"),
        district_count=("District", "nunique"),
    )
    .reset_index()
)

print("\n--- Groupby: State Statistics ---")
print(state_grouped.head(10))

# MERGE: Combine demographic and population data using District and State.
merged = pd.merge(
    demographics,
    population,
    on=["District", "State"],
    how="inner",
    suffixes=("_demographics", "_population"),
)

if merged.empty:
    raise ValueError("Merge produced an empty DataFrame.")

print("\n--- Merge: Demographics + Population ---")
print("Merged shape:", merged.shape)
print(merged.head(10))

# PIVOT_TABLE: Calculate average literacy by state.
state_pivot = pd.pivot_table(
    merged,
    index="State",
    values="Literacy",
    aggfunc="mean",
    fill_value=0,
)

print("\n--- Pivot Table: Average Literacy by State ---")
print(state_pivot.head(10))

# Export the cleaned DataFrame to CSV.
csv_path = DATA_DIR / "cleaned_census_data.csv"
merged.to_csv(csv_path, index=False)

# Export the cleaned DataFrame to compressed Parquet.
parquet_path = DATA_DIR / "cleaned_census_data.parquet"
merged.to_parquet(
    parquet_path,
    engine="pyarrow",
    compression="snappy",
    index=False,
)

# Compare exported file sizes in human-readable KB.
csv_size_kb = os.path.getsize(csv_path) / 1024
parquet_size_kb = os.path.getsize(parquet_path) / 1024

print("\n--- Export File Size Comparison ---")
print(f"CSV:     {csv_size_kb:.2f} KB")
print(f"Parquet: {parquet_size_kb:.2f} KB")

print("\n" + "=" * 60)
print("W1D2 COMPLETED SUCCESSFULLY")
print("=" * 60)
