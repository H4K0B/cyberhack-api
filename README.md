# cyberhack-api
API for CyberHack
A Python client for interacting with the CyberHack API, enabling users to search for domains or emails.

## Features

- **Search Functionality:** Allows users to search for domains or emails using the CyberHack API.
- **Environment Variable Support:** API keys are securely managed through environment variables.
- **Command-Line Interface:** Accepts search queries directly from the command line.

## Installation

**Clone the Repository:**

   ```bash
   git clone https://github.com/H4K0B/cyberhack-api.git
   cd cyberhack-api
Set Up Environment Variables:

On Linux/macOS:

Add the following line to your shell configuration file (e.g., ~/.bashrc or ~/.zshrc):

export CYBERHACK_API_KEY="your_api_key_here"

Replace "your_api_key_here" with your actual API key. After adding this line, reload your shell configuration by running:

On Windows:

Open Command Prompt and set the environment variable using:

setx CYBERHACK_API_KEY "your_api_key_here"

Replace "your_api_key_here" with your actual API key. This command sets the environment variable permanently for your user account.

Install Dependencies:

Ensure you have Python 3 and pip installed. Then, install the required packages:

```bash
pip install -r requirements.txt
