# analyzer

analyzer is a small command-line tool that scans a local Git repository (or any folder) for Python files and generates clear, human-friendly summaries of each function it finds.

## Features

- Recursively finds `.py` files in the given directory (only valid Git repos are scanned by default).
- Extracts top-level and nested function definitions (including async functions).
- Produces descriptive summaries for each function, including purpose, inputs, return value, and notable side effects.
- Optionally customizable via the source to adjust summary verbosity.

## Requirements

- Python 3.8+
- `gitpython` (to validate repository paths)
- `typer`, `rich`, `python-dotenv`
- Access to the Gemini/API key stored in the `GEMINI_API_KEY` environment variable

Install dependencies locally (example):

```bash
python -m pip install -r requirements.txt
```

If you don't have a `requirements.txt`, install the basics directly:

```bash
python -m pip install gitpython typer rich python-dotenv google-generativeai
```

## Configuration

The tool expects a Gemini API key to be available as the `GEMINI_API_KEY` environment variable. You can place it in a `.env` file at the project root or export it in your shell:

```bash
export GEMINI_API_KEY="your_api_key_here"
# On Windows (PowerShell):
$Env:GEMINI_API_KEY = "your_api_key_here"
```

## Usage

Run the analyzer from the repository root or point it to any folder path:

```bash
python analyzer.py /path/to/repo
```

If you omit the path it defaults to the current working directory:

```bash
python analyzer.py
```

Output is printed to the terminal with readable panels for each function summary.

## How it works (high level)

1. Validates the supplied folder is a Git repository.
2. Recursively finds Python files (`*.py`).
3. Parses each file's AST to extract function definitions and source code.
4. Sends the function code to a configured generative model to produce a descriptive summary.
5. Prints summaries using `rich` for readable terminal output.

## Contributing

Contributions, bug reports, and suggestions are welcome. Open an issue or submit a pull request describing the change.

## License

This project is provided as-is. Add your preferred license file if needed.