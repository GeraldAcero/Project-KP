# Project KP - PLDT Modem Network Control Script

Project KP is a Python script designed to provide a command-line interface for managing parental control and firewall settings on a PLDT modem, targeting your internet provider's network. It utilizes Selenium automation with the Microsoft Edge browser to interact with the web interface of the PLDT modem.

## Features

- Activate and deactivate parental controls.
- Adjust firewall settings.
- Simple command-line interface for user interaction.
- Designed for educational purposes.

## Prerequisites

Before using Project KP with your PLDT modem, ensure you have the following prerequisites installed on your system:

- Python 3.x
- Microsoft Edge browser
- Selenium Python library (`pip install selenium`)

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/GeraldAcero/project-kp.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd project-kp
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Download Microsoft Edge WebDriver:**

    Download the appropriate version of the Microsoft Edge WebDriver from [here](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/) and place it in the project directory.

## Usage

1. **Run the script:**

    ```bash
    main.py
    ```

2. **Follow on-screen instructions:**

    Choose an option from the displayed menu by entering the corresponding number. Options include activating parental controls, deactivating parental controls, and exiting the program.

## Disclaimer

- Project KP is provided as-is without any warranty. Use it at your own risk.
- Ensure that you have the necessary permissions to access and modify the settings of your PLDT modem.
- Project KP is intended for educational purposes and should be used responsibly.

## Contributing

Contributions are welcome! Feel free to submit pull requests or open issues for any improvements or bug fixes.

