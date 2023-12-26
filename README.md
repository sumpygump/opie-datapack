# Opie Taylor Minecraft Datapack

This is a datapack for Minecraft version 1.19+

## To install

Move the docs/opie.zip into the datapacks directory of one of your Minecraft worlds.
E.g. It should go in `{minecraft_dir}/saves/{worldname}/datapacks/opie.zip`, where
`{minecraft_dir}` is your Minecraft install directory, see below for paths per OS.

- Linux: `/home/{username}/.minecraft`
- Windows: `C:\Users\{username}\AppData\Roaming\.minecraft`
- MacOS: `/Users/{username}/Library/Application Support/minecraft`

Where `{username}` is the your user name on the OS.

And `{worldname}` is the name of the world that you have previously created
where you want the datapack to be loaded.

While Minecraft is running, inside Minecraft:
 - Run `/datapack list enabled` to list the loaded datapacks
 - Run `/reload` to reload the datapack

## To rebuild (development only)

Run `make recipes` to regenerate all the recipes (only needed if changes were
made in the bin python files.

Run `make datapack` to make the zip file if there were any changes in the `data` folder
(after adding/editing any recipes).
