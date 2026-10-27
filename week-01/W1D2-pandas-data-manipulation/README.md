
# W1D2 — Pandas Data Manipulation

## Objective

Perform practical data manipulation using Pandas with a real Indian Census dataset.

## Tasks Completed

- Loaded Indian Census CSV datasets
- Inspected shape, dtypes, and head(10)
- Cleaned numeric columns
- Filtered districts by literacy
- Grouped data by state
- Merged demographic and population datasets
- Created a state-level pivot table
- Exported cleaned data to CSV
- Exported cleaned data to Parquet
- Compared CSV and Parquet file sizes

## Pandas Operations

- **Filter:** Selected districts with literacy above 90%.
- **GroupBy:** Calculated state-level average literacy, average growth, and district count.
- **Merge:** Combined demographic and population data using District and State.
- **Pivot Table:** Calculated average literacy by state.

## Self-Review

- [x] Dataset loads successfully
- [x] Shape, dtypes, and head(10) verified
- [x] Numeric values cleaned
- [x] Filter implemented
- [x] GroupBy implemented
- [x] Merge implemented
- [x] Pivot table implemented
- [x] CSV export verified
- [x] Parquet export verified
- [x] File sizes compared
- [x] CIA Interaction 1 completed
- [x] CIA Interaction 2 completed

## Viva Preparation

1. `loc` uses labels, while `iloc` uses integer positions.
2. `merge` combines DataFrames using matching keys; `join` is primarily index-based; `concat` combines DataFrames along an axis.
3. `groupby` splits data into groups, applies an aggregation, and combines the results.

## How to Run

```powershell
python pandas_data_manipulation.py
## Results

- Demographics rows: 640
- Population rows: 640
- Merged records: 606
- CSV size: 29.57 KB
- Parquet size: 26.18 KB
