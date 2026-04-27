# Amazon Playwright Tests

Automated test suite for Amazon user journeys using **Playwright** and **pytest**.  
This project demonstrates clean automation patterns, reusable fixtures, and CI/CD integration with GitHub Actions.

Automated test suite for Amazon user journeys using Playwright + pytest.  
Includes fixtures, reusable page objects, and CI/CD with GitHub Actions.  
Run tests with `pytest packages/demoqa/amazon/tests --html=report.html --self-contained-html`.

---

## 📂 Project Structure
packages/
└── demoqa/
    └── amazon/
        ├── src/  
            ├── pages/      # Page Objects and helper classes
            ├── fixtures/   # Pytest fixtures
            ├── flows/      # User Flow
        ├── tests/       # Test cases
        └── pytest.ini   # Pytest configuration
README.md
.gitignore
.github/workflows/ci.yml   # GitHub Actions workflow

