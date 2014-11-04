def convert_str_to_list(str):
    list = []
    for char in str:
        list.append(char)
    return list

def convert_list_to_str(list):
    str = ""
    for index in range(len(list)):
        str += list[index]
    return str

def remove(baseStr,rmStr):
    baseList = convert_str_to_list(baseStr)
    rmList = convert_str_to_list(rmStr)
    for elem in rmList:
        baseList.remove(elem)
    return convert_list_to_str(baseList)

def sublist(sublist,superlist):
    '''Seriously, I think this might already be a method.'''
    for elem1 in sublist:
        if elem1 not in superlist:
            return False
        
def extend(list1,list2):
    list_str = convert_list_to_str(list1)
    l = list1.copy()
    for elem in list2:
        l.append(elem)
    l1 = convert_str_to_list(list_str)
    return l

class Propos:
    '''Class for a categorical proposition from the Aristotelian standpoint.'''

    def __init__(self,sub,pred,lettype,tVal):
        '''__init__(str,str,str,bool) -> Propos
           Propositon constructor. Takes the subject, predicate, categorical proposition type, and truth value.'''
        self.sub = sub
        self.pred = pred
        if lettype != "A" and lettype != "I" and lettype != "E" and lettype != "O":
            print('''You cannot have a proposition with type '''+str(lettype)+'.')
            raise TypeError
        else:
            self.lettype = lettype
        self.tVal = tVal

    def __str__(self):
        '''Propos.__str__() -> str
           Class printer. Will put "F" in front of the proposition if it is false.'''
        if self.tVal == True:
            outStr = ""
            if self.lettype == "A":
                outStr+= "All " + str(self.sub) + " are " + str(self.pred)
            elif self.lettype == "I":
                outStr+= "Some " + str(self.sub) + " are " + str(self.pred)
            elif self.lettype == "E":
                outStr+= "No " + str(self.sub) + " are " + str(self.pred)
            else:
                outStr+= "Some " + str(self.sub) + " are not " + str(self.pred)
        else:
            outStr = "F "
            if self.lettype == "A":
                outStr+= "All " + str(self.sub) + " are " + str(self.pred)
            elif self.lettype == "I":
                outStr+= "Some " + str(self.sub) + " are " + str(self.pred)
            elif self.lettype == "E":
                outStr+= "No " + str(self.sub) + " are " + str(self.pred)
            else:
                outStr+= "Some " + str(self.sub) + " are not " + str(self.pred)
            
        return outStr

    def getEngName(self):
        '''Propos.getEngName() -> str
           Same as __str__, but ignores truth.'''
        outStr = ""
        if self.lettype == "A":
            outStr+= "All " + str(self.sub) + " are " + str(self.pred)
        elif self.lettype == "I":
            outStr+= "Some " + str(self.sub) + " are " + str(self.pred)
        elif self.lettype == "E":
            outStr+= "No " + str(self.sub) + " are " + str(self.pred)
        else:
            outStr+= "Some " + str(self.sub) + " are not " + str(self.pred)
        return outStr


    def getQuantity(self):
        '''Propos.getQuantity() -> str
           Prints quantity of proposition.'''
        if self.lettype == "A" or self.lettype == "E":
            return "universal"
        else:
            return "particular"

    def getQuality(self):
        '''Propos.getQuality() -> str
           Prints quality of proposition.'''
        if self.lettype == "A" or self.lettype == "I":
            return "affirmative"
        else:
            return "negative"

    def getTermsDist(self):
        '''Propos.getTermsDist() -> list
           Lists the terms distributed by the propositon.'''
        if self.lettype == "A":
            return [self.sub]
        elif self.lettype == "I":
            return [None]
        elif self.lettype == "E":
            return [self.sub,self.pred]
        else:
            return [self.pred]

    def chgQuantity(self):
        '''Propos.chgQuantity() -> None
           Changes the quantifier of the proposition.'''
        if self.lettype == "A":
            self.lettype = "I"
        elif self.lettype == "E":
            self.lettype = "0"
        elif self.lettype == "I":
            self.lettype = "A"
        elif self.lettype == "O":
            self.lettype = "E"

    def chgQuality(self):
        '''Propos.chgQuality() -> None
           Changes the quality of the proposition.'''
        if self.lettype == "A":
            self.lettype = "E"
        elif self.lettype == "E":
            self.lettype = "A"
        elif self.lettype == "I":
            self.lettype = "O"
        elif self.lettype == "O":
            self.lettype = "I"

    def contrary(self):
        '''Propos.contrary() -> None
           Performs Aristotelian contrary on the propositon.
           If proposition does not satisfy the conditions, returns "Illicit contrary."'''
        if self.lettype == "A" and self.tVal:
            self.tVal = False
            self.lettype = "E"

        elif self.lettype == "E" and self.tVal:
            self.tVal = False
            self.lettype = "A"
        else:
            return "Illicit contrary."

    def subalt(self):
        '''Propos.subalt() -> None
           Performs Aristotelian subalternation on the propositon.
           If proposition does not satisfy the conditions, returns "Illicit subalternation."'''
        if self.lettype == "A" and self.tVal:
            self.lettype = "I"
        elif self.lettype == "I" and not self.tVal:
            self.lettype = "A"
        elif self.lettype == "E" and self.tVal:
            self.lettype = "O"
        elif self.lettype == "O" and not self.tVal:
            self.lettype = "E"
        else:
            return "Illicit subalternation."

    def subcontrary(self):
        '''Propos.subcontrary() -> None
           Performs Aristotelian subcontrary on the propositon.
           If proposition does not satisfy the conditions, returns "Illicit subcontrary."'''
        if self.lettype == "I" and not self.tVal:
            self.tVal = True
            self.lettype = "O"

        elif self.lettype == "O" and not self.tVal:
            self.tVal = True
            self.lettype = "I"

        else:
            return "Illicit subcontrary."

    def contradictory(self):
        '''Propos.chgQuality() -> None
           Performs contradiction on the propositon.'''
        if self.lettype == "A" and self.tVal:
            self.lettype = "O"
            self.tVal = False
        elif self.lettype == "A" and not self.tVal:
            self.lettype = "O"
            self.tVal = True
        elif self.lettype == "O" and self.tVal:
            self.lettype = "A"
            self.tVal = False
        elif self.lettype == "O" and not self.tVal:
            self.lettype = "A"
            self.tVal = True
        elif self.lettype == "E" and self.tVal:
            self.lettype = "I"
            self.tVal = False
        elif self.lettype == "E" and not self.tVal:
            self.lettype = "I"
            self.tVal = True
        elif self.lettype == "I" and self.tVal:
            self.lettype = "E"
            self.tVal = False
        elif self.lettype == "I" and not self.tVal:
            self.lettype = "E"
            self.tVal = True
            
    def convert(self):
        '''Propos.convert() -> None
           Performs conversion on the propositon.
           If proposition does not satisfy the conditions, returns "Illicit conversion."'''
        if self.lettype == "A" or self.lettype == "O":
            return "Illicit conversion."
        else:
            subBak= self.sub
            self.sub = self.pred
            self.pred = subBak

    def obvert(self):
       '''Propos.obvert() -> None
           Performs obversion on the propositon.'''
       self.chgQuality()
       if not ("non-" in self.pred):
           self.pred = "non-" + self.pred 
       elif ("non-" in self.pred):
           self.pred = remove(self.pred,"non-")        

    def contrapose(self):
        '''Propos.contrapose() -> None
           Performs contradiction on the propositon.
           If proposition does not satisfy the conditions, returns "Illicit contraposition."'''
        if self.lettype == "E" or self.lettype == "I":
            return "Illicit contraposition."
        else:
            if not ("non-" in self.sub) and not ("non-" in self.pred):
                subBak = self.sub
                self.sub = "non-" + self.pred
                self.pred = "non-" + subBak
            elif not ("non-" in self.sub) and ("non-" in self.pred):
                self.sub = "non-" + self.sub
                self.pred = remove(self.pred,"non-")
                subBak = self.sub
                self.sub = self.pred
                self.pred = subBak

            elif ("non-" in self.sub) and  not ("non-" in self.pred):
                self.sub = remove(self.sub,"non-")
                self.pred = "non-" + self.pred
                subBak = self.sub
                self.sub = self.pred
                self.pred = subBak

            elif ("non-" in self.sub) and ("non-" in self.pred):
                self.sub = remove(self.sub,"non-")
                self.pred = remove(self.pred,"non-")
                subBak = self.sub
                self.sub = self.pred
                self.pred = subBak
                               

        
