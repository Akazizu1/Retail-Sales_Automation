from pathlib import Path

from loader import DataLoader
from cleaner import DataCleaner
from validator import DataValidator

def main():

    data_folder = Path(__file__).resolve().parent.parent / "data" / "raw"
    loader = DataLoader(data_folder)

    df = loader.load_all_files()

    print("\n## DATA LOADED SUCCESSFULLY")
    print(f"\nRows  : {df.shape[0]}")
    print(f"Columns: {df.shape[1]}")

    cleaner = DataCleaner(df)

    clean_df = cleaner.clean()

    print("\n## DATA CLEANED SUCCESSFULLY")
    print(f"\nRows  : {clean_df.shape[0]}")
    print(f"Columns: {clean_df.shape[1]}")

    validator = DataValidator(clean_df)
    errors, warnings = validator.validate()

    print("\n## DATA VALIDATION RESULTS")
    if errors:
        print("\nErrors:")
        for error in errors:
            print(f"- {error}")
    else:
        print("\nNo errors found.")

    if warnings:
        print("\nWarnings:")
        for warning in warnings:
            print(f"- {warning}")
    else:
        print("\nNo warnings found.")

if __name__ == "__main__":
    main()
           