# Simple Python CI Demo

This tiny project demonstrates a beginner-friendly GitHub Actions CI pipeline for a simple Python calculator.

Files added:
- [calculator.py](calculator.py) - simple functions and a sample `__main__` run
- [test_calculator.py](test_calculator.py) - pytest tests
- [requirements.txt](requirements.txt) - project dependencies
- [.github/workflows/ci.yml](.github/workflows/ci.yml) - CI workflow

Added `square(n)` to `calculator.py` and `test_square` to `test_calculator.py` to demonstrate a simple unary function and its test.

Quick local run:
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python calculator.py
pytest -q
```

To push and trigger CI, commit and push to GitHub (instructions in the repo root).
# GiiHub-action-demo