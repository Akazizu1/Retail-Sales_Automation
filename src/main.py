
from pathlib import Path

from loader import DataLoader
from cleaner import DataCleaner
from validator import DataValidator
from analyzer import SalesAnalyzer
from exporter import ExcelExporter
from logger import setup_logger


def main():

    # Project paths
    project_folder = Path(__file__).resolve().parent.parent
    data_folder = project_folder / "data" / "raw"
    reports_folder = project_folder / "data" / "reports"

    logger = setup_logger(reports_folder)

    try:
        # -----------------------------
        # Load data
        # -----------------------------

        logger.info("Starting retail sales automation.")

        loader = DataLoader(data_folder)
        df = loader.load_all_files()

        logger.info(
            "Data loaded successfully. Rows: %s, Columns: %s",
            df.shape[0],
            df.shape[1]
        )

        # -----------------------------
        # Clean data
        # -----------------------------

        cleaner = DataCleaner(df)
        clean_df = cleaner.clean()

        logger.info(
            "Data cleaned successfully. Rows: %s, Columns: %s",
            clean_df.shape[0],
            clean_df.shape[1]
        )

        # -----------------------------
        # Validate data
        # -----------------------------

        validator = DataValidator(clean_df)
        errors, warnings = validator.validate()

        if errors:
            for error in errors:
                logger.error("Validation error: %s", error)
        else:
            logger.info("Data validation completed with no errors.")

        if warnings:
            for warning in warnings:
                logger.warning("Validation warning: %s", warning)
        else:
            logger.info("No validation warnings found.")

        # -----------------------------
        # Analyze data
        # -----------------------------

        analyzer = SalesAnalyzer(clean_df)

        logger.info("Starting sales analysis.")

        logger.info("Total Sales: %.2f", analyzer.total_sales())
        logger.info("Total Profit: %.2f", analyzer.total_profit())
        logger.info("Total Quantity: %s", analyzer.total_quantity())
        logger.info(
            "Average Order Value: %.2f",
            analyzer.average_order_value()
        )
        logger.info(
            "Profit Margin: %.2f%%",
            analyzer.profit_margin()
        )

        # -----------------------------
        # Export report
        # -----------------------------

        exporter = ExcelExporter(reports_folder)
        output_file = exporter.export_report(analyzer)

        logger.info("Excel report generated: %s", output_file)
        logger.info("Retail sales automation completed successfully.")

    except Exception:
        logger.exception("Retail sales automation failed.")
        raise


if __name__ == "__main__":
    main()