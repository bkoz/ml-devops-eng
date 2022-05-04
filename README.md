# ML DevOps Engineering 
## Coursework

### Course 1. - Writing Clean Code

#### Directory Structure

```
01-clean-code
├── project_churn
├── ex01_refactor_wine_quality.ipynb
├── ex02_refactor_wine_quality_solution.ipynb
├── ex03_optimizing_code_common_books.ipynb
├── ex04_optimizing_code_holiday_gifts.ipynb
├── ex05_pep8_lint.py
├── ex06_read_csv.py
├── ex07_testing_logging.py
└── testing
    ├── conftest.py
    ├── test_caching.py
    ├── test_mylibrary.py
    └── test_mylibrary_copy.py
```

#### Check your code for cleanliness.
```
pylint <source-file>
```

Source files can not begin with a number.

#### After acheiving a high score with `pylint` run `autopep8` to format.
```
autopep8 --in-place --aggressive --aggressive <source-file>.py
```