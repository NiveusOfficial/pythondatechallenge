import string

class dateStuff(object):
    """docstring for dateStuff."""

    def __init__(self, fY, sY):
        super(dateStuff, self).__init__()
        self.fy = fY.split('/')
        self.sy = sY.split('/')
        self.months = {1 : 31,2 : 28,3 : 31,4 : 30,5 : 31,6 : 30,7 : 31,8 : 31,9 : 30,10 : 31,11 : 30,12 : 31}

    def getHigherDate(self):
        fy = int(self.fy[0])
        sy = int(self.sy[0])
        fm = int(self.fy[1])
        sm = int(self.sy[1])
        fd = int(self.fy[2])
        sd = int(self.sy[2])
        if fy > sy:
            higher = fy, fm, fd
            lower = sy, sm, sd
        elif (fy < sy):
            higher = sy, sm, sd
            lower = fy, fm, fd
        else:
            if fm > sm:
                higher = fy, fm, fd
                lower = sy, sm, sd
            elif fm < sm:
                higher = sy, sm, sd
                lower = fy, fm, fd
            else:
                if fd > sd:
                    higher = fy, fm, fd
                    lower = sy, sm, sd
                elif fd < sd:
                    higher = sy, sm, sd
                    lower = fy, fm, fd
                else:
                    higher = sy, sm, sd
                    lower = fy, fm, fd
        return higher, lower

    def getAmountOfSuperYears(self):
        higher = self.getHigherDate()[0]
        lower = self.getHigherDate()[1]
        superyearsCount = 0

        for d in range(lower[0], higher[0]):
            if d%4 == 0:
                superyearsCount += 1

        if lower[0]%4 == 0:
            if lower[1] > 2:
                superyearsCount -= 1
        if higher[0]%4 == 0:
            if higher[1] <= 2:
                if higher[2] != 29:
                    superyearsCount -= 1

        return superyearsCount

    def getDifference(self):
        superDays = self.getAmountOfSuperYears()
        higher = self.getHigherDate()[0]
        lower = self.getHigherDate()[1]
        DM = 0
        for i in self.months:
            if i == int(lower[1]):
                DM = self.months[i]
        A = DM - lower[2] + higher[2]
        B = 11 - lower[1] + higher[1]
        C = higher[0] - lower[0] - 1

        if A > DM:
            B += 1
            A -= DM

        if B > 12:
            C += 1
            B -= 12

        days = A

        if (lower[1] + B) > 12:
            K = lower[1] + B - 12
            for x in range(1, K):
                days += self.months[x]
            for z in range(lower[1], 13):
                days += self.months[z]
            if lower[1] == 12:
                days += self.months[12]

        else:
            if lower[1] != 12:
                for z in range(lower[1], lower[1] + B):
                    days += self.months[z]
            else:
                days += self.months[12]


        days += C*365
        days += superDays

        return days


#a = dateStuff("1918/04/08", "1891/11/27")
#a = dateStuff("2009/12/04", "2000/01/01")
#a = dateStuff("2009/02/28", "2000/09/01")
#a = dateStuff("2009/02/02", "2000/11/01")

print (a.getDifference())