class Syllog:
    '''A class for a categorical syllogism.'''

    def __init__(self, majorPrem, minorPrem, conclus):
        '''__init__(Propos,Propos,Propos) -> Syllog
           Class constructor. Takes three propositions as input.'''
        self.majorPrem = majorPrem
        self.minorPrem = minorPrem
        self.conclus = conclus

    def __str__(self):
        '''Propos.__str__() -> str
           Class printer. Bar adjusts itself to length of the longest
           propositions. Also ignores putting F for false propositions.'''
        maxLen = max([len(self.majorPrem.getEngName()), len(self.minorPrem.getEngName()), len(self.conclus.getEngName())])
        outStr = ""
        outStr += self.majorPrem.getEngName() + '\n' + self.minorPrem.getEngName() + '\n' + "-"*maxLen + '\n' + self.conclus.getEngName()
        return outStr

    def getMood(self):
        '''Propos.getMood() -> str
           Gives the mood of the syllogism.'''
        return self.majorPrem.lettype + self.minorPrem.lettype + self.conclus.lettype

    def getMiddleTerm(self):
        '''Propos.getMiddleTerm() -> str
           Gives the middle term of the syllogism.'''
        for term in [self.majorPrem.sub, self.majorPrem.pred,self.minorPrem.sub,self.minorPrem.pred]:
            if term in self.majorPrem.getEngName() and (not (term in self.conclus.getEngName())):
                middleterm = term
        return middleterm
    
    def getFig(self):
        '''Propos.getFig() -> int
           Gives the figure of the syllogism as an Int.'''
        if self.getMiddleTerm() == self.majorPrem.sub and self.getMiddleTerm() == self.minorPrem.sub:
            return 4
        if self.getMiddleTerm() == self.majorPrem.sub and self.getMiddleTerm() == self.minorPrem.pred:
            return 1
        if self.getMiddleTerm() == self.majorPrem.pred and self.getMiddleTerm() == self.minorPrem.sub:
            return 3
        if self.getMiddleTerm() == self.majorPrem.pred and self.getMiddleTerm() == self.majorPrem.pred:
            return 2

    def isValid(self):
        '''Propos.getFig() -> bool
           Tests for validity. IT DOES NOT TEST FOR SOUNDNESS.'''
        if not (((self.majorPrem.getEngName())+(self.minorPrem.getEngName())).count(self.getMiddleTerm()) == 0 \
           or not sublist(self.conclus.getTermsDist(),extend((self.majorPrem.getTermsDist()),(self.minorPrem.getTermsDist()))) \
           or ((self.majorPrem.getQuality()=="negative") and (self.minorPrem.getQuality()=="negative")) \
           or ((self.conclus.getQuality()=="negative" and self.minorPrem.getQuality()=="affirmative" and self.majorPrem.getQuality()=="affirmative") or (self.conclus.getQuality()=="affirmative" and ((not (self.minorPrem.getQuality()=="affirmative")) or (not (self.majorPrem.getQuality()=="affirmative")))))): 
            return "Not Valid"
        else:
            return "Valid"
