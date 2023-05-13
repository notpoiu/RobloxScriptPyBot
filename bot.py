import json, typing, os, importlib.util, discord
from discord import app_commands

scriptDefinitions = {}  # Dictionary to store script definitions

# Retrieve the list of script files in the "scripts" directory
script_files = [f for f in os.listdir("scripts") if f.endswith(".py")]

# Loop through each script file
for script_file in script_files:
    script_name = os.path.splitext(script_file)[0]  # Extract the script name from the file name
    module_name = f"scripts.{script_name}"  # Create the module name using the script name

    spec = importlib.util.spec_from_file_location(module_name, f"scripts/{script_file}")  # Create a module spec
    module = importlib.util.module_from_spec(spec)  # Create a module from the spec
    spec.loader.exec_module(module)  # Execute the module

    script_definition = module.script_definition  # Retrieve the script definition from the module
    scriptDefinitions[script_definition["Name"]] = script_definition  # Add the script definition to the dictionary

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
client = discord.Client(intents=intents)  # Create a Discord client with the specified intents
tree = app_commands.CommandTree(client)  # Create a command tree for the client

# Function to retrieve configuration values from the "config.json" file
def getConfig(key):
    with open("config.json", "r") as file:
        data = json.load(file)
        if key in data:
            return data[key]
        else:
            return False

@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=getConfig("Server Info")["Server ID"]))  # Sync the command tree with the guild
    print(f'We have logged in as {client.user}')

@tree.command(
    name="scripts",
    description="Gets scripts that I made!",
    guild=discord.Object(id=getConfig("Server Info")["Server ID"])  # Specify the guild for the command
)
@app_commands.choices(script=[
    app_commands.Choice(name=script_name, value=script_name) for script_name in scriptDefinitions.keys()
])
async def scripts(interaction: discord.Interaction, script: typing.Optional[app_commands.Choice[str]]):
    if script is None:
        embed = discord.Embed(
            title=getConfig('Server Info')['Server Name'],  # Set the embed title
            description=f"",  # Set the embed description
            color=discord.Color(int(getConfig("Bot Info")["Color Scheme"],16))  # Set the embed color
        )
        for script_name, script_data in scriptDefinitions.items():
            embed.add_field(
                name=script_name,  # Add the script name as the field name
                value=script_data["Description"],  # Add the script description as the field value
                inline=True
            )
        await interaction.response.send_message(embed=embed)  # Send the embed as a response
    else:
        script_data = scriptDefinitions.get(script.name)  # Get the script data for the specified script
        if script_data is not None:
            color = discord.Color(int(getConfig("Bot Info")["Color Scheme"],16))  # Default color
            if "Color" in script_data:  # Check if color is specified in script data
                color = discord.Color(int(script_data["Color"], 16))  # Set the specified color
                
            embed = discord.Embed(
                title=f"{script.name} | {getConfig('Server Info')['Server Name']}",  # Set the embed title
                description=script_data["Description"],  # Set the script description as the embed description
                color=color  # Set the embed color
            )
            embed.add_field(name="Code", value=f'```lua\n{script_data["Code"]}\n```', inline=False)  # Add the script code as a field

            author = script_data.get("Author")  # Get the author from the script data
            if author:  # Check if author exists
                embed.set_footer(text=f"Author: {author}")  # Set the author in the footer

            await interaction.response.send_message(embed=embed)  # Send the embed as a response
        else:
            await interaction.response.send_message(f"The Script (`{script.name}`) was not found.")  # Send an error message if the script is not found

client.run(getConfig("Bot Info")["Token"])  # Run the Discord bot with the specified token
