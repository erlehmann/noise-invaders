# $LastChangedDate: 2009-08-23 18:40:21 -0500 (Sun, 23 Aug 2009) $
# Configuration.
# Author:   Jim Brooks  http://www.jimbrooks.org
# Date:     initial 2004/08, rewritten 2009/08
# License:  GNU General Public License Version 2 (GPL2).
#===============================================================================

"""Configuration options"""

class Conf():
    """Space Invaders speficic and pygame configurations"""
    # pyspaceinvaders-specific:
    CEILING        = 32
    GROUND_PADDING = 6
    PLAYER_LIVES   = 3

    # pygame:
    WINDOW_WIDTH   = 550
    WINDOW_HEIGHT  = 500
    WINDOW_TITLE   = "Noise Invaders"
    WINDOW_ICON    = "img/icon.png"
    FONT_NAME      = None  # pygame default
    FONT_SIZE      = 40
    TIMER_TICK     = 40

#-------------------------------------------------------------------------------
# Color definitions.
#-------------------------------------------------------------------------------

class Color(object):
    """Color definitions"""
    BG        = (0xff, 0xff, 0xff, 0xff)
    KEY       = (0x00, 0x00, 0xff, 0xff)
    TEXT      = (0xff, 0xff, 0xff, 0xff)
    ALIVE     = (0xff, 0xff, 0xff, 0xff)
    DEAD      = (0xff, 0xff, 0xff, 0xff)
    GAME_OVER = DEAD
    GREEN     = (0x00, 0xff, 0x00, 0xff)
    CYAN      = (0x00, 0xc8, 0xc8, 0xff)
