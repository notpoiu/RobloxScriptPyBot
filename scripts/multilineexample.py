script_definition = {
    "Name": "Infinite revive",
    "Description": "(real)",
    "Code": """
game.Players.LocalPlayer.Character.Humanoid.Health = 0
game.ReplicatedStorage.EntityInfo.Revive:FireServer()
    """,
    "Author": "upio",
    "Color": "3792f1"
}