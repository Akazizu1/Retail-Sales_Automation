import pandas as pd

class DataValidator:
    def __init__(self, df):
        self.df = df
        self.errors = []
        self.warnings = []

    def check_req_columns(self):
        """
        Check if the required columns are present in the DataFrame.
        """    

        required_columns = [
            "Order_ID",
            "Customer_ID",
            "Product_ID",
            "Quantity",
            "Order_Date",
            "Ship_Date"
        ]

        missing_columns = [
            col for col in required_columns if col not in self.df.columns
        ]

        if missing_columns:
            self.errors.append(
                f"Missing required columns: {', '.join(missing_columns)}"
            )

    def check_missing_values(self):
        """
        Check for missing values in the DataFrame.
        """

        missing_values = self.df.isnull().sum()

        for column, count in missing_values.items():
            if count > 0:
                self.warnings.append(
                    f"Column '{column}' has {count} missing values."
                )

    def check_duplicates(self):
        """
        Check for duplicate rows in the DataFrame.
        """

        duplicate_count = self.df.duplicated().sum()

        if duplicate_count > 0:
            self.warnings.append(
                f"There are {duplicate_count} duplicate rows in the DataFrame."
            )

    def validate(self):
        """
        Run all validation checks and return errors and warnings.
        """

        self.check_req_columns()
        self.check_missing_values()
        self.check_duplicates()
        self.check_numeric_values()
        self.check_dates()

        return self.errors, self.warnings

    def check_numeric_values(self):

        if "Sales" in self.df.columns:
            if(self.df["Sales"]<0).any():
                self.warnings.append("Negative Sales Found.")

        if "Quantity" in self.df.columns:
                if(self.df["Quantity"]<=0).any():
                    self.warning.append("Zero or negative quantites found.")

        if "Discount" in self.df.columns:
            if(self.df["Discount"]<0).any():
                self.warnings.append("Negative Discounts Found.")

        if "Shipping_Cost" in self.df.columns:
            if(self.df["Shipping_Cost"]<0).any():
                self.warnings.append("Negative Shipping Costs Found.")

    def check_dates(self):
        """
        Check whether shipping dates occur before order dates.
        """

        if "Order_Date" in self.df.columns and "Ship_Date" in self.df.columns:

         invalid_dates = (
            self.df["Ship_Date"] < self.df["Order_Date"]
        ).sum()

        if invalid_dates > 0:
            self.warnings.append(
                f"{invalid_dates} records have a Ship_Date "
                f"before the Order_Date."
            )