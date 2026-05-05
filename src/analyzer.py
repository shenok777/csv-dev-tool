from file_utils import load_csv


def show_overview(df):
    """
    Shows basic information about the dataset.
    """

    print("\nDataset overview")
    print("----------------")
    print(f"Rows: {df.shape[0]}")
    print(f"Columns: {df.shape[1]}")

    print("\nColumn names:")
    for column in df.columns:
        print(f"- {column}")


def show_missing_values(df):
    """
    Shows the number of missing values in each column.
    """

    print("\nMissing values")
    print("--------------")

    missing_values = df.isnull().sum()

    for column, count in missing_values.items():
        print(f"{column}: {count}")


def show_numeric_statistics(df):
    """
    Shows statistics for numeric columns.
    """

    print("\nNumeric statistics")
    print("------------------")

    numeric_columns = df.select_dtypes(include="number")

    if numeric_columns.empty:
        print("No numeric columns found.")
        return

    print(numeric_columns.describe())


def analyze(file_path):
    """
    Loads a CSV file and runs all analysis functions.
    """

    df = load_csv(file_path)

    if df is None:
        return

    show_overview(df)
    show_missing_values(df)
    show_numeric_statistics(df)