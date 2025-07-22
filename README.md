
---

## Installation

### From Source

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/simple-ci-cd-calculator.git
   cd simple-ci-cd-calculator
   ```

2. Install with test and lint dependencies:
   ```sh
   pip install ".[test, lint]"
   ```

### From TestPyPI (for published releases)

1. Install from TestPyPI:
   ```sh
   pip install --index-url https://test.pypi.org/simple/ simple-ci-cd-calculator
   ```

---

## Usage

```python
from calculator import add, subtract, multiply, divide

print(add(2, 3))        # 5
print(subtract(5, 2))   # 3
print(multiply(3, 4))   # 12
print(divide(10, 2))    # 5.0
```

---

## Running Tests

```sh
pytest
```

---

## Linting

```sh
flake8 src/
```

---

## Continuous Integration / Continuous Deployment

- **Linting and tests** run automatically on every push and pull request to `main`.
- **Coverage reports** are posted as comments on pull requests.
- **Publishing** to [TestPyPI](https://test.pypi.org/) happens automatically when you push a tag like `v1.2.3` to the repository.

### To publish a new release:

1. Bump the version in `pyproject.toml`.
2. Commit and push your changes.
3. Create and push a new tag:
   ```sh
   git tag v1.2.3
   git push origin v1.2.3
   ```

---

## License

MIT License

---

## Security

- API tokens and secrets are stored securely in GitHub Actions secrets.
- Publishing uses trusted PyPI publishing with OpenID Connect.

---

## Author

- [Indian Boult](https://github.com/Indian-boult/CI-CD)
