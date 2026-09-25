from pathlib import Path

from loader import DataLoader
from cleaner import DataCleaner
from validator import DataValidator
from analyzer import SalesAnalyzer
from exporter import ExcelExporter

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

    
    analyzer = SalesAnalyzer(clean_df)
   
    print("\n## DATA ANALYSIS RESULTS")
    print(f"Total Sales: {analyzer.total_sales()}")
    print(f"Total Profit: {analyzer.total_profit()}")
    print(f"Total Quantity: {analyzer.total_quantity()}")
    print(f"Average Order Value: {analyzer.average_order_value()}")
    print(f"Profit Margin: {analyzer.profit_margin():.2f}%")

    """Export Report"""
    exporter = ExcelExporter("data/reports")
    exporter.export_report(analyzer)
    
    print("\nSales by Year:")
    print(analyzer.sales_by_year())
    print("\nProfit by Year:")
    print(analyzer.profit_by_year())
    print("\nTop Products by Profit:")
    print(analyzer.top_products_by_profit())
    print("\nBottom Products by Profit:")
    print(analyzer.bottom_products_by_profit())
    print("\nProfit by Discount:")
    print(analyzer.profit_by_discount())
    print("\nPerformance by Ship Mode:")
    print(analyzer.performance_by_ship_mode())
    print("\nSales Growth by Year:")
    print(analyzer.sales_growth_by_year())
    print("\nProfit by Discount Band:")
    print(analyzer.profit_by_discount())
if __name__ == "__main__":
    main()
