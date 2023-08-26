# Dummy Hex Casting Addon

Or HexDummy for short! This is an up-to-date bare-bones template for starting a multiloader Hex Casting addon on
1.19.2 with Architectury. Includes all necessary dependencies on both Forge and Fabric loaders, plus some demo
bits. There is nothing specifically for Quilt here because Fabric builds implicitly support Quilt.

It is an amalgamation of the [HexCastingEmptyAddon](https://github.com/Talia-12/EmptyHexCastingAddon),
the forge-fabric-mixin 1.19.2 template
from [Architectury templates](https://github.com/architectury/architectury-templates), a few helpful bits from
[Hex Gloop](https://github.com/SamsTheNerd/HexGloop)'s setup, and some custom improvements thrown in.

## How to get started?

1. Fork the repo.
2. Make a copy of `template.env` and rename to `.env`. You can leave the API keys empty at this stage, just the file
   itself is needed
3. In the entire project, rename occurrences of `hexdummy` to your mod's id, both in files and in directory structure.
   Preferably also change occurrences adjacent to "Dummy" in text and file names to something related to your
   project, and change the base package path to something other than `net.hexdummy`, e.g.
   to `io.github.yourname.yourmod`.
3. Check out the [Architectury wiki](https://docs.architectury.dev/start) if you haven't yet. If you can't find
   something there, try searching on their Discord.
4. After checking out how demo patterns are registered, replace them with your own! You can look into Hex Casting
   sources to see real implementations. If you're new to this,
   here's a challenge: try making a single-pattern equivalent of the raycast mantra.
5. Launch the game client. Time for testing!
6. (Optional) Set up the publishMods tasks to simplify publishing updates: add necessary API keys to `.env`, add
   necessary project ids to root `gradle.properties`, and uncomment curseforge / modrinth / both segments in the
   publishMods task in `build.gradle` files from `forge` and `fabric` directories.

## Common problems

- IntelliJ IDEA shows false-positive errors about not being to access something in Kotlin files, but code compiles and
  runs fine.
    - Delete the .idea folder and re-open the project.

## Why did I make this?

To put it simply, I have a WIP addon of my own ([Hex Channeling](https://github.com/artynova/hexchanneling), shameless
plug time), and was looking for a sustainable long-term solution for supporting all the major loaders (Forge,
Fabric, Quilt). I had a hard time figuring it out at first, then got carried away, and the end result is something
that, I think, might be useful to people other than me.

Some conveniences I have managed to get to work so that you don't have to:

- Patchouli additions showing up in dev environment (there were problems with how patchouli reads its data).
- Slightly improved docgen system based on the one from HexCastingEmptyAddon, with a gradle task and fixes to a few
  issues:
    - Patterns category becoming a spoiler if there are spell patterns but no regular patterns.
    - Per-world patterns not actually parsing as per-world (was a regex issue).

There are other templates, like the aforementioned Talia-12's EmptyHexCastingAddon, but this one is a bit more
light, beginner-friendly, and up-to-date, in my opinion. However, do check out Talia's template if you would like
to see how to add configs and / or see how the Xplat multiloader layout works, which is what Hex Casting
itself and some other addons use.

## Acknowledgements

- Petrak@ and other Hex Casting devs.
- Talia-12, author of the stripped-down addon template which helped me get started with this one.
- SamsTheNerd, author of the Hex Gloop addon also powered by Architectury: its setup code helped me resolve an issue or
  two with Architectury here.
- Architectury devs and their discord.
