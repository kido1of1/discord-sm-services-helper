<h1>Discord Service Bot</h1>
<p>A simple <strong>Discord bot</strong> built using Python and the <a href="https://discordpy.readthedocs.io/">discord.py</a> library to facilitate service-based transactions. This bot allows users to open tickets for purchasing services, provides them with PayPal payment instructions, and helps admins manage the process.</p>

<h2>Features</h2>
<ul>
    <li>Users can open a private ticket channel to inquire about services.</li>
    <li>Bot lists available services and prices for easy selection.</li>
    <li>Generates a unique payment note for users to add to their PayPal transaction.</li>
    <li>Automatically waits for users to upload a screenshot of their payment.</li>
    <li>Notifies admins in a specified channel with payment confirmation details and attached screenshots.</li>
    <li>Closes the ticket automatically if the user fails to respond in time or provides invalid input.</li>
</ul>

<h2>Setup</h2>
<ol>
    <li>Clone the repository.</li>
    <li>Install the required libraries using <code>pip install discord.py</code>.</li>
    <li>Replace the placeholder <code>TOKEN</code> and <code>ADMIN_CHAT_ID</code> with your actual Discord bot token and admin channel ID.</li>
    <li>Run the bot using <code>python bot.py</code>.</li>
</ol>

<h2>Available Services</h2>
<p>The bot currently supports a basic list of services. You can expand or modify the <code>services</code> dictionary with your own offerings and prices.</p>

<h2>Usage</h2>
<p>Once the bot is up and running, users can type <code>!ticket</code> to open a new ticket, choose a service, and proceed with payment via PayPal. Admins will be notified in the admin channel to verify the payment and process the order.</p>

<h2>License</h2>
<p>This project is licensed under the MIT License.</p>
