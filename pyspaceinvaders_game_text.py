# $LastChangedDate: 2009-08-19 20:42:39 -0500 (Wed, 19 Aug 2009) $
# Class for drawing lines of text at appropriate times specific to Space Invaders.
# Author:   Jim Brooks  http://www.jimbrooks.org
# Date:     initial 2004/08, rewritten 2009/08
# License:  GNU General Public License Version 2 (GPL2).
#===============================================================================

from pyspaceinvaders_exception import *
from pyspaceinvaders_conf import *
from pyspaceinvaders_text import *

#-------------------------------------------------------------------------------
# Class for drawing lines of text at appropriate times specific to Space Invaders.
#-------------------------------------------------------------------------------

class GameTextPage:
    """ Class for drawing lines of text at appropriate times specific to Space Invaders. """
    """ The Show() methods don't actually draw text. Rather, Show() add/removes TextLine objects """
    """ from the underlying TextPage object which does the drawing. """

    def __init__( self, game ):
        self.game = game
        self.textPage = TextPage()
        self.showSplash = True
        window = game.window

        # Create text lines.
        # Some are lists of text lines.
        # Some have constant text.
        # Some have dynamic text/attributes that are updated by Draw().
        self.textLineScore    = TextLine( x=4, y=4, color=Color.TEXT )  # dynamic text
        self.textLineLevel    = TextLine( x=36+window.width//3, y=4, color=Color.TEXT, )
        self.textLineLives    = TextLine( x=24+window.width//4*3, y=4, color=Color.ALIVE )
        self.textLineGameOver = TextLine( text="GAME OVER", x=window.width//2, y=224, color=Color.GAME_OVER, center=True )
        x = window.width // 2; y =192  # splash x,y
        self.textLinesSplash = \
           [ TextLine( text="NOISE INVADERS",     x=x, y=y+32*1, color=Color.TEXT, center=True ), \
             TextLine( text="ENTER: START",                  x=x, y=y+32*3, color=Color.TEXT,  center=True ), \
             TextLine( text="LEFT ARROW: LEFT",         x=x, y=y+32*4, color=Color.TEXT,  center=True ), \
             TextLine( text="RIGHT ARROW: RIGHT",        x=x, y=y+32*5, color=Color.TEXT,  center=True ), \
             TextLine( text="SPACE : FIRE",                x=x, y=y+32*6, color=Color.TEXT,  center=True ), \
             TextLine( text="P: PAUSE / HELP",           x=x, y=y+32*7, color=Color.TEXT,  center=True ), \
             TextLine( text="ESC: QUIT",                 x=x, y=y+32*9, color=Color.TEXT,  center=True )  ]

        # Show some text lines.
        self.textPage.Show( self.textLineScore )
        self.textPage.Show( self.textLineLevel )
        self.textPage.Show( self.textLineLives )
        self.ShowSplash( True )  # special-case

    def Show( self, show, textLine ):
        """ (private method) """
        if show:
            self.textPage.Show( textLine )
        else:
            self.textPage.Hide( textLine )
            
    def ShowSplash( self, show=True ):
        self.showSplash = show  # for ToggleHelp()
        for textLine in self.textLinesSplash:
            self.Show( show, textLine )

    def ToggleHelp( self ):
        self.ShowSplash( not self.showSplash )

    def ShowGameOver( self, show=True ):
        self.Show( show, self.textLineGameOver )

    def Draw( self, surface ):
        """ Update and draw lines of text specific to Space Invaders. """
        # Update score.
        self.textLineScore.SetText( "SCORE: " + str(self.game.score) )

        # Update level.
        self.textLineLevel.SetText( "LEVEL: " + str(self.game.level) )

        # Update player's lives.
        if self.game.player.lives > 0:
            self.textLineLives.SetColor( Color.ALIVE )
        else:
            self.textLineLives.SetColor( Color.DEAD )
        self.textLineLives.SetText( "LIVES: " + str(self.game.player.lives) )

        # Now actually draw all text lines (delegate to underlying TextPage).
        self.textPage.Draw( surface )
