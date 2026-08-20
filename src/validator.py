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

        return self.errors, self.warnings                    