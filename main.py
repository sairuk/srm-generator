#!/usr/bin/env python3

import os, json, yaml
srm_userpath = "/home/{{ item.0.username }}/{{ fs_shortcuts }}/"
configs=[
    { 
        'title': 'Atari 2600', 
        'srm_romdir': f'{srm_userpath}a2600', 
        'categories': ['Atari 2600'], 
        'short_name': 'a2600',
        'format': 'mamesl', 
        'mode': 'file', 
        'exec': 'mame', 
        'ini': '~/.mame/mame.ini', 
        'scan_romdir': 'MAME_BASE_DIR_SOFT_ROMS/SYSTEM_NAME', 
        'scan_artdir': 'MAME_BASE_DIR_SOFT_ART/SYSTEM_NAME', 
        'data_dir': 'MAME_BASE_DIR_HASH', 
        'soft_lists': '', 
        'working_dir': 'system-working-dir', 
        'extensions': 'zip', 
        'mister_core': 'Atari2600', 
        'extension': 'zip', 
        'cmd': 'GAME_EXEC SYSTEM_NAME -cart ROM_BASENAME'
    },
    { 
        'title': 'Atari 800', 
        'srm_romdir': f'{srm_userpath}a800', 
        'categories': ['Atari 800'], 
        'short_name': 'a800',
        'format': 'mamesl', 
        'mode': 'file', 
        'exec': 'mame', 
        'ini': '~/.mame/mame.ini', 
        'scan_romdir': 'MAME_BASE_DIR_SOFT_ROMS/SYSTEM_NAME', 
        'scan_artdir': 'MAME_BASE_DIR_SOFT_ART/SYSTEM_NAME', 
        'data_dir': 'MAME_BASE_DIR_HASH', 
        'soft_lists': '', 
        'working_dir':'system-working-dir', 
        'extensions': 'zip', 
        'mister_core': 'ATARI800', 
        'extension': 'zip', 
        'cmd': 'GAME_EXEC SYSTEM_NAME ROM_BASENAME'
    },
    { 
        'title': 'Atari 5200', 
        'srm_romdir': f'{srm_userpath}a5200', 
        'categories': ['Atari 5200'], 
        'short_name': 'a5200',
        'format': 'mamesl', 
        'mode': 'file', 
        'exec': 'mame', 
        'ini': '~/.mame/mame.ini', 
        'scan_romdir': 'MAME_BASE_DIR_SOFT_ROMS/SYSTEM_NAME', 
        'scan_artdir': 'MAME_BASE_DIR_SOFT_ART/SYSTEM_NAME', 
        'data_dir': 'MAME_BASE_DIR_HASH', 
        'soft_lists': '', 
        'working_dir':'system-working-dir', 
        'extensions': 'zip', 
        'mister_core': 'ATARI5200', 
        'extension': 'zip', 
        'cmd': 'GAME_EXEC SYSTEM_NAME -cart ROM_BASENAME'
    },
    { 
        'title': 'Atari 7800', 
        'srm_romdir': f'{srm_userpath}a7800', 
        'categories': ['Atari 7800'], 
        'short_name': 'a7800',
        'format': 'mamesl', 
        'mode': 'file', 
        'exec': 'mame', 
        'ini': '~/.mame/mame.ini', 
        'scan_romdir': 'MAME_BASE_DIR_SOFT_ROMS/SYSTEM_NAME', 
        'scan_artdir': 'MAME_BASE_DIR_SOFT_ART/SYSTEM_NAME', 
        'data_dir': 'MAME_BASE_DIR_HASH', 
        'soft_lists': '', 
        'working_dir':'system-working-dir', 
        'extensions': 'zip', 
        'mister_core': 'ATARI7800', 
        'extension': 'zip', 
        'cmd': 'GAME_EXEC SYSTEM_NAME -cart ROM_BASENAME'
    },
    { 
        'title': 'Atari Lynx', 
        'srm_romdir': f'{srm_userpath}lynx', 
        'categories': ['Atari Lynx'], 
        'short_name': 'lynx',
        'format': 'mamesl', 
        'mode': 'file', 
        'exec': 'mame', 
        'ini': '~/.mame/mame.ini', 
        'scan_romdir': 'MAME_BASE_DIR_SOFT_ROMS/SYSTEM_NAME', 
        'scan_artdir': 'MAME_BASE_DIR_SOFT_ART/SYSTEM_NAME', 
        'data_dir': 'MAME_BASE_DIR_HASH', 
        'soft_lists': '', 
        'working_dir':'system-working-dir', 
        'extensions': 'zip', 
        'mister_core': 'AtariLynx', 
        'extension': 'zip', 
        'cmd': 'GAME_EXEC SYSTEM_NAME ROM_BASENAME'
    },
    { 
        'title': 'Astrocade', 
        'srm_romdir': f'{srm_userpath}astrocde', 
        'categories': ['Astrocade'], 
        'short_name': 'astrocde',
        'format': 'mamesl', 
        'mode': 'file', 
        'exec': 'mame', 
        'ini': '~/.mame/mame.ini', 
        'scan_romdir': 'MAME_BASE_DIR_SOFT_ROMS/SYSTEM_NAME', 
        'scan_artdir': 'MAME_BASE_DIR_SOFT_ART/SYSTEM_NAME', 
        'data_dir': 'MAME_BASE_DIR_HASH', 
        'soft_lists': '', 
        'working_dir':'system-working-dir', 
        'extensions': 'zip', 
        'mister_core': 'Astrocade', 
        'extension': 'zip', 
        'cmd': 'GAME_EXEC SYSTEM_NAME -cart ROM_BASENAME'
    },
    { 
        'title': 'AdventureVision', 
        'srm_romdir': f'{srm_userpath}advision', 
        'categories': ['AdventureVision'], 
        'short_name': 'advision',
        'format': 'mamesl', 
        'mode': 'file', 
        'exec': 'mame', 
        'ini': '~/.mame/mame.ini', 
        'scan_romdir': 'MAME_BASE_DIR_SOFT_ROMS/SYSTEM_NAME', 
        'scan_artdir': 'MAME_BASE_DIR_SOFT_ART/SYSTEM_NAME', 
        'data_dir': 'MAME_BASE_DIR_HASH', 
        'soft_lists': '', 
        'working_dir':'system-working-dir', 
        'extensions': 'zip', 
        'mister_core': 'AVision', 
        'extension': 'zip', 
        'cmd': 'GAME_EXEC SYSTEM_NAME ROM_BASENAME'
    },
    { 
        'title': 'Bandai Wonderswan Color',
        'srm_romdir': f'{srm_userpath}wsc', 
        'categories': ['WSC'],
        'short_name': 'wsc',
        'format': 'mamesl', 
        'mode': 'file', 
        'exec': 'mame', 
        'ini': '~/.mame/mame.in', 
        'scan_romdir': 'MAME_BASE_DIR_SOFT_ROMS/SYSTEM_NAME', 
        'scan_artdir': 'MAME_BASE_DIR_SOFT_ART/SYSTEM_NAME', 
        'data_dir': 'MAME_BASE_DIR_HASH', 
        'soft_lists': '', 
        'working_dir': 'system-working-dir', 
        'extensions': 'zip', 
        'mister_core': 'NONE', 
        'extension': 'zip', 
        'cmd': 'GAME_EXEC SYSTEM_NAME ROM_BASENAME'
    },
    { 
        'title': 'Amstrad GX4000',
        'srm_romdir': f'{srm_userpath}gx4000', 
        'categories': ['Amstrad GX4000'],
        'short_name': 'gx4000',
        'format': 'mamesl', 
        'mode': 'file', 
        'exec': 'mame', 
        'ini': '~/.mame/mame.ini', 
        'scan_romdir': 'MAME_BASE_DIR_SOFT_ROMS/SYSTEM_NAME', 
        'scan_artdir': 'MAME_BASE_DIR_SOFT_ART/SYSTEM_NAME', 
        'data_dir': 'MAME_BASE_DIR_HASH', 
        'soft_lists': '', 
        'working_dir': 'system-working-dir', 
        'extensions': 'zip', 
        'mister_core': 'NONE', 
        'extension': 'zip', 
        'cmd': 'GAME_EXEC SYSTEM_NAME ROM_BASENAME'
    },
    { 
        'title': 'Colecovision',
        'srm_romdir': f'{srm_userpath}coleco',
        'categories': ['Colecovision'],
        'short_name': 'coleco',
        'format': 'mamesl', 
        'mode': 'file', 
        'exec': 'mame', 
        'ini': '~/.mame/mame.ini', 
        'scan_romdir': 'MAME_BASE_DIR_SOFT_ROMS/SYSTEM_NAME', 
        'scan_artdir': 'MAME_BASE_DIR_SOFT_ART/SYSTEM_NAM', 
        'data_dir': 'MAME_BASE_DIR_HASH', 
        'soft_lists': '', 
        'working_dir': 'system-working-dir', 
        'extensions': 'zip', 
        'mister_core': 'ColecoVision', 
        'extension': 'zip', 
        'cmd': 'GAME_EXEC SYSTEM_NAME ROM_BASENAME'
    },
    { 
        'title': 'Commodore 64',
        'srm_romdir': f'{srm_userpath}c64',
        'categories': ['Commodore 64'],
        'short_name': 'c64',
        'format': 'generic', 
        'mode': 'file', 
        'exec': '', 
        'ini': '', 
        'scan_romdir': '/var/lib/freestation/games/SYSTEM_NAME', 
        'scan_artdir': '', 
        'data_dir': '', 
        'soft_lists': '', 
        'working_dir': 'system-working-dir', 
        'extensions': 'zip', 
        'mister_core': 'C64', 
        'extension': 'zip', 
        'cmd': 'GAME_EXEC c64p -joy1 joy -joy2 joy ROM_BASENAME'
    },
    { 
        'title': 'Commodore 64 Disks - Original',
        'srm_romdir': f'{srm_userpath}c64_flop_orig',
        'categories': ['Commodore 64'],
        'short_name': 'c64_flop_orig',
        'format': 'mamesl', 
        'mode': 'file', 
        'exec': 'mame', 
        'ini': '~/.mame/mame.ini', 
        'scan_romdir': 'MAME_BASE_DIR_SOFT_ROMS/SYSTEM_NAME', 
        'scan_artdir': 'MAME_BASE_DIR_SOFT_ART/SYSTEM_NAME', 
        'data_dir': 'MAME_BASE_DIR_HASH', 
        'soft_lists': '', 
        'working_dir':'system-working-dir', 
        'extensions': 'zip', 
        'mister_core': 'C64', 
        'extension': 'zip', 
        'cmd': 'GAME_EXEC c64p -joy1 joy -joy2 joy -autoboot_script /var/lib/freestation/config/mame/autoboots/c64_diskloader.lua -autoboot_delay 2 -flop ROM_BASENAME'
    },
    { 
        'title': 'Commodore Amiga',
        'srm_romdir': f'{srm_userpath}amiga',
        'categories': ['Amiga'],
        'short_name': 'amiga',
        'format': 'generic', 
        'mode': 'file-parent', 
        'exec': '/usr/local/bin/fs-uae-50hz.sh', 
        'ini': '~/.mame/mame.ini', 
        'scan_romdir': '/var/lib/freestation/games/SYSTEM_NAME/floppy', 
        'scan_artdir': 'MAME_BASE_DIR_SOFT_ART/SYSTEM_NAME', 
        'data_dir': 'system-data-dir', 
        'soft_lists': '', 
        'working_dir':'system-working-dir', 
        'extensions': 'adf, ipf', 
        'mister_core': 'Amiga', 
        'extension': 'ipf', 
        'cmd': 'GAME_EXEC --amiga-model=A500 --floppy-drive-0=ROM_PATH --fullscreen'
    },
    { 
        'title': 'Flatpaks', 
        'srm_romdir': '/var/lib/flatpak/exports/share/applications/',
        'categories': ['Flatpak'],
        'short_name': 'flatpak',
        'format': 'generic', 
        'mode': 'file', 
        'exec': '', 
        'ini': '', 
        'scan_romdir': '/var/lib/flatpak/exports/share/applications/', 
        'scan_artdir': '', 
        'data_dir': '', 
        'soft_lists': '', 
        'working_dir': 'system-working-dir', 
        'extensions': 'desktop', 
        'mister_core': 'NONE', 
        'extension': 'desktop', 
        'cmd': 'exo-open "ROM_PATH"'
    },
    { 
        'title': 'MAME',
        'srm_romdir': f'{srm_userpath}mame',
        'categories': ['MAME'],
        'short_name': 'mame',
        'format': 'mame', 
        'mode': 'file', 
        'exec': 'mame', 
        'ini': '~/.mame/mame.ini', 
        'scan_romdir': 'MAME_BASE_DIR_SOFT_ROMS/SYSTEM_NAME', 
        'scan_artdir': 'MAME_BASE_DIR_SOFT_ART/SYSTEM_NAME', 
        'data_dir': 'system-data-dir', 
        'soft_lists': '', 
        'working_dir': 'system-working-dir', 
        'extensions': 'zip', 
        'mister_core': 'mame', 
        'extension': 'zip', 
        'cmd': 'GAME_EXEC ROM_NAME'
    },
    { 
        'title': 'Microsoft MSX1',
        'srm_romdir': f'{srm_userpath}msx',
        'categories': ['Microsoft MSX1'],
        'short_name': 'msx',
        'format': 'mame', 
        'mode': 'file', 
        'exec': 'mame', 
        'ini': '~/.mame/mame.ini', 
        'scan_romdir': 'MAME_BASE_DIR_SOFT_ROMS/SYSTEM_NAME', 
        'scan_artdir': 'MAME_BASE_DIR_SOFT_ART/SYSTEM_NAME', 
        'data_dir': '', 
        'soft_lists': '', 
        'working_dir': 'system-working-dir', 
        'extensions': 'zip', 
        'mister_core': 'MSX1', 
        'extension': 'zip', 
        'cmd': 'GAME_EXEC SYSTEM_NAME ROM_BASENAME'
    },
    { 
        'title': 'Microsoft XBOX',
        'srm_romdir': f'{srm_userpath}xbox',
        'categories': ['Microsoft XBOX'],
        'short_name': 'xbox',
        'format': 'generic', 
        'mode': 'file', 
        'exec': '/usr/bin/flatpak run app.xemu.xemu', 
        'ini': '', 
        'scan_romdir': '/var/lib/freestation/games/SYSTEM_NAME', 
        'scan_artdir': '', 
        'data_dir': '', 
        'soft_lists': '', 
        'working_dir': 'system-working-dir', 
        'extensions': 'iso', 
        'mister_core': 'NONE', 
        'extension': 'iso', 
        'cmd': 'GAME_EXEC -full-screen -dvd_path "ROM_PATH"'
    },
    { 
        'title': 'Microsoft XBOX 360',
        'srm_romdir': f'{srm_userpath}x360',
        'categories': ['Microsoft XBOX 360'],
        'short_name': 'x360',
        'format': 'generic', 
        'mode': 'file', 
        'exec': 'xenia', 
        'ini': '~/.mame/mame.ini', 
        'scan_romdir': '/var/lib/freestation/games/SYSTEM_NAME', 
        'scan_artdir': 'MAME_BASE_DIR_SOFT_ART/SYSTEM_NAME', 
        'data_dir': 'MAME_BASE_DIR_HASH', 
        'soft_lists': '', 
        'working_dir': 'system-working-dir', 
        'extensions': 'zip', 
        'mister_core': 'NONE', 
        'extension': 'zip', 
        'cmd': 'GAME_EXEC ROM_PATH'
    },
    { 
        'title': 'Nintendo 3DS',
        'srm_romdir': f'{srm_userpath}3ds',
        'categories': ['Nintendo 3DS'],
        'short_name': '3ds',
        'format': 'generic', 
        'mode': 'file', 
        'exec': '/usr/bin/flatpak run io.github.lime3ds.Lime3DS', 
        'ini': '', 
        'scan_romdir': '/var/lib/freestation/games/SYSTEM_NAME', 
        'scan_artdir': '', 
        'data_dir': '', 
        'soft_lists': '', 
        'working_dir': 'system-working-dir', 
        'extensions': '3ds', 
        'mister_core': 'NONE', 
        'extension': '3ds', 
        'cmd': 'GAME_EXEC "ROM_PATH"'
    },
    { 
        'title': 'SNK NEO-GEO CD',
        'srm_romdir': f'{srm_userpath}neocd',
        'categories': ['SNK NEO-GEO CD'],
        'short_name': 'neocd',
        'format': 'mamesl', 
        'mode': 'dir', 
        'exec': 'mame', 
        'ini': '~/.mame/mame.ini', 
        'scan_romdir': 'MAME_BASE_DIR_SOFT_DISK/SYSTEM_NAME', 
        'scan_artdir': 'MAME_BASE_DIR_SOFT_ART/SYSTEM_NAME', 
        'data_dir': 'MAME_BASE_DIR_HASH', 
        'soft_lists': '', 
        'working_dir': 'system-working-dir', 
        'extensions': 'zip', 
        'mister_core': 'NeoGeo-CD', 
        'extension': 'zip', 
        'cmd': 'GAME_EXEC SYSTEM_NAME ROM_BASENAME'
    },
    { 
        'title': 'SNK NEO-GEO AES',
        'srm_romdir': f'{srm_userpath}neogeo',
        'categories': ['SNK NEO-GEO AES'],
        'short_name': 'neogeo',
        'format': 'mamesl', 
        'mode': 'file', 
        'exec': 'mame', 
        'ini': '~/.mame/mame.ini', 
        'scan_romdir': 'MAME_BASE_DIR_SOFT_DISK/SYSTEM_NAME', 
        'scan_artdir': 'MAME_BASE_DIR_SOFT_ART/SYSTEM_NAME', 
        'data_dir': 'MAME_BASE_DIR_HASH', 
        'soft_lists': '', 
        'working_dir': 'system-working-dir', 
        'extensions': 'zip', 
        'mister_core': 'NEOGEO', 
        'extension': 'zip', 
        'cmd': 'GAME_EXEC SYSTEM_NAME ROM_BASENAME'
    },
    { 
        'title': 'Nintendo 64',
        'srm_romdir': f'{srm_userpath}n64',
        'categories': ['Nintendo 64'],
        'short_name': 'n64',
        'format': 'mamesl', 
        'mode': 'file', 
        'exec': '/usr/bin/flatpak run io.github.simple64.simple64', 
        'ini': '~/.mame/mame.ini', 
        'scan_romdir': '/var/lib/freestation/games/SYSTEM_NAME', 
        'scan_artdir': 'MAME_BASE_DIR_SOFT_ART/SYSTEM_NAME', 
        'data_dir': 'MAME_BASE_DIR_HASH', 
        'soft_lists': '', 
        'working_dir': 'system-working-dir', 
        'extensions': 'z64', 
        'mister_core': 'N64', 
        'extension': 'z64', 
        'cmd': 'GAME_EXEC ROM_PATH'
    },
    { 
        'title': 'Nintendo Entertainment System',
        'srm_romdir': f'{srm_userpath}nes',
        'categories': ['NES'],
        'short_name': 'nes',
        'format': 'mamesl', 
        'mode': 'file', 
        'exec': 'mame', 
        'ini': '~/.mame/mame.ini', 
        'scan_romdir': 'MAME_BASE_DIR_SOFT_ROMS/SYSTEM_NAME', 
        'scan_artdir': 'MAME_BASE_DIR_SOFT_ART/SYSTEM_NAME', 
        'data_dir': 'MAME_BASE_DIR_HASH', 
        'soft_lists': '', 
        'working_dir': 'system-working-dir', 
        'extensions': 'zip', 
        'mister_core': 'NES', 
        'extension': 'zip', 
        'cmd': 'GAME_EXEC SYSTEM_NAME ROM_BASENAME'
    },
    { 
        'title': 'Nintendo GameBoy Advance',
        'srm_romdir': f'{srm_userpath}gba',
        'categories': ['Nintendo GameBoy Advance'],
        'short_name': 'gba',
        'format': 'mamesl', 
        'mode': 'file', 
        'exec': 'mame', 
        'ini': '~/.mame/mame.ini', 
        'scan_romdir': 'MAME_BASE_DIR_SOFT_ROMS/SYSTEM_NAME', 
        'scan_artdir': 'MAME_BASE_DIR_SOFT_ART/SYSTEM_NAME', 
        'data_dir': 'MAME_BASE_DIR_HASH', 
        'soft_lists': '', 
        'working_dir': 'system-working-dir', 
        'extensions': 'zip', 
        'mister_core': 'GBA', 
        'extension': 'zip', 
        'cmd': 'GAME_EXEC SYSTEM_NAME ROM_BASENAME'
    },
    { 
        'title': 'Nintendo Gameboy (Color)',
        'srm_romdir': f'{srm_userpath}gbc',
        'categories': ['GBC'],
        'short_name': 'gbcolor',
        'format': 'mamesl', 
        'mode': 'file', 
        'exec': 'mame', 
        'ini': '~/.mame/mame.ini', 
        'scan_romdir': 'MAME_BASE_DIR_SOFT_ROMS/SYSTEM_NAME', 
        'scan_artdir': 'MAME_BASE_DIR_SOFT_ART/SYSTEM_NAME', 
        'data_dir': 'MAME_BASE_DIR_HASH', 
        'soft_lists': '', 
        'working_dir': 'system-working-dir', 
        'extensions': 'zip', 
        'mister_core': 'GBC', 
        'extension': 'zip', 
        'cmd': 'GAME_EXEC SYSTEM_NAME ROM_BASENAME'
        
    },
    { 
        'title': 'Nintendo GameCube',
        'srm_romdir': f'{srm_userpath}ngc',
        'categories': ['Nintendo GC'],
        'short_name': 'ngc',
        'format': 'generic', 
        'mode': 'file-parent', 
        'exec': '/usr/bin/flatpak run org.DolphinEmu.dolphin-emu', 
        'ini': '/var/lib/freestation/games/SYSTEM_NAME', 
        'scan_romdir': '', 
        'scan_artdir': '', 
        'data_dir': '', 
        'soft_lists': '', 
        'working_dir': 'system-working-dir', 
        'extensions': 'iso', 
        'mister_core': 'NONE', 
        'extension': 'iso', 
        'cmd': 'GAME_EXEC -b -e "ROM_PATH"'
    },
    { 
        'title': 'Nintendo Switch',
        'srm_romdir': f'{srm_userpath}nsw',
        'categories': ['Nintendo Switch'],
        'short_name': 'nsw',
        'format': 'generic', 
        'mode': 'file', 
        'exec': '/usr/bin/flatpak run org.ryujinx.Ryujinx', 
        'ini': '', 
        'scan_romdir': '/var/lib/freestation/games/nsw/NSP/', 
        'scan_artdir': '', 
        'data_dir': '', 
        'soft_lists': '', 
        'working_dir': 'system-working-dir', 
        'extensions': 'nsp', 
        'mister_core': 'NONE', 
        'extension': 'nsp', 
        'cmd': 'GAME_EXEC SYSTEM_NAME -cart "ROM_PATH"'
    },
    { 
        'title': 'Nintendo Wii',
        'srm_romdir': f'{srm_userpath}wii',
        'categories': ['Nintendo Wii'],
        'short_name': 'wii',
        'format': 'generic', 
        'mode': 'file-parent', 
        'exec': '/usr/bin/flatpak run org.DolphinEmu.dolphin-emu', 
        'ini': '', 
        'scan_romdir': '/var/lib/freestation/games/SYSTEM_NAME', 
        'scan_artdir': '', 
        'data_dir': '', 
        'soft_lists': '', 
        'working_dir': 'system-working-dir', 
        'extensions': 'iso, wbfs', 
        'mister_core': 'NONE', 
        'extension': 'iso', 
        'cmd': 'GAME_EXEC -b -e "ROM_PATH"'
    },
    { 
        'title': 'Nintendo Wii-U',
        'srm_romdir': f'{srm_userpath}wiiu',
        'categories': ['Nintendo Wii-U'],
        'short_name': 'wiiu',
        'format': 'generic', 
        'mode': 'file-parent', 
        'exec': '/usr/local/bin/cemu', 
        'ini': '', 
        'scan_romdir': '/var/lib/freestation/games/SYSTEM_NAME', 
        'scan_artdir': '', 
        'data_dir': '', 
        'soft_lists': '', 
        'working_dir': 'system-working-dir', 
        'extensions': 'wud', 
        'mister_core': 'NONE', 
        'extension': 'wud', 
        'cmd': 'GAME_EXEC -g "ROM_PATH"'
    },
    { 
        'title': 'Non-Steam Shortcuts',
        'srm_romdir': f'{srm_userpath}non-steam',
        'categories': ['Non-Steam Shortcuts'],
        'short_name': 'non-steam',
        'format': '', 
        'mode': '', 
        'exec': '', 
        'ini': '', 
        'scan_romdir': '', 
        'scan_artdir': '', 
        'data_dir': '', 
        'soft_lists': '', 
        'working_dir':'', 
        'extensions': '', 
        'mister_core': 'NONE', 
        'extension': '', 
        'cmd': ''
    },
    { 
        'title': 'SEGA Dreamcast',
        'srm_romdir': f'{srm_userpath}dc',
        'categories': ['SEGA Dreamcast'],
        'short_name': 'dc',
        'format': 'mamesl', 
        'mode': 'file-parent', 
        'exec': '/usr/bin/flatpak run org.flycast.Flycast', 
        'ini': '~/.mame/mame.ini', 
        'scan_romdir': 'MAME_BASE_DIR_SOFT_DISK/SYSTEM_NAME', 
        'scan_artdir': 'MAME_BASE_DIR_SOFT_ART/SYSTEM_NAME', 
        'data_dir': 'system-data-dir', 
        'soft_lists': '', 
        'working_dir': 'system-working-dir', 
        'extensions': 'chd', 
        'mister_core': 'NONE', 
        'extension': 'chd', 
        'cmd': 'GAME_EXEC "ROM_PATH"'
    },
    { 
        'title': 'SEGA GameGear',
        'srm_romdir': f'{srm_userpath}gg',
        'categories': ['SEGA GameGear'],
        'short_name': 'gamegear',
        'format': 'mamesl', 
        'mode': 'file', 
        'exec': 'mame', 
        'ini': '~/.mame/mame.ini', 
        'scan_romdir': 'MAME_BASE_DIR_SOFT_ROMS/SYSTEM_NAME', 
        'scan_artdir': 'MAME_BASE_DIR_SOFT_ART/SYSTEM_NAME', 
        'data_dir': 'MAME_BASE_DIR_HASH', 
        'soft_lists': '', 
        'working_dir': 'system-working-dir', 
        'extensions': 'zip', 
        'mister_core': 'GameGear', 
        'extension': 'zip', 
        'cmd': 'GAME_EXEC SYSTEM_NAME ROM_BASENAME'
    },
    { 
        'title': 'SEGA Master System',
        'srm_romdir': f'{srm_userpath}sms',
        'categories': ['SEGA Master System'],
        'short_name': 'sms',
        'format': 'mamesl', 
        'mode': 'file', 
        'exec': 'mame', 
        'ini': '~/.mame/mame.ini', 
        'scan_romdir': 'MAME_BASE_DIR_SOFT_ROMS/SYSTEM_NAME', 
        'scan_artdir': 'MAME_BASE_DIR_SOFT_ART/SYSTEM_NAME', 
        'data_dir': 'MAME_BASE_DIR_HASH', 
        'soft_lists': '', 
        'working_dir': 'system-working-dir', 
        'extensions': 'zip', 
        'mister_core': 'SMS', 
        'extension': 'zip', 
        'cmd': 'GAME_EXEC SYSTEM_NAME ROM_BASENAME'
    },
    { 
        'title': 'SEGA Mega Drive',
        'srm_romdir': f'{srm_userpath}smd',
        'categories': ['SEGA Mega Drive'],
        'short_name': 'megadriv',
        'format': 'mamesl', 
        'mode': 'file', 
        'exec': 'mame', 
        'ini': '~/.mame/mame.ini', 
        'scan_romdir': 'MAME_BASE_DIR_SOFT_ROMS/SYSTEM_NAME', 
        'scan_artdir': 'MAME_BASE_DIR_SOFT_ART/SYSTEM_NAME', 
        'data_dir': 'MAME_BASE_DIR_HASH', 
        'soft_lists': '', 
        'working_dir': 'system-working-dir', 
        'extensions': 'zip', 
        'mister_core': 'MegaDrive', 
        'extension': 'zip', 
        'cmd': 'GAME_EXEC SYSTEM_NAME ROM_BASENAME'
    },
    { 
        'title': 'SEGA Mega CD',
        'srm_romdir': f'{srm_userpath}megacd',
        'categories': ['SEGA Mega Drive'],
        'short_name': 'megacd',
        'format': 'mamesl', 
        'mode': 'dir', 
        'exec': 'mame', 
        'ini': '~/.mame/mame.ini', 
        'scan_romdir': 'MAME_BASE_DIR_SOFT_DISK/SYSTEM_NAME', 
        'scan_artdir': 'MAME_BASE_DIR_SOFT_ART/SYSTEM_NAME', 
        'data_dir': 'MAME_BASE_DIR_HASH', 
        'soft_lists': '', 
        'working_dir': 'system-working-dir', 
        'extensions': 'zip', 
        'mister_core': 'MegaCD', 
        'extension': 'zip', 
        'cmd': 'GAME_EXEC SYSTEM_NAME ROM_BASENAME'
    },
    { 
        'title': 'SEGA Model 3',
        'srm_romdir': f'{srm_userpath}model3',
        'categories': ['SEGA Model 3'],
        'short_name': 'model3',
        'format': 'generic', 
        'mode': 'file', 
        'exec': './supermodel.sh', 
        'ini': '', 
        'scan_romdir': '/var/lib/freestation/games/SYSTEM_NAME', 
        'scan_artdir': '', 
        'data_dir': '', 
        'soft_lists': '', 
        'working_dir': 'system-working-dir', 
        'extensions': 'zip', 
        'mister_core': 'NONE', 
        'extension': 'zip', 
        'cmd': 'GAME_EXEC -fullscreen -res=1280,720 -legacy3d "ROM_PATH"'
    },
    { 
        'title': 'Sony PlayStation',
        'srm_romdir': f'{srm_userpath}ps1',
        'categories': ['PS1'],
        'short_name': 'psu',
        'format': 'mamesl', 
        'mode': 'file-parent', 
        'exec': '/usr/bin/flatpak run org.duckstation.DuckStation -batch -fullscreen --', 
        'ini': '~/.mame/mame.ini', 
        'scan_romdir': 'MAME_BASE_DIR_SOFT_DISK/SYSTEM_NAME', 
        'scan_artdir': 'MAME_BASE_DIR_SOFT_ART/SYSTEM_NAME', 
        'data_dir': 'system-data-dir', 
        'soft_lists': '', 
        'working_dir': 'system-working-dir', 
        'extensions': 'chd', 
        'mister_core': 'NONE', 
        'extension': 'chd', 
        'cmd': 'GAME_EXEC "ROM_PATH"'
    },
    { 
        'title': 'Sony PlayStation 2',
        'srm_romdir': f'{srm_userpath}ps2',
        'categories': ['PS2'],
        'short_name': 'ps2',
        'format': 'generic', 
        'mode': 'file', 
        'exec': '/usr/local/bin/pcsx2', 
        'ini': '', 
        'scan_romdir': '/var/lib/freestation/games/ps2/dvd', 
        'scan_artdir': 'MAME_BASE_DIR_SOFT_ART/SYSTEM_NAME', 
        'data_dir': 'system-data-dir', 
        'soft_lists': '', 
        'working_dir': 'system-working-dir', 
        'extensions': 'iso', 
        'mister_core': 'NONE', 
        'extension': 'iso', 
        'cmd': 'GAME_EXEC "ROM_PATH"'
    },
    { 
        'title': 'Sony PlayStation 3"',
        'srm_romdir': f'{srm_userpath}ps3',
        'categories': ['PS3'],
        'short_name': 'ps3',
        'format': 'generic', 
        'mode': 'file', 
        'exec': '/usr/local/bin/rpcs3_loopmount', 
        'ini': '', 
        'scan_romdir': '/var/lib/freestation/games/SYSTEM_NAME', 
        'scan_artdir': 'MAME_BASE_DIR_SOFT_ART/SYSTEM_NAME', 
        'data_dir': '', 
        'soft_lists': '', 
        'working_dir': 'system-working-dir', 
        'extensions': 'iso', 
        'mister_core': 'NONE', 
        'extension': 'iso', 
        'cmd': 'GAME_EXEC "ROM_PATH"'
    },
    { 
        'title': 'Super Nintendo',
        'srm_romdir': f'{srm_userpath}snes',
        'categories': ['SNES'],
        'short_name': 'snes',
        'format': 'mamesl', 
        'mode': 'file', 
        'exec': 'mame', 
        'ini': '~/.mame/mame.ini', 
        'scan_romdir': 'MAME_BASE_DIR_SOFT_ROMS/SYSTEM_NAME', 
        'scan_artdir': 'MAME_BASE_DIR_SOFT_ART/SYSTEM_NAME', 
        'data_dir': 'MAME_BASE_DIR_HASH', 
        'soft_lists': '', 
        'working_dir': 'system-working-dir', 
        'extensions': 'zip', 
        'mister_core': 'SNES', 
        'extension': 'zip', 
        'cmd': 'GAME_EXEC SYSTEM_NAME ROM_BASENAME'
    },
    { 
        'title': 'Super Nintendo (PAL)',
        'srm_romdir': f'{srm_userpath}snes',
        'categories': ['SNES'],
        'short_name': 'snespal',
        'format': 'mamesl', 
        'mode': 'file', 
        'exec': 'mame', 
        'ini': '~/.mame/mame.ini', 
        'scan_romdir': 'MAME_BASE_DIR_SOFT_ROMS/SYSTEM_NAME', 
        'scan_artdir': 'MAME_BASE_DIR_SOFT_ART/SYSTEM_NAME', 
        'data_dir': 'MAME_BASE_DIR_HASH', 
        'soft_lists': '', 
        'working_dir': 'system-working-dir', 
        'extensions': 'zip', 
        'mister_core': 'SNES', 
        'extension': 'zip', 
        'cmd': 'GAME_EXEC SYSTEM_NAME ROM_BASENAME'
    },
    { 
        'title': 'SEGA 32X', 
        'srm_romdir': f'{srm_userpath}32x', 
        'categories': ['32X'], 
        'short_name': '32x', 
        'format': 'mamesl', 
        'mode': 'file', 
        'exec': 'mame', 
        'ini': '~/.mame/mame.ini', 
        'scan_romdir': 'MAME_BASE_DIR_SOFT_ROMS/SYSTEM_NAME', 
        'scan_artdir': 'MAME_BASE_DIR_SOFT_ART/SYSTEM_NAME', 
        'data_dir': 'MAME_BASE_DIR_HASH', 
        'soft_lists': '',
        'working_dir': 'system-working-dir', 
        'extensions': 'zip', 
        'mister_core': 'S32X', 
        'extension': 'zip', 
        'cmd': 'GAME_EXEC SYSTEM_NAME ROM_BASENAME',
    },
    { 
        'title': 'SEGA Saturn', 
        'srm_romdir': f'{srm_userpath}saturn', 
        'categories': ['SEGA Saturn'], 
        'short_name': 'saturn', 
        'format': 'mamesl', 
        'mode': 'dir', 
        'exec': 'mame', 
        'ini': '~/.mame/mame.ini', 
        'scan_romdir': 'MAME_BASE_DIR_SOFT_DISK/SYSTEM_NAME', 
        'scan_artdir': 'MAME_BASE_DIR_SOFT_ART/SYSTEM_NAME', 
        'data_dir': 'MAME_BASE_DIR_HASH', 
        'soft_lists': '',
        'working_dir': 'system-working-dir', 
        'extensions': 'zip', 
        'mister_core': 'Saturn', 
        'extension': 'zip', 
        'cmd': 'GAME_EXEC SYSTEM_NAME -cdrom ROM_BASENAME',
    },
    { 
        'title': 'SEGA CD', 
        'srm_romdir': f'{srm_userpath}segacd', 
        'categories': ['SEGA CD'], 
        'short_name': 'segacd', 
        'format': 'mamesl', 
        'mode': 'dir', 
        'exec': 'mame', 
        'ini': '~/.mame/mame.ini', 
        'scan_romdir': 'MAME_BASE_DIR_SOFT_DISK/SYSTEM_NAME', 
        'scan_artdir': 'MAME_BASE_DIR_SOFT_ART/SYSTEM_NAME', 
        'data_dir': 'MAME_BASE_DIR_HASH', 
        'soft_lists': '',
        'working_dir': 'system-working-dir', 
        'extensions': 'zip', 
        'mister_core': 'MegaCD', 
        'extension': 'zip', 
        'cmd': 'GAME_EXEC SYSTEM_NAME ROM_BASENAME',
    },
    { 
        'title': 'PC-Engine', 
        'srm_romdir': f'{srm_userpath}pce', 
        'categories': ['PC-Engine'], 
        'short_name': 'pce', 
        'format': 'mamesl', 
        'mode': 'file', 
        'exec': 'mame', 
        'ini': '~/.mame/mame.ini', 
        'scan_romdir': 'MAME_BASE_DIR_SOFT_ROMS/SYSTEM_NAME', 
        'scan_artdir': 'MAME_BASE_DIR_SOFT_ART/SYSTEM_NAME', 
        'data_dir': 'MAME_BASE_DIR_HASH', 
        'soft_lists': '',
        'working_dir': 'system-working-dir', 
        'extensions': 'zip', 
        'mister_core': 'TGFX16', 
        'extension': 'zip', 
        'cmd': 'GAME_EXEC SYSTEM_NAME ROM_BASENAME',
    },
    { 
        'title': 'PICO-8', 
        'srm_romdir': f'{srm_userpath}pico8', 
        'categories': ['PICO-8'], 
        'short_name': 'pico8', 
        'format': 'pico8', 
        'mode': 'file', 
        'exec': '/usr/local/bin/pico8-launcher', 
        'ini': '', 
        'scan_romdir': '/mnt/roms/Fantasy Console/PICO-8 Carts', 
        'scan_artdir': '/mnt/roms/Fantasy Console/PICO-8 Screenshots ', 
        'data_dir': '/mnt/roms/Fantasy Console/PICO-8 Metadata', 
        'soft_lists': '',
        'working_dir': 'system-working-dir', 
        'extensions': 'zip', 
        'mister_core': 'NONE', 
        'extension': 'zip', 
        'cmd': 'GAME_EXEC "ROM_PATH"',
    },
]

