
import pandas as pd
import pytest

from src.analyzer import SalesAnalyzer


@pytest.fixture
def sample_data():
    return pd.DataFrame({
        "Order_ID": ["ORD-001", "ORD-001", "ORD-002"],
        "Order_Date": pd.to_datetime([
            "2014-01-01",
            "2014-01-01",
            "2015-01-01"
        ]),
        "Sales": [100.0, 50.0, 200.0],
        "Profit": [20.0, 10.0, -10.0],
        "Quantity": [2, 1, 4],
        "Discount": [0.0, 0.1, 0.5],
        "Category": ["Technology", "Furniture", "Technology"],
        "Region": ["East", "West", "East"],
        "Product_Name": ["Product A", "Product B", "Product C"],
        "Customer_ID": ["C-001", "C-002", "C-001"],
        "Segment": ["Consumer", "Corporate", "Consumer"],
        "Ship_Mode": ["Standard Class", "First Class", "Standard Class"]
    })


def test_total_sales(sample_data):
    analyzer = SalesAnalyzer(sample_data)
    assert analyzer.total_sales() == pytest.approx(350.0)


def test_total_profit(sample_data):
    analyzer = SalesAnalyzer(sample_data)
    assert analyzer.total_profit() == pytest.approx(20.0)


def test_total_quantity(sample_data):
    analyzer = SalesAnalyzer(sample_data)
    assert analyzer.total_quantity() == 7


def test_average_order_value(sample_data):
    analyzer = SalesAnalyzer(sample_data)
    # Order 1 totals 150; Order 2 totals 200.
    assert analyzer.average_order_value() == pytest.approx(175.0)


def test_profit_margin(sample_data):
    analyzer = SalesAnalyzer(sample_data)
    assert analyzer.profit_margin() == pytest.approx(
        (20.0 / 350.0) * 100
    )


def test_sales_by_year(sample_data):
    analyzer = SalesAnalyzer(sample_data)
    result = analyzer.sales_by_year()

    assert result.loc[2014] == pytest.approx(150.0)
    assert result.loc[2015] == pytest.approx(200.0)


def test_sales_growth_by_year(sample_data):
    analyzer = SalesAnalyzer(sample_data)
    result = analyzer.sales_growth_by_year()

    assert pd.isna(result.loc[2014])
    assert result.loc[2015] == pytest.approx(
        (200.0 - 150.0) / 150.0 * 100
    )
