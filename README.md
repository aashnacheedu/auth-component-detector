# Authentication Component Detector

## Overview

This application detects authentication components (login forms, password inputs) in websites. It includes:

- FastAPI backend for scraping and analysis
- Lightweight server-rendered UI for interactive URL input
- Command-line interface (CLI) for developer-friendly usage

The solution demonstrates:

- HTML scraping and parsing
- Dynamic input handling
- Structured output
- Clean, modular architecture

---

## Features

### 1. Dynamic URL input

- Analyze any website via the UI or CLI
- Preset example sites included for convenience:
  - TLDR Newsletter (`https://tldr.tech/`)
  - WordPress (`https://wordpress.com/log-in`)
  - IXL Learning (`https://www.ixl.com/`)
  - Taylor Swift (`https://www.taylorswift.com/`)
  - GitHub (`https://github.com/login`)

### 2. Authentication detection

- Searches for `<input type="password">` elements
- Returns enclosing `<form>` if present
- Structured JSON output includes:
  - `authentication_found` (boolean)
  - `components` (HTML snippets)
  - `methods` (heuristic detection methods, e.g., `password_input`)
  - `confidence` (heuristic, optional)

### 3. Multiple access methods

- **Web UI**: accessible at `/` via FastAPI
- **API endpoint**: `GET /analyze?url=<URL>` returns JSON
- **CLI**: `python cli.py <URL>` prints JSON result

---

## Installation

Requires Python 3.9+.

### 1. Clone the repository

```bash
git clone https://github.com/aashnacheedu/auth-component-detector.git
cd auth-component-detector
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv

# Linux/macOS
source venv/bin/activate

# Windows
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Application

### 1. Web UI

Start the FastAPI server:

```bash
uvicorn api:app --reload
```

Open your browser at: **http://127.0.0.1:8000**

- Use the preset buttons or enter a custom URL
- Results show authentication detection and HTML snippets

### 2. API Endpoint

Send a GET request to `/analyze`:

```bash
GET /analyze?url=https://github.com/login
```

Example response:

```json
{
  "url": "https://github.com/login",
  "authentication_found": true,
  "methods": ["password_input"],
  "components": ["<form>...</form>"],
  "confidence": 0.9
}
```

### 3. Command-Line Interface (CLI)

Run:

```bash
python cli.py https://github.com/login
```

Example output:

```json
{
  "url": "https://github.com/login",
  "authentication_found": true,
  "methods": ["password_input"],
  "components": ["<form>...</form>"],
  "confidence": 0.9
}
```
