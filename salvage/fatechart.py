from random import randint
from collections import OrderedDict


class FateOddsEnum(object):
    """ Mythic Fate Chart Odds Enum """
    IMPOSSIBLE = 0
    NOWAY = 1
    VERYUNLIKELY = 2
    UNLIKELY = 3
    FIFTYFIFTY = 4
    SOMEWHATLIKELY = 5
    LIKELY = 6
    VERYLIKELY = 7
    NEARSURETHING = 8
    ASURETHING = 9
    HASTOBE = 10


class FateRankEnum(object):
    """ Mythic Fate Chart Rank Enum """
    MINISCULE2 = 0
    MINISCULE = 1
    WEAK = 2
    LOW = 3
    BELOWAVERAGE = 4
    AVERAGE = 5
    ABOVEAVERAGE = 6
    HIGH = 7
    EXCEPTIONAL = 8
    INCREDIBLE = 9
    AWESOME = 10
    SUPERHUMAN = 11
    SUPERHUMAN2 = 12


class FateResultEnum(object):
    EXCEPTIONALYES = "Exceptional Yes"
    YES = "Yes"
    NO = "No"
    EXCEPTIONALNO = "Exceptional No"


class FateChart(object):
    def __init__(self):
        super(FateChart, self).__init__()

    odds_chart = {
        FateOddsEnum.IMPOSSIBLE: (
            (0, -20, 77), (0, 0, 81), (0, 0, 81), (1, 5, 82), (1, 5, 82), (2, 10, 83), (3, 15, 84), (5, 25, 86),
            (10, 50, 91)),
        FateOddsEnum.NOWAY: (
            (0, 0, 81), (1, 5, 82), (1, 5, 82), (2, 10, 83), (3, 15, 84), (5, 25, 86), (7, 35, 88), (10, 50, 91),
            (15, 75, 96)),
        FateOddsEnum.VERYUNLIKELY: (
            (1, 5, 82), (1, 5, 82), (2, 10, 83), (3, 15, 84), (5, 25, 86), (9, 45, 90), (10, 50, 91),
            (13, 65, 94), (16, 85, 97)),
        FateOddsEnum.UNLIKELY: (
            (1, 5, 82), (2, 10, 83), (3, 15, 84), (4, 20, 85), (7, 35, 88), (10, 50, 91), (11, 55, 92),
            (15, 75, 96), (18, 90, 99)),
        FateOddsEnum.FIFTYFIFTY: (
            (2, 10, 83), (3, 15, 84), (5, 25, 86), (7, 35, 88), (10, 50, 91), (13, 65, 94), (15, 75, 96),
            (16, 85, 97), (19, 95, 100)),
        FateOddsEnum.SOMEWHATLIKELY: (
            (4, 20, 85), (5, 25, 86), (9, 45, 90), (10, 50, 91), (13, 65, 94), (16, 80, 97), (16, 85, 97),
            (18, 90, 99), (19, 95, 100)),
        FateOddsEnum.LIKELY: (
            (5, 25, 86), (7, 35, 88), (10, 50, 91), (11, 55, 92), (15, 75, 96), (16, 85, 97), (18, 90, 99),
            (19, 95, 100), (20, 100, 999)),
        FateOddsEnum.VERYLIKELY: (
            (9, 45, 90), (10, 50, 91), (13, 65, 94), (15, 75, 96), (16, 85, 97), (18, 90, 99), (19, 95, 100),
            (19, 95, 100), (21, 105, 999)),
        FateOddsEnum.NEARSURETHING: (
            (10, 50, 91), (11, 55, 92), (15, 75, 96), (16, 80, 97), (18, 90, 99), (19, 95, 100), (19, 95, 100),
            (20, 100, 999), (23, 115, 999)),
        FateOddsEnum.ASURETHING: (
            (11, 55, 92), (13, 65, 94), (16, 80, 97), (16, 85, 97), (18, 90, 99), (19, 95, 100), (19, 95, 100),
            (22, 110, 999), (25, 125, 999)),
        FateOddsEnum.HASTOBE: (
            (16, 80, 97), (16, 85, 97), (18, 90, 99), (19, 95, 100), (19, 95, 100), (20, 100, 999), (20, 100, 999),
            (26, 130, 999), (26, 145, 999))
    }

    def roll_odds(self, odds, chaos):
        odds = int(odds)  # type check
        if odds not in range(0, 11):  # odds value must be inclusively within 0...10
            raise TypeError("odds is not a valid value (0...10), use FateOddsEnum")

        chaos = int(chaos)  # type check
        if chaos not in range(1, 10):  # Chaos rank must be inclusively within 1...9
            raise ValueError("Chaos rank is not a valid value (1...9)")

        chaos -= 1  # Shift for zero-based indexing of fate tuple

        # Get fate chart values
        exc_yes_value, yes_no_value, exc_no_value = self.odds_chart[odds][chaos]

        roll_value = randint(1, 100)  # Roll that d100!

        if roll_value <= exc_yes_value:  # Exceptional Yes result!
            result = FateResultEnum.EXCEPTIONALYES
        elif roll_value <= yes_no_value:  # Yes result
            result = FateResultEnum.YES
        elif roll_value >= exc_no_value:  # Exceptional No result!
            result = FateResultEnum.EXCEPTIONALNO
        else:  # otherwise...No
            result = FateResultEnum.NO

        return result, roll_value, (exc_yes_value, yes_no_value, exc_no_value)

    question_chart = {
        FateRankEnum.MINISCULE2: (
            (10, 50, 91), (5, 25, 86), (2, 10, 83), (1, 5, 82), (1, 5, 82), (0, 0, 81), (0, 0, 81), (0, -20, 77),
            (0, -20, 77), (0, -40, 73), (0, -40, 73), (0, -55, 70), (0, -65, 68)),
        FateRankEnum.MINISCULE: (
            (15, 75, 96), (10, 50, 91), (5, 25, 86), (3, 15, 84), (2, 10, 83), (1, 5, 82), (1, 5, 82), (0, 0, 81),
            (0, 0, 81), (0, -20, 77), (0, -20, 77), (0, -35, 74), (0, -45, 72)),
        FateRankEnum.WEAK: (
            (18, 90, 99), (15, 75, 96), (10, 50, 91), (7, 35, 88), (5, 25, 86), (3, 15, 84), (2, 10, 83), (1, 5, 82),
            (1, 5, 82), (0, 0, 81), (0, 0, 81), (0, -15, 78), (0, -25, 76)),
        FateRankEnum.LOW: (
            (19, 95, 100), (16, 85, 97), (13, 65, 94), (10, 50, 91), (9, 45, 90), (5, 25, 86), (3, 15, 84), (2, 10, 83),
            (1, 5, 82), (1, 5, 82), (1, 5, 82), (0, -5, 80), (0, -15, 78)),
        FateRankEnum.BELOWAVERAGE: (
            (20, 100, 999), (18, 90, 99), (15, 75, 96), (11, 55, 92), (10, 50, 91), (7, 35, 88), (4, 20, 85),
            (3, 15, 84), (2, 10, 83), (1, 5, 82), (1, 5, 82), (0, 0, 81), (0, -10, 79)),
        FateRankEnum.AVERAGE: (
            (21, 105, 999), (19, 95, 100), (16, 85, 97), (15, 75, 96), (13, 65, 94), (10, 50, 91), (7, 35, 88),
            (5, 25, 86), (3, 15, 84), (2, 10, 83), (2, 10, 83), (1, 5, 82), (0, -5, 80)),
        FateRankEnum.ABOVEAVERAGE: (
            (22, 110, 999), (19, 95, 100), (18, 90, 99), (16, 85, 97), (16, 80, 97), (13, 65, 94), (10, 50, 91),
            (9, 45, 90), (5, 25, 86), (4, 20, 85), (3, 15, 84), (1, 5, 82), (0, 0, 81)),
        FateRankEnum.HIGH: (
            (23, 115, 999), (20, 100, 999), (19, 95, 100), (18, 90, 99), (16, 85, 97), (15, 75, 96), (11, 55, 92),
            (10, 50, 91), (7, 35, 88), (5, 25, 86), (4, 20, 85), (2, 10, 83), (1, 5, 82)),
        FateRankEnum.EXCEPTIONAL: (
            (24, 120, 999), (21, 105, 999), (19, 95, 100), (19, 95, 100), (18, 90, 99), (16, 85, 97), (15, 75, 96),
            (13, 65, 94), (10, 50, 91), (9, 45, 90), (7, 35, 88), (3, 15, 84), (1, 5, 82)),
        FateRankEnum.INCREDIBLE: (
            (25, 125, 999), (23, 115, 999), (20, 100, 999), (19, 95, 100), (19, 95, 100), (18, 90, 99), (16, 80, 97),
            (15, 75, 96), (11, 55, 92), (10, 50, 91), (9, 45, 90), (4, 20, 85), (2, 10, 83)),
        FateRankEnum.AWESOME: (
            (26, 130, 999), (25, 125, 999), (22, 110, 999), (19, 95, 100), (19, 95, 100), (18, 90, 99), (16, 85, 97),
            (16, 80, 97), (13, 65, 94), (11, 55, 92), (10, 50, 91), (5, 25, 86), (2, 10, 83)),
        FateRankEnum.SUPERHUMAN: (
            (30, 150, 999), (26, 145, 999), (26, 130, 999), (20, 100, 999), (20, 100, 999), (19, 95, 100),
            (19, 95, 100), (18, 90, 99), (16, 85, 97), (16, 80, 97), (15, 75, 96), (10, 50, 91), (5, 25, 86)),
        FateRankEnum.SUPERHUMAN2: (
            (34, 170, 999), (26, 145, 999), (26, 130, 999), (20, 100, 999), (20, 100, 999), (19, 95, 100),
            (19, 95, 100), (18, 90, 99), (16, 85, 97), (16, 80, 97), (18, 90, 99), (15, 75, 96), (10, 50, 91))
    }

    def roll_question(self, acting_rank, difficulty_rank):
        """
        When asking a question against the Mythic Fate Chart you pit an acting rank against a difficulty rank.
        """
        acting_rank = int(acting_rank)  # type check
        if acting_rank not in range(0, 13):  # must be inclusively within 0...12
            raise TypeError("acting rank value is not valid (0...12), use FateRankEnum")

        difficulty_rank = int(difficulty_rank)  # type check
        if difficulty_rank not in range(0, 13):  # rank must be inclusively within 0...12
            raise ValueError("difficulty rank is not a valid value (0...12), use FateRankEnum")

        # Get fate chart values
        exc_yes_value, yes_no_value, exc_no_value = self.question_chart[acting_rank][difficulty_rank]

        roll_value = randint(1, 100)  # Roll that d100!

        if roll_value <= exc_yes_value:  # Exceptional Yes result!
            result = FateResultEnum.EXCEPTIONALYES
        elif roll_value <= yes_no_value:  # Yes result
            result = FateResultEnum.YES
        elif roll_value >= exc_no_value:  # Exceptional No result!
            result = FateResultEnum.EXCEPTIONALNO
        else:  # otherwise...No
            result = FateResultEnum.NO

        # Return (FateResultEnum, Rolled_Int, Fate_Chart_Values_Tuple )
        return result, roll_value, (exc_yes_value, yes_no_value, exc_no_value)

    event_focus_unordered = {
        7: "Remote event",
        28: "NPC action",
        35: "New NPC",
        45: "Move toward a thread",
        52: "Move away from a thread",
        55: "Close a thread",
        67: "PC negative",
        75: "PC positive",
        83: "Ambiguous event",
        92: "NPC negative",
        100: "NPC positive"
    }
    # Create the event focus table as an ordered dict, ordered by key.
    event_focus = OrderedDict(sorted(event_focus_unordered.items(), key=lambda t: t[0]))

    event_action = (
        "Attainment", "Starting", "Neglect", "Fight", "Recruit", "Triumph",
        "Violate", "Oppose", "Malice", "Communicate", "Persecute", "Increase",
        "Decrease", "Abandon", "Gratify", "Inquire", "Antagonise", "Move",
        "Waste", "Truce", "Release", "Befriend", "Judge", "Desert",
        "Dominate", "Procrastinate", "Praise", "Separate", "Take", "Break",
        "Heal", "Delay", "Stop", "Lie", "Return", "Immitate", "Struggle",
        "Inform", "Bestow", "Postpone", "Expose", "Haggle", "Imprison",
        "Release", "Celebrate", "Develop", "Travel", "Block", "Harm",
        "Debase", "Overindulge", "Adjourn", "Adversity", "Kill", "Disrupt",
        "Usurp", "Create", "Betray", "Agree", "Abuse", "Oppress", "Inspect",
        "Ambush", "Spy", "Attach", "Carry", "Open", "Carelessness", "Ruin",
        "Extravagance", "Trick", "Arrive", "Propose", "Divide", "Refuse",
        "Mistrust", "Deceive", "Cruelty", "Intolerance", "Trust",
        "Excitement", "Activity", "Assist", "Care", "Negligence", "Passion",
        "Work hard", "Control", "Attract", "Failure", "Pursue", "Vengeance",
        "Proceedings", "Dispute", "Punish", "Guide", "Transform", "Overthrow",
        "Oppress", "Change"
    )

    event_subject = (
        "Goals", "Dreams", "Environment", "Outside", "Inside", "Reality",
        "Allies", "Enemies", "Evil", "Good", "Emotions", "Opposition", "War",
        "Peace", "The innocent", "Love", "The spiritual", "The intellectual",
        "New ideas", "Joy", "Messages", "Energy", "Balance", "Tension",
        "Friendship", "The physical", "A project", "Pleasures", "Pain",
        "Possessions", "Benefits", "Plans", "Lies", "Expectations",
        "Legal matters", "Bureaucracy", "Business", "A path", "News",
        "Exterior factors", "Advice", "A plot", "Competition", "Prison",
        "Illness", "Food", "Attention", "Success", "Failure", "Travel",
        "Jealousy", "Dispute", "Home", "Investment", "Suffering", "Wishes",
        "Tactics", "Stalemate", "Randomness", "Misfortune", "Death",
        "Disruption", "Power", "A burden", "Intrigues", "Fears", "Ambush",
        "Rumor", "Wounds", "Extravagance", "A representative", "Adversities",
        "Opulence", "Liberty", "Military", "The mundane", "Trials", "Masses",
        "Vehicle", "Art", "Victory", "Dispute", "Riches", "Status quo",
        "Technology", "Hope", "Magic", "Illusions", "Portals", "Danger",
        "Weapons", "Animals", "Weather", "Elements", "Nature", "The public",
        "Leadership", "Fame", "Anger", "Information"
    )

    def roll_event(self):
        """
        Rolls an Event using the Mythic event generation system which encompasses the event focus, action, and subject.

        :return (focus, action, subject):
        """
        # Get the event focus
        roll_value = randint(1, 100)  # Roll that d100!
        focus = None
        for item in self.event_focus.items():
            focus_threshold = item[0]
            if roll_value <= focus_threshold:
                focus = item[1]
                break

        # Get the event action
        roll_value = randint(0, 99)  # Roll that zero-based d100!
        action = self.event_action[roll_value]

        # Get the event subject
        roll_value = randint(0, 99)  # Roll that zero-based d100!
        subject = self.event_subject[roll_value]

        return focus, action, subject
