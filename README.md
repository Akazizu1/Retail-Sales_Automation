# Retail Sales Automation

## Overview

Retail Sales Automation is a Python-based data analysis and reporting project built using the Global Superstore dataset. It automates repetitive steps involved in processing sales data, from loading and cleaning raw files to validating data, analyzing business performance, and generating a formatted Excel report.

The project was also an opportunity to practice Python project structure, Git and GitHub, virtual environments, dependency management, and automated testing.

## Features

1. **Data loading:** Loads and combines supported CSV and Excel files from the raw data folder.
2. **Data cleaning:** Standardizes column names, trims text values, converts dates, and handles numeric data types.
3. **Data validation:** Checks required columns, missing values, duplicate records, and potential data quality issues.
4. **Sales analysis:** Calculates key performance indicators and analyzes sales and profit by category, region, segment, year, discount band, and shipping mode.
5. **Product analysis:** Identifies top performing and least profitable products and analyzes customer performance.
6. **Excel reporting:** Generates a formatted workbook with a dashboard, summary metrics, analysis sheets, and charts.
7. **Logging and error handling:** Records execution progress and errors in a log file.
8. **Automated testing:** Uses pytest to test cleaning, validation, and sales analysis calculations.

## Technologies Used

Python, Pandas, OpenPyXL, pytest, Git, and GitHub.

## Project Structure

```text
Retail-Sales_Automation/
├── data/
│   ├── raw/
│   ├── processed/
│   └── reports/
├── src/
│   ├── loader.py
│   ├── cleaner.py
│   ├── validator.py
│   ├── analyzer.py
│   ├── exporter.py
│   ├── logger.py
│   └── main.py
├── tests/
│   ├── test_cleaner.py
│   ├── test_validator.py
│   └── test_analyzer.py
├── .gitignore
├── requirements.txt
└── README.md
```

## Dataset

The project uses the Global Superstore dataset from Kaggle.

Dataset source: https://www.kaggle.com/datasets/fatihilhan/global-superstore-dataset

The raw dataset is not included in the repository. Download the dataset, place the CSV file in `data/raw/`, and ensure the filename and format are supported by the loader.

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/Akazizu1/Retail-Sales_Automation.git
cd Retail-Sales_Automation
```

### 2. Create and activate a virtual environment

On Windows:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add the dataset

Place the downloaded CSV file in `data/raw/`.

### 5. Run the automation

From the project root:

```bash
python src/main.py
```

### 6. Run automated tests

```bash
python -m pytest tests/ -v
```

## Sample Results

The following results were obtained from the dataset during a successful execution.

| Metric | Result |
|---|---:|
| Records processed | 51,290 |
| Total sales | 12,642,905.00 |
| Total profit | 1,467,457.29 |
| Total quantity | 178,312 |
| Average order value | 505.01 |
| Profit margin | 11.61% |

The analysis also showed that annual sales increased from approximately 2.26 million in 2011 to 4.30 million in 2014. Higher discount bands were associated with negative aggregate profit in this dataset.

## Output Files

The automation generates the following files in `data/reports/`:

1. `sales_report.xlsx`: An Excel workbook containing dashboard metrics, charts, and detailed analysis sheets.
2. `automation.log`: A log of execution progress and any errors encountered.

Generated reports and raw data are excluded from version control through `.gitignore`.

## Testing

The project includes 14 automated tests covering data cleaning, data validation, and core sales analysis calculations. All 14 tests passed during the latest test run.

## What I Learned

Through this project, I gained practical experience with:

1. Structuring a Python project into reusable modules.
2. Using Pandas to clean, validate, and analyze data.
3. Generating formatted Excel reports with charts.
4. Managing a Python virtual environment and recording dependencies in `requirements.txt` using `pip freeze`.
5. Using Git and GitHub to track project changes.
6. Writing automated tests with pytest.
7. Implementing logging and error handling in a data processing workflow.

## Future Improvements

Potential improvements include adding more robust input handling, expanding test coverage, and supporting additional report formats.
