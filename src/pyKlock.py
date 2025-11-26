###############################################################################################################
#    pyKlock4   Copyright (C) <2025>  <Kevin Scott>                                                           #
#    A klock built using the wxPython framework.                    .                                         #
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
import wx.lib.gizmos as gizmos

import src.selectTime as st
import src.utils.klock_utils as utils

class pyKlock(wx.Frame):
    """
    create nice LED clock showing the current time
    """
    def __init__(self, parent, id, myConfig):

        self.config     = myConfig
        pos   = (self.config.X_POS, self.config.Y_POS)
        size  = (self.config.WIDTH, self.config.HEIGHT)
        name  = self.config.NAME
        style = gizmos.LED_ALIGN_CENTER

        wx.Frame.__init__(self, parent, id, name, pos, size)

        self.selectTime = st.SelectTime()
        self.TIME_MODE  = "Local Time"

        self.led = gizmos.LEDNumberCtrl(self, -1, pos, size, style)

        self.timer = wx.Timer(self, -1)
        # update clock digits every second (1000ms)
        self.timer.Start(1000)
        self.Bind(wx.EVT_TIMER, self.OnTimer)

        self.stsBar = self.CreateStatusBar(number=4)
        self.stsBar.SetStatusText("Thursday 20 November 2025", 0)
        self.stsBar.SetStatusText("L.E.D.", 1)
        self.stsBar.SetStatusText("cisN", 2)
        self.stsBar.SetStatusText("idle : 7s", 3)

        self.stsBar.SetStatusWidths([-4, -2, -1, -2])

        # default colours are green on black
        self.led.SetBackgroundColour("Black")
        self.led.SetForegroundColour("Green")

        self.OnTimer(None)

    def OnTimer(self, event):
        self.led.SetValue(f"{self.selectTime.getTime(self.TIME_MODE)}")

        self.updateStatusBar()

    def updateStatusBar(self):
        strDate = wx.DateTime.Now().Format("%A %d %B %Y")
        self.stsBar.SetStatusText(f"{strDate}", 0)
        self.stsBar.SetStatusText(f"{self.TIME_MODE}", 1)
        self.stsBar.SetStatusText(f"{utils.getState()}", 2)
        self.stsBar.SetStatusText(utils.getIdleDuration(), 3)


# test the clock ...
if __name__ == "__main__":
    app = wx.App()
    frame = pyKlock(None, -1)
    frame.Show(True)
    app.SetTopWindow(frame)
    app.MainLoop()
