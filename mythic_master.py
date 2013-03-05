import wx
from form_main import MythicMasterFormMain


class MythicMaster( wx.App ):
    def __init__(self, redirect=False, filename=None):
        wx.App.__init__(self, redirect, filename)
        self.frame = MythicMasterFormMain( None )
        self.panel = wx.Panel(self.frame, wx.ID_ANY)


if __name__ == "__main__":
    app = MythicMaster()
    app.frame.Show()
    app.MainLoop()
