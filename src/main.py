import cleaner
from loader import DataLoader
from cleaner import DataCleaner


def main():

    # -------------------------
    # LOAD DATA
    # -------------------------

    loader = DataLoader("../data/raw")

    df = loader.load_all_files()

    print("\n## DATA LOADED SUCCESSFULLY")

    print(f"\nRows  : {df.shape[0]}")
    print(f"Columns: {df.shape[1]}")


    # -------------------------
    # CLEAN DATA
    # -------------------------

    cleaner = DataCleaner(df)

    clean_df = cleaner.clean()

    print("\n## DATA CLEANED SUCCESSFULLY")

    print(f"\nRows  : {clean_df.shape[0]}")
    print(f"Columns: {clean_df.shape[1]}")

    print("\nCleaned column names:")
    print(clean_df.columns.tolist())

    print("\nData types:")
    print(clean_df.dtypes)


if __name__ == "__main__":
    main()
