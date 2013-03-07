"""Subclass of FormMain, which is generated by wxFormBuilder."""

import generated_forms
from fatechart import FateChart, FateOddsEnum, FateRankEnum
from random import randint


class MythicMasterFormMain(generated_forms.FormMain):
    def __init__(self, parent):
        generated_forms.FormMain.__init__(self, parent)
        self.fate = FateChart()
        self.acting_rank = FateRankEnum.AVERAGE

    # Handlers for FormMain events.

    def _get_odds_text_value(self, odds):
        chaos_value = int(self.m_txtChaos.GetValue())

        result, roll_value, bounds = self.fate.roll_odds(odds, chaos_value)
        new_value = "(%d -- %d/%d/%d) %s\r\n" % (roll_value, bounds[0], bounds[1], bounds[2], result)

        if roll_value % 11 == 0 and roll_value / 11 <= chaos_value:
            # Random event occurred!!!
            focus, action, subject = self.fate.roll_event()
            new_value += "Event Occurred!  %s:\r\n%s [of] %s\r\n---\r\n" % (focus, action, subject)
        else:
            new_value += "\r\n\r\n---\r\n"

        return new_value

    def m_btnImpossibleOnButtonClick(self, event):
        new_value = self._get_odds_text_value(FateOddsEnum.IMPOSSIBLE)
        existing_value = self.m_txtFate.GetValue()
        new_value += existing_value[0:1000]  # Append the recent fate history
        self.m_txtFate.SetValue(new_value)

    def m_btnNoWayOnButtonClick(self, event):
        new_value = self._get_odds_text_value(FateOddsEnum.NOWAY)
        existing_value = self.m_txtFate.GetValue()
        new_value += existing_value[0:1000]  # Append the recent fate history
        self.m_txtFate.SetValue(new_value)

    def m_btnVeryUnlikelyOnButtonClick(self, event):
        new_value = self._get_odds_text_value(FateOddsEnum.VERYUNLIKELY)
        existing_value = self.m_txtFate.GetValue()
        new_value += existing_value[0:1000]  # Append the recent fate history
        self.m_txtFate.SetValue(new_value)

    def m_btnUnlikelyOnButtonClick(self, event):
        new_value = self._get_odds_text_value(FateOddsEnum.UNLIKELY)
        existing_value = self.m_txtFate.GetValue()
        new_value += existing_value[0:1000]  # Append the recent fate history
        self.m_txtFate.SetValue(new_value)

    def m_btn5050OnButtonClick(self, event):
        new_value = self._get_odds_text_value(FateOddsEnum.FIFTYFIFTY)
        existing_value = self.m_txtFate.GetValue()
        new_value += existing_value[0:1000]  # Append the recent fate history
        self.m_txtFate.SetValue(new_value)

    def m_btnSomewhatLikelyOnButtonClick(self, event):
        new_value = self._get_odds_text_value(FateOddsEnum.SOMEWHATLIKELY)
        existing_value = self.m_txtFate.GetValue()
        new_value += existing_value[0:1000]  # Append the recent fate history
        self.m_txtFate.SetValue(new_value)

    def m_btnLikelyOnButtonClick(self, event):
        new_value = self._get_odds_text_value(FateOddsEnum.LIKELY)
        existing_value = self.m_txtFate.GetValue()
        new_value += existing_value[0:1000]  # Append the recent fate history
        self.m_txtFate.SetValue(new_value)

    def m_btnVeryLikelyOnButtonClick(self, event):
        new_value = self._get_odds_text_value(FateOddsEnum.VERYLIKELY)
        existing_value = self.m_txtFate.GetValue()
        new_value += existing_value[0:1000]  # Append the recent fate history
        self.m_txtFate.SetValue(new_value)

    def m_btnNearSureThingOnButtonClick(self, event):
        new_value = self._get_odds_text_value(FateOddsEnum.NEARSURETHING)
        existing_value = self.m_txtFate.GetValue()
        new_value += existing_value[0:1000]  # Append the recent fate history
        self.m_txtFate.SetValue(new_value)

    def m_btnSureThingOnButtonClick(self, event):
        new_value = self._get_odds_text_value(FateOddsEnum.ASURETHING)
        existing_value = self.m_txtFate.GetValue()
        new_value += existing_value[0:1000]  # Append the recent fate history
        self.m_txtFate.SetValue(new_value)

    def m_btnHasToBeOnButtonClick(self, event):
        new_value = self._get_odds_text_value(FateOddsEnum.HASTOBE)
        existing_value = self.m_txtFate.GetValue()
        new_value += existing_value[0:1000]  # Append the recent fate history
        self.m_txtFate.SetValue(new_value)

    def m_rdoActMiniscule2OnRadioButton(self, event):
        self.acting_rank = FateRankEnum.MINISCULE2

    def m_rdoActMinisculeOnRadioButton(self, event):
        self.acting_rank = FateRankEnum.MINISCULE

    def m_rdoActWeakOnRadioButton(self, event):
        self.acting_rank = FateRankEnum.WEAK

    def m_rdoActLowOnRadioButton(self, event):
        self.acting_rank = FateRankEnum.LOW

    def m_rdoActBelowAvgOnRadioButton(self, event):
        self.acting_rank = FateRankEnum.BELOWAVERAGE

    def m_rdoActAvgOnRadioButton(self, event):
        self.acting_rank = FateRankEnum.AVERAGE

    def m_rdoActAboveAvgOnRadioButton(self, event):
        self.acting_rank = FateRankEnum.ABOVEAVERAGE

    def m_rdoActHighOnRadioButton(self, event):
        self.acting_rank = FateRankEnum.HIGH

    def m_rdoActExceptionalOnRadioButton(self, event):
        self.acting_rank = FateRankEnum.EXCEPTIONAL

    def m_rdoActIncredibleOnRadioButton(self, event):
        self.acting_rank = FateRankEnum.INCREDIBLE

    def m_rdoActAwesomeOnRadioButton(self, event):
        self.acting_rank = FateRankEnum.AWESOME

    def m_rdoActSuperhumanOnRadioButton(self, event):
        self.acting_rank = FateRankEnum.SUPERHUMAN

    def m_rdoActSuperhuman2OnRadioButton(self, event):
        self.acting_rank = FateRankEnum.SUPERHUMAN2

    def _get_rank_text_value(self, acting_rank, difficulty_rank):
        result, roll_value, bounds = self.fate.roll_question(acting_rank, difficulty_rank)
        new_value = "(%d -- %d/%d/%d) %s\r\n" % (roll_value, bounds[0], bounds[1], bounds[2], result)

        chaos_value = int(self.m_txtChaos.GetValue())
        if roll_value % 11 == 0 and roll_value / 11 <= chaos_value:
            # Random event occurred!!!
            focus, action, subject = self.fate.roll_event()
            new_value += "Event Occurred!  %s:\r\n%s [of] %s\r\n---\r\n" % (focus, action, subject)
        else:
            new_value += "\r\n\r\n---\r\n"

        return new_value

    def m_btnDiffMiniscule2OnButtonClick(self, event):
        new_value = self._get_rank_text_value(self.acting_rank, FateRankEnum.MINISCULE2)
        existing_value = self.m_txtFate.GetValue()
        new_value += existing_value[0:1000]  # Append the recent fate history
        self.m_txtFate.SetValue(new_value)

    def m_btnDiffMinisculeOnButtonClick(self, event):
        new_value = self._get_rank_text_value(self.acting_rank, FateRankEnum.MINISCULE)
        existing_value = self.m_txtFate.GetValue()
        new_value += existing_value[0:1000]  # Append the recent fate history
        self.m_txtFate.SetValue(new_value)

    def m_btnDiffWeakOnButtonClick(self, event):
        new_value = self._get_rank_text_value(self.acting_rank, FateRankEnum.WEAK)
        existing_value = self.m_txtFate.GetValue()
        new_value += existing_value[0:1000]  # Append the recent fate history
        self.m_txtFate.SetValue(new_value)

    def m_btnDiffLowOnButtonClick(self, event):
        new_value = self._get_rank_text_value(self.acting_rank, FateRankEnum.LOW)
        existing_value = self.m_txtFate.GetValue()
        new_value += existing_value[0:1000]  # Append the recent fate history
        self.m_txtFate.SetValue(new_value)

    def m_btnDiffBelowAvgOnButtonClick(self, event):
        new_value = self._get_rank_text_value(self.acting_rank, FateRankEnum.BELOWAVERAGE)
        existing_value = self.m_txtFate.GetValue()
        new_value += existing_value[0:1000]  # Append the recent fate history
        self.m_txtFate.SetValue(new_value)

    def m_btnDiffAvgOnButtonClick(self, event):
        new_value = self._get_rank_text_value(self.acting_rank, FateRankEnum.AVERAGE)
        existing_value = self.m_txtFate.GetValue()
        new_value += existing_value[0:1000]  # Append the recent fate history
        self.m_txtFate.SetValue(new_value)

    def m_btnDiffAboveAvgOnButtonClick(self, event):
        new_value = self._get_rank_text_value(self.acting_rank, FateRankEnum.ABOVEAVERAGE)
        existing_value = self.m_txtFate.GetValue()
        new_value += existing_value[0:1000]  # Append the recent fate history
        self.m_txtFate.SetValue(new_value)

    def m_btnDiffHighOnButtonClick(self, event):
        new_value = self._get_rank_text_value(self.acting_rank, FateRankEnum.HIGH)
        existing_value = self.m_txtFate.GetValue()
        new_value += existing_value[0:1000]  # Append the recent fate history
        self.m_txtFate.SetValue(new_value)

    def m_btnDiffExceptionalOnButtonClick(self, event):
        new_value = self._get_rank_text_value(self.acting_rank, FateRankEnum.EXCEPTIONAL)
        existing_value = self.m_txtFate.GetValue()
        new_value += existing_value[0:1000]  # Append the recent fate history
        self.m_txtFate.SetValue(new_value)

    def m_btnDiffIncredibleOnButtonClick(self, event):
        new_value = self._get_rank_text_value(self.acting_rank, FateRankEnum.INCREDIBLE)
        existing_value = self.m_txtFate.GetValue()
        new_value += existing_value[0:1000]  # Append the recent fate history
        self.m_txtFate.SetValue(new_value)

    def m_btnDiffAwesomeOnButtonClick(self, event):
        new_value = self._get_rank_text_value(self.acting_rank, FateRankEnum.AWESOME)
        existing_value = self.m_txtFate.GetValue()
        new_value += existing_value[0:1000]  # Append the recent fate history
        self.m_txtFate.SetValue(new_value)

    def m_btnDiffSuperhumanOnButtonClick(self, event):
        new_value = self._get_rank_text_value(self.acting_rank, FateRankEnum.SUPERHUMAN)
        existing_value = self.m_txtFate.GetValue()
        new_value += existing_value[0:1000]  # Append the recent fate history
        self.m_txtFate.SetValue(new_value)

    def m_btnDiffSuperhuman2OnButtonClick(self, event):
        new_value = self._get_rank_text_value(self.acting_rank, FateRankEnum.SUPERHUMAN2)
        existing_value = self.m_txtFate.GetValue()
        new_value += existing_value[0:1000]  # Append the recent fate history
        self.m_txtFate.SetValue(new_value)

    def m_txtChaosOnText(self, event):
        try:
            int(self.m_txtChaos.GetValue())
        except ValueError:
            self.m_txtChaos.Undo()

    def m_btnEventOnButtonClick(self, event):
        focus, action, subject = self.fate.roll_event()
        new_value = "%s:\r\n%s [of] %s\r\n---\r\n" % (focus, action, subject)

        existing_value = self.m_txtEvent.GetValue()
        new_value += existing_value[0:1000]  # Append the recent event history

        self.m_txtEvent.SetValue(new_value)

    def m_btnSceneOnButtonClick(self, event):
        scene_roll = randint(1, 10)
        if scene_roll <= int(self.m_txtChaos.GetValue()):
            if scene_roll % 2 == 1:  # Odd indicates an altered scene
                new_value = "Scene is altered (rolled %d):\r\nProceed with the next logical scene\r\n\r\n" % scene_roll
            else:  # Even indicates an interrupted scene
                focus, action, subject = self.fate.roll_event()
                new_value = "Scene is interrupted:\r\n%s:\r\n%s [of] %s\r\n" % (focus, action, subject)
        else:  # Unaltered scene
            new_value = "Scene proceeds as expected (rolled %d)\r\n\r\n\r\n" % scene_roll

        new_value += "---\r\n"

        existing_value = self.m_txtScene.GetValue()
        new_value += existing_value[0:1000]  # Append the recent scene history

        self.m_txtScene.SetValue(new_value)

    def m_btnComplexOnButtonClick(self, event):
        focus, action, subject = self.fate.roll_event()
        new_value = "%s [of] %s\r\n---\r\n" % (action, subject)

        existing_value = self.m_txtComplex.GetValue()
        new_value += existing_value[0:1000]  # Append the recent question history

        self.m_txtComplex.SetValue(new_value)

    def _roll_die(self, size):
        roll = str(randint(1, size))
        new_value = "d%-3d : %2s\r\n" % (size, roll)
        existing_value = self.m_textRolls.GetValue()
        new_value += existing_value[0:1000]  # Append the die roll history
        self.m_textRolls.SetValue(new_value)
        return roll
        
    def m_btnD4OnButtonClick(self, event):
        roll = self._roll_die(4)
        self.m_btnD4.SetLabel(str(roll))

    def m_btnD6OnButtonClick(self, event):
        roll = self._roll_die(6)
        self.m_btnD6.SetLabel(str(roll))

    def m_btnD8OnButtonClick(self, event):
        roll = self._roll_die(8)
        self.m_btnD8.SetLabel(str(roll))

    def m_btnD10OnButtonClick(self, event):
        roll = self._roll_die(10)
        self.m_btnD10.SetLabel(str(roll))

    def m_btnD12OnButtonClick(self, event):
        roll = self._roll_die(12)
        self.m_btnD12.SetLabel(str(roll))

    def m_btnD20OnButtonClick(self, event):
        roll = self._roll_die(20)
        self.m_btnD20.SetLabel(str(roll))

    def m_btnD100OnButtonClick(self, event):
        roll = self._roll_die(100)
        self.m_btnD100.SetLabel(str(roll))
