from file_utils import load_csv


def clean(file_path, output_path = None):
    """
    Cleans CSV data by removing rows with missing values.
    """

    df = load_csv(file_path)

    if df is None:
        return
    print("\nCleaning data...")
    print("------------------")

    cleaned_df = df.dropna()

    print(f"Original rows: {len(df)}")
    print(f"Cleaned rows: {len(cleaned_df)}")

    if output_path:
        cleaned_df.to_csv(output_path, index = False)
        print(f"\nCleaned file saved to: {output_path}")
    else:
        print(f"\nNo output file specified. Data not saved.")
