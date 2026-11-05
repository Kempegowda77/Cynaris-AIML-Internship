"""W1D3 - Data Loading, Cleaning & Inspection."""

from pathlib import Path
import logging
import pandas as pd

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

DATA_PATH = Path(__file__).parent / "data" / "census_raw.csv"


def load_data(path: Path) -> pd.DataFrame:
    """Load and inspect the Indian Census dataset."""
    if not path.exists():
        raise FileNotFoundError(f"Dataset not found: {path}")

    df = pd.read_csv(path, encoding="utf-8")

    if df.empty:
        raise ValueError("CSV dataset is empty.")

    df.columns = df.columns.str.strip()

    logging.info("Loaded dataset: %s rows x %s columns", *df.shape)

    return df


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Clean Growth values and remove duplicate rows."""
    df["Growth"] = pd.to_numeric(
        df["Growth"].astype(str)
        .str.replace("%", "", regex=False)
        .str.replace(",", "", regex=False)
        .str.strip(),
        errors="coerce",
    )

    duplicates = df.duplicated().sum()
    logging.info("Duplicate rows found: %s", duplicates)

    if duplicates > 0:
        df = df.drop_duplicates().reset_index(drop=True)

    return df


def validate_data(df: pd.DataFrame) -> None:
    """Validate the cleaned dataset."""
    missing = df.isna().sum()

    if missing.any():
        raise ValueError(f"Missing values detected:\n{missing[missing > 0]}")

    assert df.duplicated().sum() == 0, "Duplicates found after cleaning"
    assert pd.api.types.is_numeric_dtype(df["Growth"]), (
        "Growth column must be numeric"
    )


def main() -> None:
    """Run the complete loading, cleaning and inspection pipeline."""
    print("=" * 60)
    print("W1D3 - Data Loading, Cleaning & Inspection")
    print("=" * 60)

    df = load_data(DATA_PATH)

    print("\n--- Raw Dataset ---")
    print("Shape:", df.shape)
    print("Columns:", df.columns.tolist())
    print("\nData Types:")
    print(df.dtypes)
    print("\nFirst 10 Rows:")
    print(df.head(10))

    df = clean_data(df)
    validate_data(df)

    print("\n--- Cleaning Results ---")
    print("Missing values:")
    print(df.isna().sum())

    print("\n--- Numerical Summary ---")
    print(df.describe())

    print("\n--- Cleaned Dataset ---")
    print("Shape:", df.shape)
    print(df.head(10))

    print("\n" + "=" * 60)
    print("W1D3 COMPLETED SUCCESSFULLY")
    print("=" * 60)


if __name__ == "__main__":
    main()
