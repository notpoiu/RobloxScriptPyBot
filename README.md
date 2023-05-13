# Roblox Script Python Discord Bot

I created this Discord bot as a fun project while I was bored. Feel free to use it for your own purposes!

**Credits would be appreciated but not required.**

## Security Concerns
The code runs every `.py` file inside the `scripts` directory. Why? Because its easier to extract the data from it, but that raises some security concerns.
DO IN ANY CIRCUMSTANCES PUT A `.py` FILE THAT YOU DON'T KNOW WHAT IT DOES INSIDE THE SCRIPTS DIRECTORY.

## Documentation
For detailed documentation on how to use the Roblox Script Python Discord Bot, please refer to the [official documentation](https://upio.gitbook.io/roblox-script-bot-documentation/).

## How to Install
To install and set up the bot, follow these steps:

1. Clone the repository by running the following command in the command line:
   ```
   git clone https://github.com/notpoiu/RobloxScriptPyBot
   ```
2. Navigate to the cloned directory using the command prompt:
   ```
   cd RobloxScriptPyBot
   ```
3. Install the required dependencies by running:
   ```
   pip install -r requirements.txt
   ```

## How to Set up the Bot

To set up the bot and make it work with your Discord server, follow these steps:

1. Go to the [Discord Developer Portal](https://discord.com/developers) and create a new bot.
2. Copy the token for your bot.
3. Open the `config.json` file in the project and locate the `"Token"` value under the `"Bot Info"` section.
4. Replace the existing token value with the token you copied in the previous step.

Next, we need to enable intents for the bot to work properly:

1. Scroll down on the Discord Developer Portal page until you find the "Privileged Gateway Intents" section.
   ![Intents Unchecked](https://github.com/notpoiu/RobloxScriptPyBot/assets/75510171/cd05f4ad-7cb5-4128-add7-9355f2a88467)
2. Enable all the intents by checking the corresponding checkboxes. (You don't need to enable every single one, but it's recommended for the bot's functionality.)
   ![Intents Checked](https://github.com/notpoiu/RobloxScriptPyBot/assets/75510171/856582c0-70f6-4605-9b34-6d1dea8f1f9f)

That's it! You have successfully set up the bot. Now you can run it and start using the Roblox Script Python Discord Bot in your server.
