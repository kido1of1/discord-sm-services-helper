import discord
import random
import string
from discord.ext import commands


TOKEN = ''
PAYPAL_LINK = 'https://www.paypal.me/urpaypal'
ADMIN_CHAT_ID = 1515221512512525115  # Replace with your admin channel ID

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.reactions = True
intents.message_content = True  # For accessing the content of the message
intents.dm_messages = True

bot = commands.Bot(command_prefix="!", intents=intents)

# List of services (you can expand this later)
services = {
    "1K TikTok Followers": 5.00,
}

# Generate a random string for PayPal notes
def generate_random_string(length=8):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# Command to open a ticket
@bot.command()
async def ticket(ctx):
    # Create a private text channel for the user
    overwrites = {
        ctx.guild.default_role: discord.PermissionOverwrite(read_messages=False),
        ctx.author: discord.PermissionOverwrite(read_messages=True)
    }

    # Create ticket channel
    ticket_channel = await ctx.guild.create_text_channel(f'ticket-{ctx.author.name}', overwrites=overwrites)
    
    await ticket_channel.send(f"Hello {ctx.author.mention}, what service would you like to purchase?")
    
    # List services to choose from
    service_message = "Available services:\n"
    for idx, (service_name, price) in enumerate(services.items(), 1):
        service_message += f"{idx}. {service_name} - ${price}\n"
    
    service_message += "\nPlease type the number of the service you'd like to buy."

    await ticket_channel.send(service_message)

    def check(m):
        return m.author == ctx.author and m.channel == ticket_channel

    try:
        # Wait for the user's response
        service_choice = await bot.wait_for('message', check=check, timeout=60.0)
        choice = int(service_choice.content)  # Convert choice to an integer
        if choice < 1 or choice > len(services):
            await ticket_channel.send("Invalid choice. Please try again.")
            return

        selected_service = list(services.items())[choice - 1]
        service_name, price = selected_service

        # Generate the PayPal instructions
        random_string = generate_random_string()
        payment_message = (
            f"You have chosen **{service_name}** for **${price}**.\n"
            f"Please send the payment to our PayPal link: {PAYPAL_LINK}\n"
            f"Add the following string as a note in your payment: **{random_string}**\n"
            f"Once payment is made, please upload a screenshot of the transaction here."
        )

        await ticket_channel.send(payment_message)

        # Wait for the screenshot of the payment
        def image_check(m):
            return m.author == ctx.author and m.channel == ticket_channel and len(m.attachments) > 0

        payment_screenshot = await bot.wait_for('message', check=image_check, timeout=300.0)

        # Confirm the order has started and notify admin
        await ticket_channel.send(f"Thank you! Your order for **{service_name}** has been started.")
        admin_channel = bot.get_channel(ADMIN_CHAT_ID)
        await admin_channel.send(
            f"{ctx.author.mention} has made a payment for **{service_name}**. Please verify the order. "
            f"Screenshot: {payment_screenshot.attachments[0].url}"
        )
        await admin_channel.send(f"@admin Order started for {ctx.author.mention}.")

    except (ValueError, TimeoutError):
        await ticket_channel.send("You did not respond in time or provided an invalid response. Closing the ticket.")
        await ticket_channel.delete()

# Event listener for when the bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

bot.run(TOKEN)
