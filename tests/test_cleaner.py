
import pandas as pd

from src.cleaner import DataCleaner


def test_clean_column_names():
    df = pd.DataFrame({
        "Order Date": ["2014-01-01"],
        "Customer Name": ["John Smith"]
    })

    cleaner = DataCleaner(df)
    cleaned_df = cleaner.clean_column_names()

    assert "Order_Date" in cleaned_df.columns
    assert "Customer_Name" in cleaned_df.columns


def test_convert_dates():
    df = pd.DataFrame({
        "Order_Date": ["2014-01-01", "invalid-date"]
    })

    cleaner = DataCleaner(df)
    cleaned_df = cleaner.convert_dates()

    assert pd.api.types.is_datetime64_any_dtype(
        cleaned_df["Order_Date"]
    )
    assert pd.isna(cleaned_df["Order_Date"].iloc[1])


def test_clean_numeric_columns():
    df = pd.DataFrame({
        "Sales": ["100.50", "250"],
        "Profit": ["20", "50"],
        "Quantity": ["2", "5"]
    })

    cleaner = DataCleaner(df)
    cleaned_df = cleaner.clean_numeric_columns()

    assert pd.api.types.is_numeric_dtype(cleaned_df["Sales"])
    assert cleaned_df["Sales"].iloc[0] == 100.50
    assert cleaned_df["Quantity"].iloc[1] == 5