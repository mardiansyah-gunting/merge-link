# Merge Link

A Python-based utility to generate TREEO Cloud URLs for forestry plots based on their Plot IDs from CSV files.

## Overview

This project provides a script to process CSV data containing forestry plot information. It extracts the `Plot ID` and generates a direct link to the TREEO Cloud platform for each plot, appending these links to a new output CSV file.

## Requirements

- Python 3.x
- `pandas` library

## Setup

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd merge-link
   ```

2. **Set up a virtual environment (recommended):**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install pandas
   ```

## Usage

The main script is `main.py`. Currently, it is configured to process `obel_plots.csv`.

1. Place your input CSV file (e.g., `obel_plots.csv`) in the root directory.
2. Run the script:
   ```bash
   python main.py
   ```
3. The script will generate a new file named `obel_treeo_plot_urls.csv` containing the original data plus a `Generated URL` column.

## Scripts

- `main.py`: The entry point script that performs CSV processing and URL generation.

## Project Structure

```text
merge-link/
├── .venv/                      # Python virtual environment
├── delight_plots.csv           # Input data for Delight plots
├── delight_treeo_plot_urls.csv # Generated output for Delight plots
├── main.py                     # Main execution script
├── obel_plots.csv              # Input data for Obel plots
├── obel_treeo_plot_urls.csv    # Generated output for Obel plots
└── README.md                   # Project documentation
```

## Environment Variables

No environment variables are currently required.

## Tests

No automated tests are currently implemented.
- [TODO] Add unit tests for URL generation logic.

## TODOs

- [ ] Parameterize `main.py` to accept input/output filenames as arguments.
- [ ] Add support for processing multiple files in a batch.
- [ ] Implement error handling for missing 'Plot ID' columns.
- [ ] Add a `requirements.txt` file for easier dependency management.

## License

[TODO: Add License Information]
