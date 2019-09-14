from enum import Enum

class Category(Enum):
    ACTIVITY = "activity"
    STUDY = "study"
    FOOD = "food"


class College(Enum):
    CFA = "College of Fine Arts"
    CIT = "Carnegie Institute of Technology"
    DC = "Dietrich College of H&SS"
    HC = "Heinz College"
    MCS = "Mellon College of Science"
    SCS = "School of Computer Science"
    TSB = "Tepper School of Business"