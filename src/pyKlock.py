###############################################################################################################
#    pyKlock4   Copyright (C) <2025>  <Kevin Scott>                                                           #
#    A klock built using the wxPython framework.                                                              #
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
import src.classes.statusbar as sb

class pyKlock(wx.Frame):
    """  Create pyKlock - shows local time.
    """
    def __init__(self, parent, id, myConfig):

        self.config = myConfig

        pos   = (self.config.X_POS, self.config.Y_POS)
        size  = (self.config.WIDTH, self.config.HEIGHT)
        name  = self.config.NAME

        self.backgroundColour = self.config.DIGITAL_BACKGROUND_COLOUR
        self.foregroundColour = self.config.DIGITAL_FOREGROUND_COLOUR

        style = wx.CAPTION | wx.CLOSE_BOX | wx.STAY_ON_TOP

        wx.Frame.__init__(self, parent, id, name, pos, size, style)

        panel = wx.Panel(self, -1)
        panel.SetBackgroundColour("Black")

        self.bar = sb.StatusBar(self, -1)
        self.SetStatusBar(self.bar)             #  Create the status bar.
        self.selectTime = st.SelectTime()       #  Used to display the time in different formats.
        self.TIME_MODE  = "Local Time"

        width, height = panel.GetSize()
        style    = gizmos.LED_ALIGN_CENTER
        self.led = gizmos.LEDNumberCtrl(panel, -1, (0,0), (width, height), style)

        self.timer = wx.Timer(self, -1)
        # update clock digits every second (1000ms)
        self.timer.Start(1000)
        self.Bind(wx.EVT_TIMER, self.OnTimer)

        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)

        self.led.SetBackgroundColour(self.backgroundColour)
        self.led.SetForegroundColour(self.foregroundColour)

        # Instead we'll just call the SetTransparent method
        #self.SetTransparent(125)

        self.OnTimer(None)

    def OnTimer(self, event):
        """  Called every second - updated the time and the status bar.
        """
        self.led.SetValue(f"{self.selectTime.getTime(self.TIME_MODE)}")

        self.bar.updateStatusBar(self.TIME_MODE)

    def OnCloseWindow(self, event):
        """  close pyKlock at user request.
        """
        x_pos, y_pos  = self.GetPosition()
        width, height = self.GetSize()

        self.config.X_POS  = x_pos
        self.config.Y_POS  = y_pos
        self.config.WIDTH  = width
        self.config.HEIGHT = height

        self.config.DIGITAL_BACKGROUND_COLOUR = self.backgroundColour
        self.config.DIGITAL_FOREGROUND_COLOUR = self.foregroundColour

        self.config.writeConfig()               #  Update config file.

        self.Destroy()



if __name__ == "__main__":
    app = wx.App()
    frame = pyKlock(None, -1)
    frame.Show(True)
    app.SetTopWindow(frame)
    app.MainLoop()
