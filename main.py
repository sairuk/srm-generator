#!/usr/bin/env python3

import os, json
userpath = "/home/{{ item.0.username }}/{{ fs_shortcuts }}/"
configs=[
    { 'configTitle': 'Atari 2600', 'romDirectory': f'{userpath}a2600', 'steamCategories': ['Atari 2600'] },
    { 'configTitle': 'Bandai Wonderswan Color', 'romDirectory': f'{userpath}wsc', 'steamCategories': ['WSC'] },
    { 'configTitle': 'Colecovision', 'romDirectory': f'{userpath}coleco', 'steamCategories': ['Colecovision'] },
    { 'configTitle': 'Commodore 64', 'romDirectory': f'{userpath}c64', 'steamCategories': ['Commodore 64'] },
    { 'configTitle': 'Commodore Amiga', 'romDirectory': f'{userpath}amiga', 'steamCategories': ['Amiga'] },
    { 'configTitle': 'Flatpaks', 'romDirectory': '/var/lib/flatpak/exports/share/applications/', 'steamCategories': ['Flatpak'] },
    { 'configTitle': 'MAME', 'romDirectory': f'{userpath}mame', 'steamCategories': ['MAME'] },
    { 'configTitle': 'Microsoft XBOX', 'romDirectory': f'{userpath}xbox', 'steamCategories': ['Microsoft XBOX'] },
    { 'configTitle': 'Nintendo 64', 'romDirectory': f'{userpath}n64', 'steamCategories': ['Nintendo 64'] },
    { 'configTitle': 'Nintendo Entertainment System', 'romDirectory': f'{userpath}nes', 'steamCategories': ['NES'] },
    { 'configTitle': 'Nintendo GameBoy Advance', 'romDirectory': f'{userpath}gba', 'steamCategories': ['Nintendo GameBoy Advance'] },
    { 'configTitle': 'Nintendo Gameboy (Color)', 'romDirectory': f'{userpath}gbc', 'steamCategories': ['GBC'] },
    { 'configTitle': 'Nintendo Gamecube', 'romDirectory': f'{userpath}ngc', 'steamCategories': ['Nintendo GC'] },
    { 'configTitle': 'Nintendo Switch', 'romDirectory': f'{userpath}nsw', 'steamCategories': ['Nintendo Switch'] },
    { 'configTitle': 'Nintendo Wii', 'romDirectory': f'{userpath}wii', 'steamCategories': ['Nintendo Wii'] },
    { 'configTitle': 'Nintendo Wii-U', 'romDirectory': f'{userpath}wiiu', 'steamCategories': ['Nintendo Wii-U'] },
    { 'configTitle': 'Non-Steam Shortcuts', 'romDirectory': f'{userpath}non-steam', 'steamCategories': ['Non-Steam Shortcuts'] },
    { 'configTitle': 'SEGA Dreamcast', 'romDirectory': f'{userpath}dc', 'steamCategories': ['SEGA Dreamcast'] },
    { 'configTitle': 'SEGA GameGear', 'romDirectory': f'{userpath}gg', 'steamCategories': ['SEGA GameGear'] },
    { 'configTitle': 'SEGA Mega Drive', 'romDirectory': f'{userpath}smd', 'steamCategories': ['SEGA Mega Drive'] },
    { 'configTitle': 'SEGA Model 3', 'romDirectory': f'{userpath}model3', 'steamCategories': ['SEGA Model 3'] },
    { 'configTitle': 'Sony PlayStation 1', 'romDirectory': f'{userpath}ps1', 'steamCategories': ['PS1'] },
    { 'configTitle': 'Sony PlayStation 2', 'romDirectory': f'{userpath}ps2', 'steamCategories': ['PS2'] },
    { 'configTitle': 'Sony PlayStation 3"', 'romDirectory': f'{userpath}ps3', 'steamCategories': ['PS3'] },
    { 'configTitle': 'Super Nintendo', 'romDirectory': f'{userpath}snes', 'steamCategories': ['SNES'] },
    #{ 'configTitle': '', 'romDirectory': '', 'steamCategories': [''] },

]

def main():

    configset = []
    for config in configs:
        f = open('template.json','r')
        data = json.load(f)
        data['configTitle'] = config['configTitle']
        data['romDirectory'] = config['romDirectory']
        data['steamCategories'] = config['steamCategories']
        configset.append(data)

    with open("userConfigurations.json.j2","w") as out:
        json.dump(configset, out, ensure_ascii=True, indent=4, sort_keys=False)

    return


if __name__ == "__main__":
    main()
