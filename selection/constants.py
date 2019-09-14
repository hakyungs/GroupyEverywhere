from enum import Enum

class Category(Enum):
    ACTIVITY = "activity"
    STUDY = "study"
    FOOD = "food"

class Activity(Enum):
    
    def list_all(self):
        return


class Food(Enum):
    pass


class College(Enum):
    CFA = "College of Fine Arts"
    CIT = "Carnegie Institute of Technology"
    DC = "Dietrich College of H&SS"
    HC = "Heinz College"
    MCS = "Mellon College of Science"
    SCS = "School of Computer Science"
    TSB = "Tepper School of Business"

    def list_all(self):
        return [self.CFA, self.CIT, self.DC, self.HC, self.MCS, self.SCS, self.TSB]