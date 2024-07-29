@Client.on_message(Filters.command("start"))
async def start_command(client, message):
    print("This is the /start command")

@Client.on_message(Filters.command("help"))
async def help_command(client, message):
    print("This is the /help command")
