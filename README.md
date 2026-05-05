# CSV Developer Tool

A simple CLI tool for analyzing and cleaning CSV files.

## Features

- Analyze CSV datasets
- Show missing values
- Display basic statistics
- Clean data (remove rows with missing values)
- Export cleaned CSV

## Installation

```bash
pip install -r requirements.txt
```

## Usage

### Analyze data

```bash
python src/main.py analyze data/sample.csv
```

### Clean data

```bash
python src/main.py clean data/sample.csv --output data/cleaned.csv
```


