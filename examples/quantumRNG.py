import urllib.request as urlrequest
from numpy import array
# CASEY PANCOAST 2019
# Adapted from https://github.com/pcragone/anurandom/blob/master/anurandom.py
class ANURandom:
    BINARY = "BINARY"
    HEX = "HEX"

    # gets a quantum-generated random number from a server
    def getRandom(self, type):
        # Finds location to get random number from
        if type == self.BINARY:
            url = 'http://150.203.48.55/RawBin.php'
        elif type == self.HEX:
            url = 'http://150.203.48.55/RawHex.php'

        # Gets the page
        page = urlrequest.urlopen(url, timeout=5)

        # Returns the html of the page as a string
        data = page.read().decode()

        # Finds the portion of the code where the random number is
        numString = data.split('<td>\n')[1].split('</td>')[0]

        if type == self.BINARY:
            num = int(numString, 2)
        elif type == self.HEX:
            num = int(numString, 16)

        return num

    def getBin(self):
        return self.getRandom(self.BINARY)

    def getHex(self):
        return self.getRandom(self.HEX)

    def getChar(self):
        return self.getRandom(self.CHAR)

def realrandom(k=1):
    anuRandom = ANURandom()
    ran = []
    i = 0
    while i<k:
        r = str(anuRandom.getBin())
        pr=len(r)
        initial = 5
        ran.append(float(r[initial:pr])/10**(pr-initial))
        i+=1
    return array(ran)