import pandas as pd

class SalesAnalyzer:

   import pandas as pd


class SalesAnalyzer:

    def __init__(self, df):
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