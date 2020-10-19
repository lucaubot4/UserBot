# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.b (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot help command """


from userbot import HELPER
from userbot.events import register

@register(outgoing=True, pattern="^.help(?: |$)(.*)")
async def helper(event):
    """ Per il comando .help, """
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        args = event.pattern_match.group(1)
        if args:
            if args in HELPER:
                await event.edit(str(HELPER[args]))
            else:
                await event.edit("Specifica un nome di modulo valido.")
        else:
            await event.edit("Per favore specifica per quale modulo vuoi aiuto!")
            string = ""
            for i in HELPER:
                string += str(i)
                string += "\n"
            await event.reply(string)
