# Opie Taylor Minecraft Datapack

This is a datapack for Minecraft version 1.19+

## To install

Move the opie.zip into the datapacks directory of one of your Minecraft worlds.
E.g. It should go in `~/.minecraft/saves/{worldname}/datapacks/opie.zip`, where
`~/.minecraft/` is your Minecraft install directory (usually that is where it
is on Linux), on Windows it may be at
`C:\Users\{username}\AppData\Roaming\.minecraft` and on MacOS it may be at
`/home/users/{username}/Library/Application Support/minecraft`.

And `{worldname}` is the name of the world that you have previously created
where you want the datapack to be loaded.

While Minecraft is running, inside Minecraft:
 - Use `/datapack list enabled` to list the loaded datapacks
 - Use `/reload` to reload the datapack

## To build (development only)

Run `make` to make the zip file if there were any changes in the `data` folder
(after adding/editing any recipes).
