from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
import cohere
import asyncio
import sys
import nest_asyncio

# Set up your Cohere API key
cohere_client = cohere.Client('GQI8PTe9h9Ii22MbiVXcht0szYcJC8WQSCfCxJwg')  # Replace with your actual API key

# Set up your Telegram Bot Token
TELEGRAM_TOKEN = '8063629260:AAGIt5Y6LfE3yMhCwNSmE8dhd8cxV-cQlF4'  # Replace with your actual Telegram bot token

# Function to handle '/start' command
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("Hello! prends answer venuma pookies send the question,0 I'll help you solve them.")

# Function to process and respond to coding problems
async def solve_coding_problem(update: Update, context: CallbackContext):
    user_input = update.message.text  # Get the user's message
    
    try:
        # Generate the response from Cohere API
        response = cohere_client.generate(
        model='command-xlarge-nightly',  # Replace with a valid model name
        prompt=f"Provide a Python solution for:\n{user_input}",
        max_tokens=150,
        temperature=0.7
)


        # Get the solution text from the response
        solution = response.generations[0].text.strip()
        await update.message.reply_text(f"Here’s a solution:\n\n{solution}")
    
    except Exception as e:
        await update.message.reply_text("Sorry, I couldn't process your request. Please try again later.")
        print(f"Exception: {e}", file=sys.stderr)

# Main function to set up the bot
async def main():
    app = Application.builder().token(TELEGRAM_TOKEN).build()

    # Add handlers for commands and messages
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, solve_coding_problem))

    # Run the bot
    print("Bot is running...")
    await app.run_polling()
if __name__ == "__main__":
    import sys
    if sys.version_info >= (3, 7):
        # If running in an environment where the event loop is already running (like Jupyter Notebook),
        # use `await main()` directly instead of asyncio.run(main()).
        import nest_asyncio
        nest_asyncio.apply()

    import asyncio
    asyncio.get_event_loop().run_until_complete(main())
