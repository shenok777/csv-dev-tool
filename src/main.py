import argparse
from analyzer import analyze
from cleaner import clean

def main():
    parser = argparse.ArgumentParser(description = "CSV Developer Tool")

    parser.add_argument(
        "command",
        choices = ["analyze", "clean"],
        help = "Command to execute"
    )

    parser.add_argument(
        "file",
        help = "Path to CSV file"
    )

    parser.add_argument(
        "--output",
        help = "Output file path (for clean command)",
        default = None
    )

    args = parser.parse_args()

    if args.command == "analyze":
        analyze(args.file)

    if args.command == "clean":
        clean(args.file, args.output)

if __name__ == "__main__":
    main()