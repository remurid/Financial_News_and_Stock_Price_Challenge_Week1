# Financial_News_and_Stock_Price_Challenge_Week1

This project is organized for modular, testable, and reproducible financial news analysis.

## Project Structure

```
.vscode/           # VSCode settings
.github/           # GitHub Actions workflows
src/               # Source code (modular functions)
notebooks/         # Jupyter notebooks for EDA and analysis
scripts/           # Utility scripts
requirements.txt   # Python dependencies
README.md          # Project overview
```

## Setup Instructions

1. **Clone the repository and create a virtual environment:**
   ```powershell
   git clone <your-repo-url>
   cd Financial_News_and_Stock_Price_Challenge_Week1
   python -m venv .week1_env
   .week1_env\Scripts\Activate.ps1
   pip install -r requirements.txt
   ```

2. **Run EDA Notebook:**
   - Open `notebooks/eda_modular.ipynb` in VSCode or Jupyter.
   - The notebook uses modular functions from `src/eda.py` for analysis.

3. **Testing:**
   - Add tests in the `tests/` folder.
   - Run tests with:
     ```powershell
     pytest tests
     ```

4. **CI/CD:**
   - GitHub Actions will run tests on every push or pull request.

## Modularity
- All EDA and analysis logic is in `src/eda.py` as reusable functions.
- Notebooks and scripts import from `src` for maintainability.

## Data
- Place your data files in the `data/` directory.

---

For more details, see the documentation in each subfolder.