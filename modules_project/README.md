# Smart Calc 

A modular Python calculator built with clean architecture, custom exception handling, and environment-based configuration management.

## Features
* **Environment-Based Config**: Uses `python-dotenv` to manage settings via `.env`.
* **Custom Error Handling**: Robust exception handling hierarchy for edge cases (e.g., division by zero).
* **Virtual Environment Isolated**: Pure dependency tracking using `requirements.txt`.

##  Project Structure
```text
smart_calc/
├── smart/
│   ├── __init__.py
├   ├── advanced.py
│   ├── basic.py         # Core arithmetic functions
│   ├── config.py        # Centralized configuration parser
│   └── exceptions.py    # Custom exception classes
├── .env.example         # Template for environment variables
├── .gitignore            # Git exclusion rules
├── README.md
├── main.py              # Application entry point
└── requirements.txt     # Tracked dependencies
