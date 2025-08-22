# Project: Template-based Config Generator

## Overview
This project provides a simple Python script to generate configuration files from Jinja2 templates.  
It creates directory structures based on a given prefix and renders template files using a provided principal value.

The script is especially useful for generating `ClientConfig` and `topology.yml` files in a structured and repeatable way.

## Features
- Validates a given prefix string format (e.g. `com.example.project`).
- Creates nested directories according to the prefix.
- Renders configuration files from **Jinja2 templates** stored in the `templates/` directory.
- Prevents overwriting existing files by checking before creation.

## Requirements
- Python 3.8+
- [Jinja2](https://palletsprojects.com/p/jinja/)

Install dependencies via:
```bash
pip install -r requirements.txt
```

*(Create a `requirements.txt` with at least `jinja2` if not already present.)*

## Usage
Run the script with the following arguments:

```bash
python main.py <PREFIX> <PRINCIPAL>
```

### Arguments
- **PREFIX**: Dot-separated identifier that defines the folder structure (e.g. `com.example.app` → `com/example/app/`).
- **PRINCIPAL**: A string value that will be passed into the templates (e.g. `admin@example.com`).

### Example
```bash
python main.py com.example.app admin@example.com
```

This will:
1. Create the directory `com/example/app/`.
2. Render files from the templates:
   - `ClientConfig`
   - `topology.yml`
3. Store them in the newly created directory.

## Templates
All templates should be placed in a folder named `templates/` in the project root.  
For example:
```
templates/
 ├── ClientConfig
 └── topology.yml
```

Templates can reference:
- `prefix` – the provided `PREFIX` argument
- `principal` – the provided `PRINCIPAL` argument

## License
MIT License – feel free to use and adapt.
