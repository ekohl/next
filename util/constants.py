CONF_PATH = '~/.next/next.conf'
VIDEO_EXTS = ['.avi', '.mpg', '.mpeg', '.mkv'] #need to have .'s in front!

SHOW_REGEXES = [
    r'.*S0*(?P<season>{season})E0*(?P<ep>{ep}).*',  #accounts for most S12E12 type of shows
    r'.*0*(?P<season>{season})x0*(?P<ep>{ep}).*'    #accounts for most 12x12 type of shows
    ] 

USAGE = """Usage: next [options] [show]

This program helps you in maintaining your episodes. It
will remember which eps you've already seen and start a
new named (or a new random) ep for you. The configuration
file for nextcan be found in ~/.next/
"""

class Keys:
    DB_PATH = 'database_path'
    DB_CONN = 'db_conn'
    SHOW_PATH = 'show_path'
    PLAYER_CMD = 'player_cmd'

class TVRage:
    SEARCH_NAME = 'show/name'
    SEARCH_ID = 'show/showid'

    EPLIST_NAME = 'name'
    EPLIST_SEASONNUM = 'Episodelist/Season/episode/seasonnum'
    EPLIST_EPNUM = 'Episodelist/Season/episode/epnum'
    EPLIST_AIRDATE = 'Episodelist/Season/episode/airdate'
    EPLIST_TITLE = 'Episodelist/Season/episode/title'
