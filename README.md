# learning-python-for-mlops
A hands-on Python learning roadmap for MLOps, featuring modular projects, production-ready architecture, API integration, and clean code best practices.
everything i learn i do about it a project to solidify my knowledge 

A structured, hands-on roadmap designed to master Python concepts for **MLOps (Machine Learning Operations)**—covering production-ready project architecture, API deployment, configuration management, and clean code best practices.

## Projects Directory

| Project | Description | Key Topics | Status |
| :--- | :--- | :--- | :--- |
| **[Project 01: Smart Calc](./project-01-smart-calc)** | Production-ready modular calculator | `python-dotenv`, `venv`, Custom Exceptions, Clean Architecture |
---

##  Repository Architecture

This repository uses a **Monorepo structure**. Each project inside is completely self-contained with its own code, dependencies (`requirements.txt`), and documentation (`README.md`):

```text
learning-python-for-mlops/
├── .gitignore                      # Global git ignore rules
├── README.md                       # Roadmap overview (this file)
│
├── project-01-smart-calc/          # Project 01: Modular Calculator
│   ├── smart/                      # Core python package
│   ├── main.py                     # Entry point
│   ├── requirements.txt            # Local dependencies
│   └── README.md                   # Project-specific documentation
