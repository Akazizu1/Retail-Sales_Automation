import pandas as pd

class SalesAnalyzer:

   import pandas as pd


class SalesAnalyzer:

    def __init__(self, df):
        self.df = df
        self.df = df
        

    def total_sales(self):
        """Calculate total sales."""

        return self.df["Sales"].sum()

    def total_profit(self):
        """Calculate total profit."""

        return self.df["Profit"].sum()

    def total_quantity(self):
        """Calculate total quantity sold."""

        return self.df["Quantity"].sum()

    def average_order_value(self):
        """Calculate average sales per order."""

        return self.df.groupby("Order_ID")["Sales"].sum().mean()

    def profit_margin(self):
        """Calculate overall profit margin."""

        total_sales = self.total_sales()

        if total_sales == 0:
            return 0

        return (self.total_profit() / total_sales) * 100

    def sales_by_category(self):
        """Calculate sales by product category."""

        return (
            self.df.groupby("Category")["Sales"]
            .sum()
            .sort_values(ascending=False)
        )

    def profit_by_category(self):
        """Calculate profit by product category."""

        return (
            self.df.groupby("Category")["Profit"]
            .sum()
            .sort_values(ascending=False)
        )

    def sales_by_region(self):
        """Calculate sales by region."""

        return (
            self.df.groupby("Region")["Sales"]
            .sum()
            .sort_values(ascending=False)
        )

    def profit_by_region(self):
        """Calculate profit by region."""

        return (
            self.df.groupby("Region")["Profit"]
            .sum()
            .sort_values(ascending=False)
        )

    def sales_by_segment(self):
        """Calculate sales by customer segment."""

        return (
            self.df.groupby("Segment")["Sales"]
            .sum()
            .sort_values(ascending=False)
        )

    def top_products(self, n=10):
        """Return top products by sales."""

        return (
            self.df.groupby("Product_Name")["Sales"]
            .sum()
            .sort_values(ascending=False)
            .head(n)
        )

    def top_customers(self, n=10):
        """Return top customers by sales."""

        return (
            self.df.groupby("Customer_Name")["Sales"]
            .sum()
            .sort_values(ascending=False)
            .head(n)
        )

    def sales_by_year(self):
        """Calculate sales by year."""

        self.df["Order_Date"] = pd.to_datetime(self.df["Order_Date"])
        return (
            self.df.groupby(self.df["Order_Date"].dt.year)["Sales"]
            .sum()
            .sort_index()
        )

    def sales_growth_by_year(self):
        """Calculate year-over-year sales growth."""

        yearly_sales = self.sales_by_year()

        return yearly_sales.pct_change() * 100

    def sales_by_month(self):
        """Calculate sales by month."""

        return (
            self.df.groupby(
                self.df["Order_Date"].dt.month
            )["Sales"]
            .sum()
            .sort_index()
        )
    def profit_by_year(self):
        """Calculate profit by year."""

        self.df["Order_Date"] = pd.to_datetime(self.df["Order_Date"])
        return (
            self.df.groupby(self.df["Order_Date"].dt.year)["Profit"]
            .sum()
            .sort_index()
        )
    def top_products_by_profit(self, n=10):
        """Return top products by profit."""
        return (
            self.df.groupby("Product_Name")["Profit"]
            .sum()
            .sort_values(ascending=False)
            .head(n)
        )

    def bottom_products_by_profit(self, n=10):
        """Return bottom products by profit."""
        return (
            self.df.groupby("Product_Name")["Profit"]
            .sum()
            .sort_values(ascending=True)
            .head(n)
        )
    def profit_by_discount(self):
        """Calculate profit by discount band."""

        df = self.df.copy()

        df["Discount_Band"] = pd.cut(
            df["Discount"],
            bins=[
                -0.01,
                0,
                0.10,
                0.20,
                0.40,
                1.00
            ],
            labels=[
                "No Discount",
                "Low (1-10%)",
                "Moderate (11-20%)",
                "High (21-40%)",
                "Very High (41%+)"
            ]
        )

        return (
            df.groupby(
                "Discount_Band",
                observed=False
            )
            .agg(
                Profit=("Profit", "sum"),
                Average_Profit=("Profit", "mean"),
                Records=("Profit", "count")
            )
        )

    def performance_by_ship_mode(self):
        """Calculate sales and profit by shipping mode."""
        return (
            self.df.groupby("Ship_Mode")
            .agg({
                "Sales": "sum",
                "Profit": "sum",
                "Order_ID": "nunique"
            })
            .sort_values(
                "Sales",
                ascending=False
            )
        )