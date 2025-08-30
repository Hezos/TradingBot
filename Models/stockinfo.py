class stockinfo:
    def __init__(self):
        self.Index = 0
    Index = 0
    SandP = 0
    analystrating = 0
    affected = 0
    linearregslope = 0
    linearregline = 0
    levelsupport = 0
    movingaveragecross = 0
    relativestrength = 0
    MACDcross = 0
    bollinger = 0
    EMAsign = 0
    predicted = 0
    actual = 0
    def Dictionary(self,indexV):
        dictvalue = {
            "Index" : indexV,
            "SandP" : self.SandP,
            "analystrating" : self.analystrating,
            "affected" : self.affected,
            "linearregline" : self.linearregline,
            "levelsupport" : self.levelsupport,
            "movingaveragecross" : self.movingaveragecross,
            "relativestrength" : self.relativestrength,
            "MACDcross" : self.MACDcross,
            "bollinger" : self.bollinger,
            "EMAsign" : self.EMAsign
        }
        
        return dictvalue
        