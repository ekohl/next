import re

CONF_PATH = '~/.next/next.conf'
VIDEO_EXTS = ['.avi', '.mpg', '.mpeg', '.mkv'] #need to have .'s in front!
SHOW_REGEXES = [r'.*S0*{season}E0*{ep}.*', #accounts for most S12E12 type of shows
                r'.*0*{season}x0*{ep}.*'] #accounts for most 12x12 type of shows

USAGE = \
        """Usage: %prog [options] [show]

This program helps you in maintaining your episodes. It
will remember which eps you've already seen and start a
new named (or a new random) ep for you. The configuration
file for %prog can be found in ~/.%prog/
"""

class Keys:
    DB_PATH = 'database_path'
    SHOW_PATH = 'show_path'
    PLAYER_CMD = 'player_cmd'

