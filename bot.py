import json,typing,os,importlib.util,discord
from discord import app_commands

scriptDefinitions = {}

script_files = [f for f in os.listdir("scripts") if f.endswith(".py")]

for script_file in script_files:
    script_name = os.path.splitext(script_file)[0]
    module_name = f"scripts.{script_name}"

    spec = importlib.util.spec_from_file_location(module_name, f"scripts/{script_file}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    script_definition = module.script_definition
    scriptDefinitions[script_definition["Name"]] = script_definition

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)


def getConfig(key):
    with open("config.json", "r") as file:
        data = json.load(file)
        if key in data:
            return data[key]
        else:
            return False

@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=getConfig("Server Info")["Server ID"]))
    print(f'We have logged in as {client.user}')


@tree.command(
    name="scripts",
    description="Gets scripts that I made!",
    guild=discord.Object(id=getConfig("Server Info")["Server ID"])
)
@app_commands.choices(script=[
    app_commands.Choice(name=script_name, value=script_name) for script_name in scriptDefinitions.keys()
])
async def scripts(interaction: discord.Interaction, script: typing.Optional[app_commands.Choice[str]]):
    if script is None:
        embed = discord.Embed(
            title=getConfig('Server Info')['Server Name'],
            description=f"",
            color=discord.Color(int(getConfig("Bot Info")["Color Scheme"],16))
        )
        for script_name, script_data in scriptDefinitions.items():
            embed.add_field(
                name=script_name,
                value=script_data["Description"],
                inline=True
            )
        await interaction.response.send_message(embed=embed)
    else:
        script_data = scriptDefinitions.get(script.name)
        if script_data is not None:
            color = discord.Color(int(getConfig("Bot Info")["Color Scheme"],16))  # Default color
            if "Color" in script_data:  # Check if color is specified in script data
                color = discord.Color(int(script_data["Color"], 16))
            
            embed = discord.Embed(
                title=f"{script.name} | {getConfig('Server Info')['Server Name']}",
                description=script_data["Description"],
                color=color
            )
            embed.add_field(name="Code", value=f'```lua\n{script_data["Code"]}\n```', inline=False)
            author = script_data.get("Author")  # Get the author from the script data
            if author:  # Check if author exists
                embed.set_footer(text=f"Author: {author}")  # Set the author in the footer
            await interaction.response.send_message(embed=embed)
        else:
            await interaction.response.send_message(f"The Script (`{script.name}`) was not found.")


client.run(getConfig("Bot Info")["Token"])