"""
{ 
    'title': '', 
    'srm_romdir': 'f'{srm_userpath}', 
    'categories': [''], 
    'short_name': '', 
    'format': '', 
    'mode': '', 
    'exec': '', 
    'ini': '', 
    'scan_romdir': '', 
    'scan_artdir': '', 
    'data_dir': '', 
    'soft_lists': '', 
    'working_dir':'', 
    'extensions': '', 
    'mister_core': '', 
    'extension': '', 
    'cmd': ''
},
"""

def main():
    srm_configset = []
    scan_configset = []

    outdir = "out"
    try:
        os.mkdir(outdir)
    except:
        pass

    for config in configs:

        # srm
        srm = open('templates/srm-template.json','r')
        srm_data = json.load(srm)
        print(config['title'])
        srm_data['configTitle'] = config['title']
        srm_data['romDirectory'] = config['srm_romdir']
        srm_data['steamCategories'] = config['categories']
        srm_configset.append(srm_data)

        # scan
        scan = open('templates/scan-template.yml','r')
        scan_data = yaml.safe_load(scan)
        scan_data['name'] = config['short_name']
        scan_data['display_name'] = config['title']
        scan_data['format'] = config['format']
        scan_data['mode'] = config['mode']
        scan_data['exec'] = config['exec']
        scan_data['ini'] = config['ini']
        scan_data['rom_dir'] = config['scan_romdir']
        scan_data['art_dir'] = config['scan_artdir']
        scan_data['data_dir'] = config['data_dir']
        scan_data['soft_lists'] = config['soft_lists']
        scan_data['working_dir'] = config['working_dir']
        scan_data['extensions'] = config['extensions']
        scan_data['mister_core'] = config['mister_core']
        scan_data['extension'] = config['extension']
        scan_data['cmd'] = config['cmd']

        # write the individual configs for scan
        fname = scan_data['name']
        with open(f'{outdir}/{fname}.yaml','w') as scan_out:
            yaml.dump(scan_data, scan_out)
 
    # write out the combined config for srm
    with open(f"{outdir}/userConfigurations.json.j2","w") as srm_out:
        json.dump(srm_configset, srm_out, ensure_ascii=True, indent=4, sort_keys=False)

    return


if __name__ == "__main__":
    main()
