from pathlib import Path
import pandas as pd


class DataLoader:

    def __init__(self, data_folder):
        self.data_folder = Path(data_folder)

    def get_data_files(self):
        """
        Finds all CSV and Excel files in the data folder.
        """
        csv_files = list(self.data_folder.glob("*.csv"))
        excel_files = list(self.data_folder.glob("*.xlsx"))

        return csv_files + excel_files

    def load_single_file(self, file_path):
        """
        Loads a single CSV or Excel file.
        """

        if file_path.suffix.lower() == ".csv":
            df = pd.read_csv(file_path)

        elif file_path.suffix.lower() == ".xlsx":
            df = pd.read_excel(file_path)

        else:
            raise ValueError(
                f"Unsupported file type: {file_path.suffix}"
            )

        return df

    def load_all_files(self):
        """
        Loads all supported files and combines them.
        """

        data_files = self.get_data_files()

        if not data_files:
            raise FileNotFoundError(
                "No CSV or Excel files found in the data folder."
            )

        dataframes = []

        for file in data_files:

            print(f"Loading file: {file}")

            df = self.load_single_file(file)

            # Keep track of where each row came from
            df["source_file"] = file.name

            dataframes.append(df)

        combined_df = pd.concat(
            dataframes,
            ignore_index=True
        )

        return combined_df