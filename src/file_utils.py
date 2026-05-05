import pandas as pd


def load_csv(file_path):
    """
    Loads a CSV file and returns a pandas DataFrame.
    """

    try:
        df = pd.read_csv(file_path)
        return df

    except FileNotFoundError:
        print(f"Error: file not found: {file_path}")
        return None

    except pd.errors.EmptyDataError:
        print(f"Error: file is empty: {file_path}")
        return None

    except pd.errors.ParserError:
        print(f"Error: could not parse CSV file: {file_path}")
        return None