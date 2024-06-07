# Simple Discord Bot

This is a simple example of a Discord bot implemented in Python using `dotenv-python` for managing sensitive keys, `py-cord` for interacting with the Discord API, and `cogwatch` for dynamic cog reloading. 

This repo can be forked and modified to include unlimited capabilities and features; from complex view-flows, modals, MySQL, anything!

## Features

- Loads Discord token and other sensitive keys from a `.env` file.
- Loads less sensitive configuration from `bot_config.json`
- Implements a single slash command example, `/ping`
- Utilizes `cogwatch` for hot-reloading modules in the `cogs` sub-directory.

## Requirements

- Python 3.8+
- `dotenv-python`
- `py-cord` (https://docs.pycord.dev/en/stable/api/index.html)
- `cogwatch` (https://github.com/robertwayne/cogwatch)

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/cozmycc/PythonDiscordBot.git
    cd PythonDiscordBot
    ```

2. **Create and activate a virtual environment:**

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Set up your `.env` file:**

    Create a file named `.env` in the root directory of your project, if it doesn't already exist, and add the following:

    ```env
    DISCORD_TOKEN=your_discord_token_here
    ```

## Usage

1. **Run the bot:**

    ```sh
    python bot.py
    ```

2. **Interact with the bot:**

    Use the slash command `/ping` in your Discord server where the bot is present to verify it is working.

## Example Configuration

### bot_config.json

```json
{
  "main": {
    "version": "1.0.0"
  }
}
