# CyberLab PRO

## Overview

**CyberLab PRO** is a powerful, lightweight, single-file Command-Line Interface (CLI) toolkit designed for cybersecurity professionals, ethical hackers, and network administrators. Developed entirely with Python's Standard Library, it requires **zero external dependencies** to run. It features **170 active modules** divided into 12 operational categories, ranging from Reconnaissance and OSINT to Cryptography and Visual Test Simulations, all wrapped in a responsive, modern terminal UI that adapts to your screen size.

## Preview

## Key Features

* **170 Operational Modules:** Covers Recon, Web Auditing, Offensive Testing, Blue Team, Cloud, Crypto, System Utils, Wireless, IoT, Forensics, OSINT, and Test Simulations.

* **Zero External Dependencies:** Runs completely out-of-the-box on native Python 3. No `pip install` required for the core suite.

* **Responsive Terminal UI:** Automatically detects terminal dimensions. Centers the layout perfectly on large screens and adapts to a clean left-aligned format on smaller windows.

* **Smart Prompt System:** The CLI knows which modules require input (like a target IP, email, or file path) and which ones run automatically, preventing unnecessary prompts.

* **OSINT Capabilities:** Built-in tools for email reputation checks, phone number geolocation, and username footprinting across social networks.

* **Legal Gatekeeper:** A mandatory authorization prompt at startup to ensure ethical usage and compliance.

## Tech Stack

### Core

* **Python 3.8+:** Built entirely using the Python Standard Library (`socket`, `ssl`, `urllib`, `hashlib`, `sqlite3`, `subprocess`, etc.).

* **ANSI Escape Codes:** Used for advanced terminal styling, colors, and responsive layout management.

### Optional Dependencies

While the core works natively, some advanced OSINT and Crypto modules benefit from:

* `phonenumbers` (for Phone OSINT)

* `cryptography` (for advanced AES/RSA operations)

* `holehe` (for Email to Accounts lookup)

## Project Architecture

```
cyberlab/
├── main.py           # The complete single-file application
├── tools1.png        # UI Preview image
├── README.md         # Project documentation
└── .gitignore        # Git ignore file

```

## Quick Start

### Prerequisites

* A terminal or command prompt.

* **Python 3.8** or higher installed.

### Installation & Run

1. **Clone the repository:**

   ```
   git clone https://github.com/nowii-core/cyberlab.git
   
   ```

2. **Navigate into the folder and launch the toolkit:**

   ```
   cd cyberlab && python3 main.py
   
   ```

3. **(Optional) Unlock Advanced Features:**
   If you want to unlock the 3 advanced Crypto/OSINT modules, you can install the optional dependencies:

   ```
   pip3 install phonenumbers cryptography holehe
   
   ```

## Usage

Once launched, you will be greeted by the legal disclaimer. Type `si` (or `yes`) to proceed.

* Use the main menu to navigate categories by typing the corresponding number (e.g., `1` for Reconnaissance).

* Type `list` to see a paginated, 2-column index of all 170 modules.

* Type `0` to safely exit the session.

```
  [+] SELEZIONA CATEGORIA:
      [1]  Reconnaissance & OSINT       (001 - 015)
      [2]  Web Application Auditing    (016 - 030)
      ...
      [12] Visual Test Simulations     (161 - 170)

```

##  Disclaimer

This tool is strictly for educational and authorized testing purposes only.

Using CyberLab PRO to scan, attack, or gather intelligence on targets without explicit, written consent from the owner is **illegal** and strictly prohibited. The developer (`nowii-core`) assumes no liability for any misuse or damage caused by this program.

By using this tool, you agree to take full responsibility for your actions (*Art. 615-ter c.p. - Accesso abusivo a un sistema informatico*).

## License

This project is distributed under the **MIT** license. See the [`LICENSE`](./LICENSE) file for more information.

## Contact & Support

* **Maintainer:** [@nowii-core](https://github.com/nowii-core)

* **Bug Reports & Feature Requests:** Open an [Issue](https://github.com/nowii-core/cyberlab/issues) or submit a [Pull Request](https://github.com/nowii-core/cyberlab/pulls).

<div align="center"> <sub>Developed by <b>nowii-core</b></sub> </div>
