###############################################################################################################
#    pyKlock3   Copyright (C) <2025>  <Kevin Scott>                                                           #
#                                                                                                             #
#    The Klock displays the time [local], date, key status  and the computers idle time.                      #
#       Key status is the status of Caps Lock, Scroll lock and Num lock.                                      #
#                                                                                                             #
#    To install dependencies pip install -r requirements.txt                                                  #
#                                                                                                             #
#    For changes see history.txt                                                                              #
#                                                                                                             #
###############################################################################################################
#                                                                                                             #
#    This program is free software: you can redistribute it and/or modify it under the terms of the           #
#    GNU General Public License as published by the Free Software Foundation, either Version 3 of the         #
#    License, or (at your option) any later Version.                                                          #
#                                                                                                             #
#    This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without        #
#    even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the               #
#    GNU General Public License for more details.                                                             #
#                                                                                                             #
#    You should have received a copy of the GNU General Public License along with this program.               #
#    If not, see <http://www.gnu.org/licenses/>.                                                              #
#                                                                                                             #
###############################################################################################################

import wx

import platform

import src.pyKlock as pyKlock
import src.config  as Config
import src.logger  as Logger

from src.projectPaths import LOGGER_PATH, CONFIG_PATH

############################################################################################### __main__ ######

if __name__ == "__main__":

    myLogger  = Logger.get_logger(str(LOGGER_PATH))    # Create the logger.

    myLogger.info("-" * 100)

    myConfig  = Config.Config(CONFIG_PATH, myLogger)  # Create the config.

    myLogger.info(f"  Running {myConfig.NAME} Version {myConfig.VERSION} ")
    myLogger.debug(f" {platform.uname()}")
    myLogger.debug(f" Python Version {platform.python_version()}")
    myLogger.debug("")

    myLogger.info(f"  Config path {CONFIG_PATH}")
    myLogger.info(f"  Logger path {LOGGER_PATH}")

    app = wx.App()
    frame = pyKlock.pyKlock(None, -1, myConfig)         #  frame = pyKlock.pyKlock(parent, id, myConfig)
    frame.Show()
    app.MainLoop()

    myLogger.info(f"  Ending {myConfig.NAME} Version {myConfig.VERSION} ")
    myLogger.info("=" * 100)


