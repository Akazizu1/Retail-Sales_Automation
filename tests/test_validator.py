
import pandas as pd

from src.validator import DataValidator


def create_valid_dataframe():
    return pd.DataFrame({
        "Order_ID": ["ORD-001", "ORD-002"],
        "Order_Date": pd.to_datetime(["2014-01-01", "2014-01-02"]),
        "Ship_Date": pd.to_datetime(["2014-01-03", "2014-01-04"]),
        "Customer_ID": ["C-001", "C-002"],
        "Product_ID": ["P-001", "P-002"],
        "Sales": [100.0, 200.0],
        "Quantity": [2, 4],
        "Profit": [20.0, 40.0],
        "Discount": [0.0, 0.1]
    })


def test_valid_data_has_no_errors_or_warnings():
    df = create_valid_dataframe()
    validator = DataValidator(df)

    errors, warnings = validator.validate()

    assert errors == []
    assert warnings == []


def test_missing_required_column_is_detected():
    df = create_valid_dataframe().drop(columns=["Customer_ID"])
    validator = DataValidator(df)

    errors, warnings = validator.validate()

    assert any("Customer_ID" in error for error in errors)


def test_duplicate_rows_are_detected():
    df = create_valid_dataframe()
    df = pd.concat([df, df.iloc[[0]]], ignore_index=True)
    validator = DataValidator(df)

    errors, warnings = validator.validate()

    assert any("duplicate" in warning.lower() for warning in warnings)


def test_missing_values_are_detected():
    df = create_valid_dataframe()
    df.loc[0, "Sales"] = None
    validator = DataValidator(df)

    errors, warnings = validator.validate()

    assert any("missing" in warning.lower() for warning in warnings)