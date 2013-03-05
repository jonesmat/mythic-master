# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Oct  8 2012)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class FormMain
###########################################################################

class FormMain ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Mythic Master", pos = wx.DefaultPosition, size = wx.Size( 735,652 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.MINIMIZE_BOX|wx.RESIZE_BORDER|wx.SYSTEM_MENU|wx.CLIP_CHILDREN|wx.TAB_TRAVERSAL )

        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )

        bSizer1 = wx.BoxSizer( wx.VERTICAL )

        self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer5 = wx.BoxSizer( wx.VERTICAL )

        bSizer3 = wx.BoxSizer( wx.HORIZONTAL )

        bSizer2 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText1 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Odds", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
        self.m_staticText1.Wrap( -1 )
        self.m_staticText1.SetFont( wx.Font( 10, 74, 90, 90, True, "Tahoma" ) )

        bSizer2.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.m_btnImpossible = wx.Button( self.m_panel1, wx.ID_ANY, u"Impossible", wx.DefaultPosition, wx.Size( -1,32 ), 0 )
        self.m_btnImpossible.SetFont( wx.Font( 10, 74, 90, 90, False, "Tahoma" ) )

        bSizer2.Add( self.m_btnImpossible, 0, wx.ALL|wx.EXPAND, 5 )

        self.m_btnNoWay = wx.Button( self.m_panel1, wx.ID_ANY, u"No Way", wx.DefaultPosition, wx.Size( -1,33 ), 0 )
        self.m_btnNoWay.SetFont( wx.Font( 10, 74, 90, 90, False, "Tahoma" ) )

        bSizer2.Add( self.m_btnNoWay, 0, wx.ALL|wx.EXPAND, 5 )

        self.m_btnVeryUnlikely = wx.Button( self.m_panel1, wx.ID_ANY, u"Very Unlikely", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_btnVeryUnlikely.SetFont( wx.Font( 10, 74, 90, 90, False, "Tahoma" ) )
        self.m_btnVeryUnlikely.SetMinSize( wx.Size( -1,32 ) )

        bSizer2.Add( self.m_btnVeryUnlikely, 0, wx.ALL|wx.EXPAND, 5 )

        self.m_btnUnlikely = wx.Button( self.m_panel1, wx.ID_ANY, u"Unlikely", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_btnUnlikely.SetFont( wx.Font( 10, 74, 90, 90, False, "Tahoma" ) )
        self.m_btnUnlikely.SetMinSize( wx.Size( -1,33 ) )

        bSizer2.Add( self.m_btnUnlikely, 0, wx.ALL|wx.EXPAND, 5 )

        self.m_btn5050 = wx.Button( self.m_panel1, wx.ID_ANY, u"50 / 50", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_btn5050.SetFont( wx.Font( 10, 74, 90, 90, False, "Tahoma" ) )
        self.m_btn5050.SetMinSize( wx.Size( -1,32 ) )

        bSizer2.Add( self.m_btn5050, 0, wx.ALL|wx.EXPAND, 5 )

        self.m_btnSomewhatLikely = wx.Button( self.m_panel1, wx.ID_ANY, u"Somewhat Likely", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_btnSomewhatLikely.SetFont( wx.Font( 10, 74, 90, 90, False, "Tahoma" ) )
        self.m_btnSomewhatLikely.SetMinSize( wx.Size( -1,33 ) )

        bSizer2.Add( self.m_btnSomewhatLikely, 0, wx.ALL|wx.EXPAND, 5 )

        self.m_btnLikely = wx.Button( self.m_panel1, wx.ID_ANY, u"Likely", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_btnLikely.SetFont( wx.Font( 10, 74, 90, 90, False, "Tahoma" ) )
        self.m_btnLikely.SetMinSize( wx.Size( -1,32 ) )

        bSizer2.Add( self.m_btnLikely, 0, wx.ALL|wx.EXPAND, 5 )

        self.m_btnVeryLikely = wx.Button( self.m_panel1, wx.ID_ANY, u"Very Likely", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_btnVeryLikely.SetFont( wx.Font( 10, 74, 90, 90, False, "Tahoma" ) )
        self.m_btnVeryLikely.SetMinSize( wx.Size( -1,33 ) )

        bSizer2.Add( self.m_btnVeryLikely, 0, wx.ALL|wx.EXPAND, 5 )

        self.m_btnNearSureThing = wx.Button( self.m_panel1, wx.ID_ANY, u"Near Sure Thing", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_btnNearSureThing.SetFont( wx.Font( 10, 74, 90, 90, False, "Tahoma" ) )
        self.m_btnNearSureThing.SetMinSize( wx.Size( -1,32 ) )

        bSizer2.Add( self.m_btnNearSureThing, 0, wx.ALL|wx.EXPAND, 5 )

        self.m_btnSureThing = wx.Button( self.m_panel1, wx.ID_ANY, u"Sure Thing", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_btnSureThing.SetFont( wx.Font( 10, 74, 90, 90, False, "Tahoma" ) )
        self.m_btnSureThing.SetMinSize( wx.Size( -1,33 ) )

        bSizer2.Add( self.m_btnSureThing, 0, wx.ALL|wx.EXPAND, 5 )

        self.m_btnHasToBe = wx.Button( self.m_panel1, wx.ID_ANY, u"Has to Be", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_btnHasToBe.SetFont( wx.Font( 10, 74, 90, 90, False, "Tahoma" ) )
        self.m_btnHasToBe.SetMinSize( wx.Size( -1,32 ) )

        bSizer2.Add( self.m_btnHasToBe, 0, wx.ALL|wx.EXPAND, 5 )


        bSizer3.Add( bSizer2, 0, wx.EXPAND, 5 )

        self.m_staticline1 = wx.StaticLine( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.Size( 2,-1 ), wx.LI_HORIZONTAL )
        bSizer3.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )

        bSizer8 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText2 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Acting Rank", wx.DefaultPosition, wx.Size( -1,16 ), 0 )
        self.m_staticText2.Wrap( -1 )
        self.m_staticText2.SetFont( wx.Font( 10, 74, 90, 90, True, "Tahoma" ) )

        bSizer8.Add( self.m_staticText2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.m_rdoActMiniscule2 = wx.RadioButton( self.m_panel1, wx.ID_ANY, u"Miniscule 2", wx.DefaultPosition, wx.DefaultSize, wx.RB_GROUP )
        self.m_rdoActMiniscule2.SetFont( wx.Font( 10, 74, 90, 90, False, "Tahoma" ) )

        bSizer8.Add( self.m_rdoActMiniscule2, 0, wx.ALL|wx.EXPAND, 10 )

        self.m_rdoActMiniscule = wx.RadioButton( self.m_panel1, wx.ID_ANY, u"Miniscule", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_rdoActMiniscule.SetFont( wx.Font( 10, 74, 90, 90, False, "Tahoma" ) )

        bSizer8.Add( self.m_rdoActMiniscule, 0, wx.ALL|wx.EXPAND, 10 )

        self.m_rdoActWeak = wx.RadioButton( self.m_panel1, wx.ID_ANY, u"Weak", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_rdoActWeak.SetFont( wx.Font( 10, 74, 90, 90, False, "Tahoma" ) )

        bSizer8.Add( self.m_rdoActWeak, 0, wx.ALL|wx.EXPAND, 10 )

        self.m_rdoActLow = wx.RadioButton( self.m_panel1, wx.ID_ANY, u"Low", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_rdoActLow.SetFont( wx.Font( 10, 74, 90, 90, False, "Tahoma" ) )

        bSizer8.Add( self.m_rdoActLow, 0, wx.ALL|wx.EXPAND, 10 )

        self.m_rdoActBelowAvg = wx.RadioButton( self.m_panel1, wx.ID_ANY, u"Below Average", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_rdoActBelowAvg.SetFont( wx.Font( 10, 74, 90, 90, False, "Tahoma" ) )

        bSizer8.Add( self.m_rdoActBelowAvg, 0, wx.ALL|wx.EXPAND, 10 )

        self.m_rdoActAvg = wx.RadioButton( self.m_panel1, wx.ID_ANY, u"Average", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_rdoActAvg.SetValue( True )
        self.m_rdoActAvg.SetFont( wx.Font( 10, 74, 90, 90, False, "Tahoma" ) )

        bSizer8.Add( self.m_rdoActAvg, 0, wx.ALL|wx.EXPAND, 10 )

        self.m_rdoActAboveAvg = wx.RadioButton( self.m_panel1, wx.ID_ANY, u"Above Average", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_rdoActAboveAvg.SetFont( wx.Font( 10, 74, 90, 90, False, "Tahoma" ) )

        bSizer8.Add( self.m_rdoActAboveAvg, 0, wx.ALL|wx.EXPAND, 10 )

        self.m_rdoActHigh = wx.RadioButton( self.m_panel1, wx.ID_ANY, u"High", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_rdoActHigh.SetFont( wx.Font( 10, 74, 90, 90, False, "Tahoma" ) )

        bSizer8.Add( self.m_rdoActHigh, 0, wx.ALL|wx.EXPAND, 10 )

        self.m_rdoActExceptional = wx.RadioButton( self.m_panel1, wx.ID_ANY, u"Exceptional", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_rdoActExceptional.SetFont( wx.Font( 10, 74, 90, 90, False, "Tahoma" ) )

        bSizer8.Add( self.m_rdoActExceptional, 0, wx.ALL|wx.EXPAND, 10 )

        self.m_rdoActIncredible = wx.RadioButton( self.m_panel1, wx.ID_ANY, u"Incredible", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_rdoActIncredible.SetFont( wx.Font( 10, 74, 90, 90, False, "Tahoma" ) )

        bSizer8.Add( self.m_rdoActIncredible, 0, wx.ALL|wx.EXPAND, 10 )

        self.m_rdoActAwesome = wx.RadioButton( self.m_panel1, wx.ID_ANY, u"Awesome", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_rdoActAwesome.SetFont( wx.Font( 10, 74, 90, 90, False, "Tahoma" ) )

        bSizer8.Add( self.m_rdoActAwesome, 0, wx.ALL|wx.EXPAND, 10 )

        self.m_rdoActSuperhuman = wx.RadioButton( self.m_panel1, wx.ID_ANY, u"Superhuman", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_rdoActSuperhuman.SetFont( wx.Font( 10, 74, 90, 90, False, "Tahoma" ) )

        bSizer8.Add( self.m_rdoActSuperhuman, 0, wx.ALL|wx.EXPAND, 10 )

        self.m_rdoActSuperhuman2 = wx.RadioButton( self.m_panel1, wx.ID_ANY, u"Superhuman 2", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_rdoActSuperhuman2.SetFont( wx.Font( 10, 74, 90, 90, False, "Tahoma" ) )

        bSizer8.Add( self.m_rdoActSuperhuman2, 0, wx.ALL|wx.EXPAND, 10 )


        bSizer3.Add( bSizer8, 0, wx.EXPAND, 5 )

        self.m_staticline3 = wx.StaticLine( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.Size( 2,-1 ), wx.LI_HORIZONTAL )
        bSizer3.Add( self.m_staticline3, 0, wx.EXPAND |wx.ALL, 5 )

        bSizer21 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText11 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Difficulty Rank", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText11.Wrap( -1 )
        self.m_staticText11.SetFont( wx.Font( 10, 74, 90, 90, True, "Tahoma" ) )

        bSizer21.Add( self.m_staticText11, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.m_btnDiffMiniscule2 = wx.Button( self.m_panel1, wx.ID_ANY, u"Miniscule 2", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_btnDiffMiniscule2.SetFont( wx.Font( 10, 74, 90, 90, False, "Tahoma" ) )

        bSizer21.Add( self.m_btnDiffMiniscule2, 0, wx.ALL|wx.EXPAND, 5 )

        self.m_btnDiffMiniscule = wx.Button( self.m_panel1, wx.ID_ANY, u"Miniscule", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_btnDiffMiniscule.SetFont( wx.Font( 10, 74, 90, 90, False, "Tahoma" ) )

        bSizer21.Add( self.m_btnDiffMiniscule, 0, wx.ALL|wx.EXPAND, 5 )

        self.m_btnDiffWeak = wx.Button( self.m_panel1, wx.ID_ANY, u"Weak", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_btnDiffWeak.SetFont( wx.Font( 10, 74, 90, 90, False, "Tahoma" ) )

        bSizer21.Add( self.m_btnDiffWeak, 0, wx.ALL|wx.EXPAND, 5 )

        self.m_btnDiffLow = wx.Button( self.m_panel1, wx.ID_ANY, u"Low", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_btnDiffLow.SetFont( wx.Font( 10, 74, 90, 90, False, "Tahoma" ) )

        bSizer21.Add( self.m_btnDiffLow, 0, wx.ALL|wx.EXPAND, 5 )

        self.m_btnDiffBelowAvg = wx.Button( self.m_panel1, wx.ID_ANY, u"Below Average", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_btnDiffBelowAvg.SetFont( wx.Font( 10, 74, 90, 90, False, "Tahoma" ) )

        bSizer21.Add( self.m_btnDiffBelowAvg, 0, wx.ALL|wx.EXPAND, 5 )

        self.m_btnDiffAvg = wx.Button( self.m_panel1, wx.ID_ANY, u"Average", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_btnDiffAvg.SetFont( wx.Font( 10, 74, 90, 90, False, "Tahoma" ) )

        bSizer21.Add( self.m_btnDiffAvg, 0, wx.ALL|wx.EXPAND, 5 )

        self.m_btnDiffAboveAvg = wx.Button( self.m_panel1, wx.ID_ANY, u"Above Average", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_btnDiffAboveAvg.SetFont( wx.Font( 10, 74, 90, 90, False, "Tahoma" ) )

        bSizer21.Add( self.m_btnDiffAboveAvg, 0, wx.ALL|wx.EXPAND, 5 )

        self.m_btnDiffHigh = wx.Button( self.m_panel1, wx.ID_ANY, u"High", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_btnDiffHigh.SetFont( wx.Font( 10, 74, 90, 90, False, "Tahoma" ) )

        bSizer21.Add( self.m_btnDiffHigh, 0, wx.ALL|wx.EXPAND, 5 )

        self.m_btnDiffExceptional = wx.Button( self.m_panel1, wx.ID_ANY, u"Exceptional", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_btnDiffExceptional.SetFont( wx.Font( 10, 74, 90, 90, False, "Tahoma" ) )

        bSizer21.Add( self.m_btnDiffExceptional, 0, wx.ALL|wx.EXPAND, 5 )

        self.m_btnDiffIncredible = wx.Button( self.m_panel1, wx.ID_ANY, u"Incredible", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_btnDiffIncredible.SetFont( wx.Font( 10, 74, 90, 90, False, "Tahoma" ) )

        bSizer21.Add( self.m_btnDiffIncredible, 0, wx.ALL|wx.EXPAND, 5 )

        self.m_btnDiffAwesome = wx.Button( self.m_panel1, wx.ID_ANY, u"Awesome", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_btnDiffAwesome.SetFont( wx.Font( 10, 74, 90, 90, False, "Tahoma" ) )

        bSizer21.Add( self.m_btnDiffAwesome, 0, wx.ALL|wx.EXPAND, 5 )

        self.m_btnDiffSuperhuman = wx.Button( self.m_panel1, wx.ID_ANY, u"Superhuman", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_btnDiffSuperhuman.SetFont( wx.Font( 10, 74, 90, 90, False, "Tahoma" ) )

        bSizer21.Add( self.m_btnDiffSuperhuman, 0, wx.ALL|wx.EXPAND, 5 )

        self.m_btnDiffSuperhuman2 = wx.Button( self.m_panel1, wx.ID_ANY, u"Superhuman 2", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_btnDiffSuperhuman2.SetFont( wx.Font( 10, 74, 90, 90, False, "Tahoma" ) )

        bSizer21.Add( self.m_btnDiffSuperhuman2, 0, wx.ALL|wx.EXPAND, 5 )


        bSizer3.Add( bSizer21, 0, wx.EXPAND, 5 )

        self.m_staticline4 = wx.StaticLine( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.Size( 5,-1 ), wx.LI_HORIZONTAL )
        bSizer3.Add( self.m_staticline4, 0, wx.EXPAND |wx.ALL, 5 )

        bSizer14 = wx.BoxSizer( wx.VERTICAL )

        bSizer15 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText5 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Chaos Rating:", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
        self.m_staticText5.Wrap( -1 )
        self.m_staticText5.SetFont( wx.Font( 10, 74, 90, 90, False, "Tahoma" ) )

        bSizer15.Add( self.m_staticText5, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.m_txtChaos = wx.TextCtrl( self.m_panel1, wx.ID_ANY, u"5", wx.DefaultPosition, wx.Size( 20,-1 ), 0 )
        self.m_txtChaos.SetMaxLength( 1 )
        self.m_txtChaos.SetFont( wx.Font( 10, 74, 90, 90, False, "Tahoma" ) )

        bSizer15.Add( self.m_txtChaos, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer14.Add( bSizer15, 0, wx.EXPAND, 5 )

        self.m_staticline5 = wx.StaticLine( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        bSizer14.Add( self.m_staticline5, 0, wx.EXPAND |wx.ALL, 5 )

        bSizer16 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText13 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Fate Answer:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText13.Wrap( -1 )
        self.m_staticText13.SetFont( wx.Font( 10, 74, 90, 90, False, "Tahoma" ) )

        bSizer16.Add( self.m_staticText13, 0, wx.ALL, 5 )

        self.m_txtFate = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 285,55 ), wx.TE_MULTILINE )
        self.m_txtFate.SetFont( wx.Font( 10, 74, 90, 90, False, "Tahoma" ) )

        bSizer16.Add( self.m_txtFate, 0, wx.ALL, 5 )

        self.m_staticline6 = wx.StaticLine( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        bSizer16.Add( self.m_staticline6, 0, wx.EXPAND |wx.ALL, 5 )

        self.m_btnEvent = wx.Button( self.m_panel1, wx.ID_ANY, u"Roll an Event", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_btnEvent.SetFont( wx.Font( 10, 74, 90, 90, False, "Tahoma" ) )

        bSizer16.Add( self.m_btnEvent, 0, wx.ALL|wx.EXPAND, 5 )

        self.m_txtEvent = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,40 ), wx.TE_MULTILINE )
        self.m_txtEvent.SetFont( wx.Font( 10, 74, 90, 90, False, "Tahoma" ) )

        bSizer16.Add( self.m_txtEvent, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

        self.m_staticline7 = wx.StaticLine( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        bSizer16.Add( self.m_staticline7, 0, wx.EXPAND |wx.ALL, 5 )

        self.m_btnScene = wx.Button( self.m_panel1, wx.ID_ANY, u"Check Scene", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_btnScene.SetFont( wx.Font( 10, 74, 90, 90, False, "Tahoma" ) )

        bSizer16.Add( self.m_btnScene, 0, wx.ALL|wx.EXPAND, 5 )

        self.m_txtScene = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,55 ), wx.TE_MULTILINE )
        self.m_txtScene.SetFont( wx.Font( 10, 74, 90, 90, False, "Tahoma" ) )

        bSizer16.Add( self.m_txtScene, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

        self.m_staticline8 = wx.StaticLine( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        bSizer16.Add( self.m_staticline8, 0, wx.EXPAND |wx.ALL, 5 )

        self.m_btnComplex = wx.Button( self.m_panel1, wx.ID_ANY, u"Ask a Complex Question", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_btnComplex.SetFont( wx.Font( 10, 74, 90, 90, False, "Tahoma" ) )

        bSizer16.Add( self.m_btnComplex, 0, wx.ALL|wx.EXPAND, 5 )

        self.m_txtComplex = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.Point( -1,-1 ), wx.Size( -1,25 ), wx.TE_MULTILINE )
        self.m_txtComplex.SetFont( wx.Font( 10, 74, 90, 90, False, "Tahoma" ) )

        bSizer16.Add( self.m_txtComplex, 0, wx.ALL|wx.EXPAND, 5 )


        bSizer14.Add( bSizer16, 0, wx.EXPAND, 5 )

        fgSizer3 = wx.FlexGridSizer( 0, 2, 0, 0 )
        fgSizer3.SetFlexibleDirection( wx.BOTH )
        fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )


        bSizer14.Add( fgSizer3, 1, wx.EXPAND, 5 )


        bSizer3.Add( bSizer14, 0, wx.EXPAND, 5 )

        fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
        fgSizer1.SetFlexibleDirection( wx.BOTH )
        fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )


        bSizer3.Add( fgSizer1, 0, wx.EXPAND, 5 )


        bSizer5.Add( bSizer3, 0, wx.EXPAND, 5 )

        self.m_staticline2 = wx.StaticLine( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        bSizer5.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )

        bSizer17 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_btnD4 = wx.Button( self.m_panel1, wx.ID_ANY, u"--", wx.DefaultPosition, wx.Size( 60,60 ), 0 )
        self.m_btnD4.SetFont( wx.Font( 20, 74, 90, 90, False, "Tahoma" ) )

        bSizer17.Add( self.m_btnD4, 0, wx.ALL, 5 )

        self.m_btnD6 = wx.Button( self.m_panel1, wx.ID_ANY, u"--", wx.DefaultPosition, wx.Size( 60,60 ), 0 )
        self.m_btnD6.SetFont( wx.Font( 20, 74, 90, 90, False, "Tahoma" ) )

        bSizer17.Add( self.m_btnD6, 0, wx.ALL, 5 )

        self.m_btnD8 = wx.Button( self.m_panel1, wx.ID_ANY, u"--", wx.DefaultPosition, wx.Size( 60,60 ), 0 )
        self.m_btnD8.SetFont( wx.Font( 20, 74, 90, 90, False, "Tahoma" ) )

        bSizer17.Add( self.m_btnD8, 0, wx.ALL, 5 )

        self.m_btnD10 = wx.Button( self.m_panel1, wx.ID_ANY, u"--", wx.DefaultPosition, wx.Size( 60,60 ), 0 )
        self.m_btnD10.SetFont( wx.Font( 20, 74, 90, 90, False, "Tahoma" ) )

        bSizer17.Add( self.m_btnD10, 0, wx.ALL, 5 )

        self.m_btnD12 = wx.Button( self.m_panel1, wx.ID_ANY, u"--", wx.DefaultPosition, wx.Size( 60,60 ), 0 )
        self.m_btnD12.SetFont( wx.Font( 20, 74, 90, 90, False, "Tahoma" ) )

        bSizer17.Add( self.m_btnD12, 0, wx.ALL, 5 )

        self.m_btnD20 = wx.Button( self.m_panel1, wx.ID_ANY, u"--", wx.DefaultPosition, wx.Size( 60,60 ), 0 )
        self.m_btnD20.SetFont( wx.Font( 20, 74, 90, 90, False, "Tahoma" ) )

        bSizer17.Add( self.m_btnD20, 0, wx.ALL, 5 )

        self.m_btnD100 = wx.Button( self.m_panel1, wx.ID_ANY, u"--", wx.DefaultPosition, wx.Size( 60,60 ), 0 )
        self.m_btnD100.SetFont( wx.Font( 20, 74, 90, 90, False, "Tahoma" ) )

        bSizer17.Add( self.m_btnD100, 0, wx.ALL, 5 )


        bSizer5.Add( bSizer17, 0, wx.EXPAND, 5 )

        bSizer13 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText6 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"   4 Sided", wx.Point( -1,-1 ), wx.Size( 60,-1 ), 0 )
        self.m_staticText6.Wrap( -1 )
        self.m_staticText6.SetFont( wx.Font( 8, 74, 90, 92, False, "Tahoma" ) )

        bSizer13.Add( self.m_staticText6, 0, wx.ALL, 5 )

        self.m_staticText7 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"   6 Sided", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
        self.m_staticText7.Wrap( -1 )
        self.m_staticText7.SetFont( wx.Font( 8, 74, 90, 92, False, "Tahoma" ) )

        bSizer13.Add( self.m_staticText7, 0, wx.ALL, 5 )

        self.m_staticText8 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"   8 Sided", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
        self.m_staticText8.Wrap( -1 )
        self.m_staticText8.SetFont( wx.Font( 8, 74, 90, 92, False, "Tahoma" ) )

        bSizer13.Add( self.m_staticText8, 0, wx.ALL, 5 )

        self.m_staticText9 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"  10 Sided", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
        self.m_staticText9.Wrap( -1 )
        self.m_staticText9.SetFont( wx.Font( 8, 74, 90, 92, False, "Tahoma" ) )

        bSizer13.Add( self.m_staticText9, 0, wx.ALL, 5 )

        self.m_staticText10 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"  12 Sided", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
        self.m_staticText10.Wrap( -1 )
        self.m_staticText10.SetFont( wx.Font( 8, 74, 90, 92, False, "Tahoma" ) )

        bSizer13.Add( self.m_staticText10, 0, wx.ALL, 5 )

        self.m_staticText111 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"  20 Sided", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
        self.m_staticText111.Wrap( -1 )
        self.m_staticText111.SetFont( wx.Font( 8, 74, 90, 92, False, "Tahoma" ) )

        bSizer13.Add( self.m_staticText111, 0, wx.ALL, 5 )

        self.m_staticText12 = wx.StaticText( self.m_panel1, wx.ID_ANY, u" 100 Sided", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
        self.m_staticText12.Wrap( -1 )
        self.m_staticText12.SetFont( wx.Font( 8, 74, 90, 92, False, "Tahoma" ) )

        bSizer13.Add( self.m_staticText12, 0, wx.ALL, 5 )


        bSizer5.Add( bSizer13, 0, wx.EXPAND, 5 )

        fgSizer2 = wx.FlexGridSizer( 0, 2, 0, 0 )
        fgSizer2.SetFlexibleDirection( wx.BOTH )
        fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )


        bSizer5.Add( fgSizer2, 1, wx.EXPAND, 5 )


        self.m_panel1.SetSizer( bSizer5 )
        self.m_panel1.Layout()
        bSizer5.Fit( self.m_panel1 )
        bSizer1.Add( self.m_panel1, 1, wx.EXPAND |wx.ALL, 5 )


        self.SetSizer( bSizer1 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.m_btnImpossible.Bind( wx.EVT_BUTTON, self.m_btnImpossibleOnButtonClick )
        self.m_btnNoWay.Bind( wx.EVT_BUTTON, self.m_btnNoWayOnButtonClick )
        self.m_btnVeryUnlikely.Bind( wx.EVT_BUTTON, self.m_btnVeryUnlikelyOnButtonClick )
        self.m_btnUnlikely.Bind( wx.EVT_BUTTON, self.m_btnUnlikelyOnButtonClick )
        self.m_btn5050.Bind( wx.EVT_BUTTON, self.m_btn5050OnButtonClick )
        self.m_btnSomewhatLikely.Bind( wx.EVT_BUTTON, self.m_btnSomewhatLikelyOnButtonClick )
        self.m_btnLikely.Bind( wx.EVT_BUTTON, self.m_btnLikelyOnButtonClick )
        self.m_btnVeryLikely.Bind( wx.EVT_BUTTON, self.m_btnVeryLikelyOnButtonClick )
        self.m_btnNearSureThing.Bind( wx.EVT_BUTTON, self.m_btnNearSureThingOnButtonClick )
        self.m_btnSureThing.Bind( wx.EVT_BUTTON, self.m_btnSureThingOnButtonClick )
        self.m_btnHasToBe.Bind( wx.EVT_BUTTON, self.m_btnHasToBeOnButtonClick )
        self.m_rdoActMiniscule2.Bind( wx.EVT_RADIOBUTTON, self.m_rdoActMiniscule2OnRadioButton )
        self.m_rdoActMiniscule.Bind( wx.EVT_RADIOBUTTON, self.m_rdoActMinisculeOnRadioButton )
        self.m_rdoActWeak.Bind( wx.EVT_RADIOBUTTON, self.m_rdoActWeakOnRadioButton )
        self.m_rdoActLow.Bind( wx.EVT_RADIOBUTTON, self.m_rdoActLowOnRadioButton )
        self.m_rdoActBelowAvg.Bind( wx.EVT_RADIOBUTTON, self.m_rdoActBelowAvgOnRadioButton )
        self.m_rdoActAvg.Bind( wx.EVT_RADIOBUTTON, self.m_rdoActAvgOnRadioButton )
        self.m_rdoActAboveAvg.Bind( wx.EVT_RADIOBUTTON, self.m_rdoActAboveAvgOnRadioButton )
        self.m_rdoActHigh.Bind( wx.EVT_RADIOBUTTON, self.m_rdoActHighOnRadioButton )
        self.m_rdoActExceptional.Bind( wx.EVT_RADIOBUTTON, self.m_rdoActExceptionalOnRadioButton )
        self.m_rdoActIncredible.Bind( wx.EVT_RADIOBUTTON, self.m_rdoActIncredibleOnRadioButton )
        self.m_rdoActAwesome.Bind( wx.EVT_RADIOBUTTON, self.m_rdoActAwesomeOnRadioButton )
        self.m_rdoActSuperhuman.Bind( wx.EVT_RADIOBUTTON, self.m_rdoActSuperhumanOnRadioButton )
        self.m_rdoActSuperhuman2.Bind( wx.EVT_RADIOBUTTON, self.m_rdoActSuperhuman2OnRadioButton )
        self.m_btnDiffMiniscule2.Bind( wx.EVT_BUTTON, self.m_btnDiffMiniscule2OnButtonClick )
        self.m_btnDiffMiniscule.Bind( wx.EVT_BUTTON, self.m_btnDiffMinisculeOnButtonClick )
        self.m_btnDiffWeak.Bind( wx.EVT_BUTTON, self.m_btnDiffWeakOnButtonClick )
        self.m_btnDiffLow.Bind( wx.EVT_BUTTON, self.m_btnDiffLowOnButtonClick )
        self.m_btnDiffBelowAvg.Bind( wx.EVT_BUTTON, self.m_btnDiffBelowAvgOnButtonClick )
        self.m_btnDiffAvg.Bind( wx.EVT_BUTTON, self.m_btnDiffAvgOnButtonClick )
        self.m_btnDiffAboveAvg.Bind( wx.EVT_BUTTON, self.m_btnDiffAboveAvgOnButtonClick )
        self.m_btnDiffHigh.Bind( wx.EVT_BUTTON, self.m_btnDiffHighOnButtonClick )
        self.m_btnDiffExceptional.Bind( wx.EVT_BUTTON, self.m_btnDiffExceptionalOnButtonClick )
        self.m_btnDiffIncredible.Bind( wx.EVT_BUTTON, self.m_btnDiffIncredibleOnButtonClick )
        self.m_btnDiffAwesome.Bind( wx.EVT_BUTTON, self.m_btnDiffAwesomeOnButtonClick )
        self.m_btnDiffSuperhuman.Bind( wx.EVT_BUTTON, self.m_btnDiffSuperhumanOnButtonClick )
        self.m_btnDiffSuperhuman2.Bind( wx.EVT_BUTTON, self.m_btnDiffSuperhuman2OnButtonClick )
        self.m_txtChaos.Bind( wx.EVT_TEXT, self.m_txtChaosOnText )
        self.m_btnEvent.Bind( wx.EVT_BUTTON, self.m_btnEventOnButtonClick )
        self.m_btnScene.Bind( wx.EVT_BUTTON, self.m_btnSceneOnButtonClick )
        self.m_btnComplex.Bind( wx.EVT_BUTTON, self.m_btnComplexOnButtonClick )
        self.m_btnD4.Bind( wx.EVT_BUTTON, self.m_btnD4OnButtonClick )
        self.m_btnD6.Bind( wx.EVT_BUTTON, self.m_btnD6OnButtonClick )
        self.m_btnD8.Bind( wx.EVT_BUTTON, self.m_btnD8OnButtonClick )
        self.m_btnD10.Bind( wx.EVT_BUTTON, self.m_btnD10OnButtonClick )
        self.m_btnD12.Bind( wx.EVT_BUTTON, self.m_btnD12OnButtonClick )
        self.m_btnD20.Bind( wx.EVT_BUTTON, self.m_btnD20OnButtonClick )
        self.m_btnD100.Bind( wx.EVT_BUTTON, self.m_btnD100OnButtonClick )

    def __del__( self ):
        pass


    # Virtual event handlers, overide them in your derived class
    def m_btnImpossibleOnButtonClick( self, event ):
        event.Skip()

    def m_btnNoWayOnButtonClick( self, event ):
        event.Skip()

    def m_btnVeryUnlikelyOnButtonClick( self, event ):
        event.Skip()

    def m_btnUnlikelyOnButtonClick( self, event ):
        event.Skip()

    def m_btn5050OnButtonClick( self, event ):
        event.Skip()

    def m_btnSomewhatLikelyOnButtonClick( self, event ):
        event.Skip()

    def m_btnLikelyOnButtonClick( self, event ):
        event.Skip()

    def m_btnVeryLikelyOnButtonClick( self, event ):
        event.Skip()

    def m_btnNearSureThingOnButtonClick( self, event ):
        event.Skip()

    def m_btnSureThingOnButtonClick( self, event ):
        event.Skip()

    def m_btnHasToBeOnButtonClick( self, event ):
        event.Skip()

    def m_rdoActMiniscule2OnRadioButton( self, event ):
        event.Skip()

    def m_rdoActMinisculeOnRadioButton( self, event ):
        event.Skip()

    def m_rdoActWeakOnRadioButton( self, event ):
        event.Skip()

    def m_rdoActLowOnRadioButton( self, event ):
        event.Skip()

    def m_rdoActBelowAvgOnRadioButton( self, event ):
        event.Skip()

    def m_rdoActAvgOnRadioButton( self, event ):
        event.Skip()

    def m_rdoActAboveAvgOnRadioButton( self, event ):
        event.Skip()

    def m_rdoActHighOnRadioButton( self, event ):
        event.Skip()

    def m_rdoActExceptionalOnRadioButton( self, event ):
        event.Skip()

    def m_rdoActIncredibleOnRadioButton( self, event ):
        event.Skip()

    def m_rdoActAwesomeOnRadioButton( self, event ):
        event.Skip()

    def m_rdoActSuperhumanOnRadioButton( self, event ):
        event.Skip()

    def m_rdoActSuperhuman2OnRadioButton( self, event ):
        event.Skip()

    def m_btnDiffMiniscule2OnButtonClick( self, event ):
        event.Skip()

    def m_btnDiffMinisculeOnButtonClick( self, event ):
        event.Skip()

    def m_btnDiffWeakOnButtonClick( self, event ):
        event.Skip()

    def m_btnDiffLowOnButtonClick( self, event ):
        event.Skip()

    def m_btnDiffBelowAvgOnButtonClick( self, event ):
        event.Skip()

    def m_btnDiffAvgOnButtonClick( self, event ):
        event.Skip()

    def m_btnDiffAboveAvgOnButtonClick( self, event ):
        event.Skip()

    def m_btnDiffHighOnButtonClick( self, event ):
        event.Skip()

    def m_btnDiffExceptionalOnButtonClick( self, event ):
        event.Skip()

    def m_btnDiffIncredibleOnButtonClick( self, event ):
        event.Skip()

    def m_btnDiffAwesomeOnButtonClick( self, event ):
        event.Skip()

    def m_btnDiffSuperhumanOnButtonClick( self, event ):
        event.Skip()

    def m_btnDiffSuperhuman2OnButtonClick( self, event ):
        event.Skip()

    def m_txtChaosOnText( self, event ):
        event.Skip()

    def m_btnEventOnButtonClick( self, event ):
        event.Skip()

    def m_btnSceneOnButtonClick( self, event ):
        event.Skip()

    def m_btnComplexOnButtonClick( self, event ):
        event.Skip()

    def m_btnD4OnButtonClick( self, event ):
        event.Skip()

    def m_btnD6OnButtonClick( self, event ):
        event.Skip()

    def m_btnD8OnButtonClick( self, event ):
        event.Skip()

    def m_btnD10OnButtonClick( self, event ):
        event.Skip()

    def m_btnD12OnButtonClick( self, event ):
        event.Skip()

    def m_btnD20OnButtonClick( self, event ):
        event.Skip()

    def m_btnD100OnButtonClick( self, event ):
        event.Skip()
	

