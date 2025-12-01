###############################################################################################################
#    satatusBar.py   Copyright (C) <2025>  <Kevin Scott>                                                      #
#    A statusbar for klock.                                                                                   #
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

import src.utils.klock_utils as utils

class StatusBar(wx.StatusBar):
    """  A custom class wrapping wx.StatusBar.
    """

    def __init__(self, parent, id):
        """  initialise the status bar.
        """
        wx.StatusBar.__init__(self, parent, id)

        self.SetFieldsCount(number=4)
        self.SetStatusWidths([-4, -2, -1, -2])
        #self.SetStatusStyles(styles=wx.SB_SUNKEN)

        self.SetStatusText("Thursday 20 November 2025", 0)
        self.SetStatusText("L.E.D.", 1)
        self.SetStatusText("cisN", 2)
        self.SetStatusText("idle : 7s", 3)

    def updateStatusBar(self, timeMode):
        """  Updates the status bar.
        """
        strDate = wx.DateTime.Now().Format("%A %d %B %Y")
        self.SetStatusText(f"{strDate}", 0)
        self.SetStatusText(f"{timeMode}", 1)
        self.SetStatusText(f"{utils.getState()}", 2)
        self.SetStatusText(f"{utils.getIdleDuration()}", 3)
