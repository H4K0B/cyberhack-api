
# CyberHack API

A Python client for interacting with the CyberHack API, enabling users to search for domains or emails.

## Features

- **Search Functionality**: Allows users to search for domains or emails using the CyberHack API.
- **Environment Variable Support**: API keys are securely managed through environment variables.
- **Command-Line Interface**: Accepts search queries directly from the command line.

## Installation

### Clone the Repository:

```bash
git clone https://github.com/H4K0B/cyberhack-api.git
cd cyberhack-api
```

### Set Up Environment Variables:

#### On Linux/macOS:

Add the following line to your shell configuration file (e.g., `~/.bashrc` or `~/.zshrc`):

```bash
export CYBERHACK_API_KEY="your_api_key_here"
```

Replace `"your_api_key_here"` with your actual API key. After adding this line, reload your shell configuration by running:

```bash
source ~/.bashrc  # Or ~/.zshrc depending on your shell
```

#### On Windows:

Open Command Prompt and set the environment variable using:

```bash
setx CYBERHACK_API_KEY "your_api_key_here"
```

Replace `"your_api_key_here"` with your actual API key. This command sets the environment variable permanently for your user account.

### Install Dependencies:

Ensure you have Python 3 and `pip` installed. Then, install the required packages:

```bash
pip install -r requirements.txt
```

## Usage

Run the script with your desired search query:

```bash
python3 cyberhack_api.py "search_query"
```

Replace `"search_query"` with the domain or email you wish to search for. For example:

- To search for a domain:

```bash
python3 cyberhack_api.py "example.com"
```

- To search for an email:

```bash
python3 cyberhack_api.py "user@example.com"
```

## Contributing

Feel free to open issues and submit pull requests to improve the script!

## License

This project is licensed under the MIT License - see the LICENSE file for details.
