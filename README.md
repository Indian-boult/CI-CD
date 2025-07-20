# Calculator Project - CI/CD Learning

This is a simple Python calculator project designed to learn and demonstrate CI/CD (Continuous Integration/Continuous Deployment) concepts.

## Project Structure

```
ci-cd/
├── calculator.py      # Main calculator module
├── test_calculator.py # Unit tests
├── main.py           # Application entry point
├── requirements.txt  # Project dependencies
└── README.md        # This file
```

## Features

- Basic arithmetic operations (add, subtract, multiply, divide, power)
- Comprehensive unit tests
- Error handling (division by zero)
- Clean, documented code

## Getting Started

### Prerequisites

- Python 3.7+
- Anaconda (as you mentioned you're using it)

### Installation

1. Clone this repository:
```bash
git clone <your-repo-url>
cd ci-cd
```

2. Create a conda environment:
```bash
conda create -n calculator-ci-cd python=3.9
conda activate calculator-ci-cd
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

### Running the Application

```bash
python main.py
```

### Running Tests

```bash
# Using unittest (built-in)
python -m unittest test_calculator.py

# Using pytest (if installed)
pytest test_calculator.py
```

## CI/CD Concepts We'll Learn

### Continuous Integration (CI)
- **Automated Testing**: Every code change triggers automatic test runs
- **Code Quality Checks**: Linting, formatting, and style checks
- **Build Verification**: Ensuring code compiles and runs correctly
- **Early Bug Detection**: Catching issues before they reach production

### Continuous Deployment (CD)
- **Automated Deployment**: Code changes automatically deploy to staging/production
- **Environment Management**: Consistent environments across development stages
- **Rollback Capability**: Quick rollback to previous versions if issues arise
- **Zero-Downtime Deployments**: Deploying without service interruption

## Next Steps

In the upcoming sections, we'll set up:
1. **GitHub Actions** for CI/CD automation
2. **Code quality checks** (linting, formatting)
3. **Test automation** and coverage reporting
4. **Deployment pipelines** to different environments

## Contributing

This project is designed for learning purposes. Feel free to experiment with different CI/CD configurations and add new features to practice the concepts. 