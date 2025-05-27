# Instagram Comment Bot

## Description
This bot automates the process of tagging a list of friends in the comments section of a specific Instagram post. It reads usernames from a local file and uses Selenium to interact with the Instagram website.

## Features
*   **Customizable Usernames:** Easily manage the list of users to tag via the `usernames.txt` file.
*   **Configurable Behavior:** Control settings like comment delay, target post URL, and the number of users per comment through the `config.ini` file.
*   **Selenium-Powered:** Uses Selenium WebDriver for more robust and reliable browser automation compared to UI-level automation tools.
*   **Flexible Tagging:** Specify how many users you want to tag in each individual comment.

## Prerequisites
*   **Python 3.x:** Ensure you have Python 3 installed. You can download it from [python.org](https://www.python.org/downloads/).
*   **Google Chrome:** The bot is designed to work with Google Chrome.
*   **ChromeDriver:** You need the ChromeDriver that matches your installed Google Chrome version.
    *   Download from the official site: [https://chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads)
    *   **Important:** The version of ChromeDriver *must* match your Chrome browser version. Check your Chrome version by going to `chrome://settings/help`.

## Setup Instructions

1.  **Clone the Repository:**
    ```bash
    git clone <your_repository_url_here> 
    # Replace <your_repository_url_here> with the actual URL of this repository.
    cd <repository_directory_name>
    ```

2.  **Install Selenium:**
    Open your terminal or command prompt and run:
    ```bash
    pip install selenium
    ```

3.  **Set up ChromeDriver:**
    *   Download the ChromeDriver executable that matches your Google Chrome version (see Prerequisites).
    *   Place the `chromedriver.exe` (for Windows) or `chromedriver` (for Linux/macOS) executable in the **same directory as the bot scripts** (`bot.py`, `comentarios_nombres.py`, etc.). This is the simplest method. Alternatively, you can place it in a directory included in your system's PATH.

4.  **Create `usernames.txt`:**
    *   Create a file named `usernames.txt` in the same directory as the bot scripts.
    *   Add one Instagram username per line. These are the users the bot will tag.
    *   **Example `usernames.txt`:**
        ```
        friend1_username
        another_friend
        user_xyz
        insta_user_123
        ```

5.  **Configure `config.ini`:**
    *   Create a file named `config.ini` in the same directory as the bot scripts. This file controls the bot's settings.
    *   **Settings:**
        *   `post_url`: The full URL of the Instagram post where you want to add comments.
            *   Example: `https://www.instagram.com/p/CxyzEXAMPLEpostID/`
        *   `comment_delay`: The time in seconds the bot will wait after posting each comment before posting the next one. This helps avoid account issues.
            *   Example: `35`
        *   `users_per_comment`: The number of users to tag in each individual comment.
            *   Example: `2` (tags two users per comment)
        *   `custom_messages`: A comma-separated list of custom messages or emojis to append after the tagged usernames.
            *   Example: `custom_messages = Good luck everyone!, Hoping to win! 🚀, So excited!`
            *   Behavior: If provided, one message is chosen randomly and appended to the comment. If left empty or the setting is omitted, no custom message is added.
    *   **Example `config.ini`:**
        ```ini
        [General]
        post_url = https://www.instagram.com/p/your_post_id_here/
        comment_delay = 35
        users_per_comment = 2
        custom_messages = Vamos por ese premio!, 🔥🔥🔥, Con todo! 🎉
        ```
        *Replace `https://www.instagram.com/p/your_post_id_here/` with the actual post URL.*

## Running the Bot

1.  **Log in to Instagram:** Before running the bot, open Google Chrome, navigate to [Instagram](https://www.instagram.com), and log in to your account. This step is crucial.
2.  **Handle Cookie Pop-ups:** When the bot first opens the Instagram post URL, you might need to manually click "Accept" or "Allow" on any cookie consent pop-ups if they appear. The bot will wait for you to do this.
3.  **Execute the Script:**
    Open your terminal or command prompt in the repository directory and run:
    ```bash
    python bot.py
    ```

    The bot will then:
    *   Print startup and configuration messages.
    *   Open the specified Instagram post.
    *   Start posting comments, tagging users from `usernames.txt` according to your `config.ini` settings.
    *   Print progress for each comment.

## Important Notes & Disclaimer

*   **Terms of Service:** Using bots on Instagram may violate their Terms of Service. This tool is provided for educational purposes. Use it responsibly and at your own risk. The developers are not responsible for any account restrictions or bans.
*   **Instagram UI Changes:** The bot's ability to find the comment box and post comments depends on Instagram's current website structure. If Instagram updates its website, the bot (especially the Selenium selectors in `bot.py`) might need to be updated to function correctly.
*   **Error Handling:** The bot includes basic error handling, especially for finding the comment box. If you encounter issues, check the console output for error messages.

---
This README provides a comprehensive guide for setting up and running the Instagram Comment Bot.
```
