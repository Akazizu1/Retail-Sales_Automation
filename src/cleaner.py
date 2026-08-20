# src/cleaner.py

import pandas as pd


class DataCleaner:

    def __init__(self, df):
        self.df = df.copy()

    def clean_column_names(self):
        """
        Standardize column names.
        """

        self.df.columns = (
            self.df.columns
            .str.strip()
            .str.replace(r"\\.", ".", regex=True)
            .str.replace(".", "_")
            .str.replace(" ", "_")
        )

        return self.df

    def clean_text_columns(self):
        """
        Remove unnecessary whitespace from text columns.
        """

        text_columns = self.df.select_dtypes(
            include=["object"]
        ).columns

        for column in text_columns:
            self.df[column] = (
                self.df[column]
                .str.strip()
            )

        return self.df

    def convert_dates(self):
        """
        Convert date columns to datetime format.
        """

        date_columns = [
            "Order_Date",
            "Ship_Date"
        ]

        for column in date_columns:

            if column in self.df.columns:
                self.df[column] = pd.to_datetime(
                    self.df[column],
                    errors="coerce"
                )

        return self.df

    def clean_numeric_columns(self):
        """
        Ensure important numerical columns
        contain numeric values.
        """

        numeric_columns = [
            "Sales",
            "Profit",
            "Quantity",
            "Discount",
            "Shipping_Cost"
        ]

        for column in numeric_columns:

            if column in self.df.columns:
                self.df[column] = pd.to_numeric(
                    self.df[column],
                    errors="coerce"
                )

        return self.df

    def clean(self):
        """
        Run the complete cleaning pipeline.
        """

        self.clean_column_names()
        self.clean_text_columns()
        self.convert_dates()
        self.clean_numeric_columns()

        return self.df