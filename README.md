# H3DialogTool

This tool is written in Python, and was created using ChatGPT and myself. As a newbie programmer, some features will be inefficient but working, so please fill me in on any flaws you see in my code, potential fixes or more efficient workarounds. Do with the code however you please, I do not care. If you want to use this in a module somewhere, go ahead.

*THIS IS CURRENTLY A WORK-IN-PROGRESS*

Before downloading this tool, make sure you've downloaded the latest version of Python and **IMPORTANT** make sure you add Python to Path in the installer or manually add the path to "python.exe" in environment variables. Make sure you have this repository set-up, so the facial animations import properly: https://github.com/yokimklein/H3EK-FaceFXWrapper.

This tool works with .wav files extracted using Reclaimer or downloaded from https://www.sounds-resource.com/

**Only Feature As Of Right Now** This tool currently takes .wav files from a given directory (Presumabley all contained within a single directory given) and organizes these .wav files into folders named after the .wav files, renames the .wav files into their designated permutation names that are contained within brackets[] and creates an empty .txt file with the same permutation name as the associated .wav file. So, the only part left to do before importing with "tool.exe", is the fun part of listening to the audio and typing what it says! Later on I'll add a boolean to turn off .txt file creation if you want to work with other types of sound.

- Planned features

- Batch .wav import for tool -- An easier way to bulk-import sound, so you don't have to import sounds one by one. Saves time for dialogue importing, and its a good way to update your own soundbank(.fsb) without overriding with it with someone elses soundbank *You can change the command line for whatever you want e.g. mission_dialogue\unit_dialogue*

- Batch .sound tag set default/custom -- For some reason in the .sound tag, when its imported, the "gain base" parameter is set to "-3" I find that annoying on a personal level, so this feature will open a directory of .sound tags (in guerilla) and change "gain base" to zero. [*This one is in the works*] On top of that, say you want a specific parameter changed for a directory of sound tags (For example, upping the pitch of brute dialogue .sound tags so they sound like grunts), you can specify that parameter to be changed. *This feature is kind of messy, the way I'm approaching this, but it for sure works. When this feature is running, you have to let the computer sit and do its thing, don't touch the mouse, also you have to set up several windows properly for the automation to work. I'll demonstrate this in a video, when this is complete*

Maybe feature: Batch .sound tag copy values -- Say you are porting folders of .sound tags from H2 to H3, you have everything imported as a H3 .sound tag and you don't want to copy down paramaters from the H2 .sound tags to the ported H3 .sound tags for hours on end. This feature will iterate down the H2 .sound tags in H2 Guerilla, add specified values to an excel sheet, and paste them into the H3 ported .sound tag in H3 Guerilla for the whole directory of H2 .sound tags and H3 .sound tags . *This feature works similar to the [Batch .sound tag set default/custom] feature and will be fragile. I feel like this feature may be unneccesary, but if not, let me know*

- A pretty GUI and customizability for all Halo Games -- So this tool is geared towards H3EK, but most features can also work for all the other Halo editing kits after changing a few lines. I will specificy this in a video.

***HOW TO USE RIGHT NOW***

All you need to do is open h3wavtool.py file in txt editor, and specify your directory of .wav files. Open cmd to where the tool is located and run "python h3wavtool.py". That's it folders, and files will be automatically organized and renamed. :D

Permission issues may arise if you don't have admin privileges or your trying to work with wav files in a flash drive.

If you have any questions you can msg me on Discord @ Sargent 0#1097

