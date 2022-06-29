"""

Thanks To Conrad Rider of http://cube.rider.biz/algtrans.html

Algorithm Translator.
Tool for manipulating Rubik's cube algorithms. Supports rotating, inverting and mirroring algs in standard notation.

This is a porting of the javascript code to python.

"""


class AlgTrans:
    
    def __init__(self, alg = ""):
        self.alg = alg

    ALG_POW = ['', "2", "'"]

    MOV = ['U', 'R', 'F', 'D', 'L', 'B', 'u', 'r', 'f',
            'd', 'l', 'b', 'E', 'M', 'S', 'x', 'y', 'z'
       ]
    MAN = ['d', 'l', 'b', 'u', 'r', 'f', 'D', 'L', 'B',
            'U', 'R', 'F', 's', 's', 's', '-', '-', '-']

    XTR = ['B', 'R', 'U', 'F', 'L', 'D', 'b', 'r', 'u',
            'f', 'l', 'd', 'S', 'M', 'E-', 'x', 'z-', 'y']

    YTR = ['U', 'F', 'L', 'D', 'B', 'R', 'u', 'f', 'l',
            'd', 'b', 'r', 'E', 'S-', 'M', 'z', 'y', 'x-']

    ZTR = ['R', 'D', 'F', 'L', 'U', 'B', 'r', 'd', 'f',
            'l', 'u', 'b', 'M', 'E-', 'S', 'y-', 'x', 'z']

    MTR = ['U-', 'L-', 'F-', 'D-', 'R-', 'B-', 'u-', 'l-', 'f-',
       'd-', 'r-', 'b-', 'E-', 'M', 'S-', 'x', 'y-', 'z-']

    STR = ['U-', 'R-', 'B-', 'D-', 'L-', 'F-', 'u-', 'r-', 'b-',
       'd-', 'l-', 'f-', 'E-', 'M-', 'S', 'x-', 'y-', 'z']

    ETR = ['D-', 'R-', 'F-', 'U-', 'L-', 'B-', 'd-', 'r-', 'f-',
       'u-', 'l-', 'b-', 'E', 'M-', 'S-', 'x-', 'y', 'z-']

    # Maps move names to a move id
    def moveId(self, move):
        """
        Python 3.10 or higher

        match(move):
            case 'U':
                return 0
            case 'R':
                return 1
            case 'F':
                return 2
            case 'D':
                return 3
            case 'L':
                return 4
            case 'B':
                return 5
            case 'u':
                return 6
            case 'r':
                return 7
            case 'f':
                return 8
            case 'd':
                return 9
            case 'l':
                return 10
            case 'b':
                return 11
            case 'E':
                return 12
            case 'M':
                return 13
            case 'S':
                return 14
            case 'x':
                return 15
            case 'y':
                return 16
            case 'z':
                return 17
        """

        if move == 'U':
            return 0
        elif move == 'R':
            return 1
        elif move == 'F':
            return 2
        elif move == 'D':
            return 3
        elif move == 'L':
            return 4
        elif move == 'B':
            return 5
        elif move == 'u':
            return 6
        elif move == 'r':
            return 7
        elif move == 'f':
            return 8
        elif move == 'd':
            return 9
        elif move == 'l':
            return 10
        elif move == 'b':
            return 11
        elif move == 'E':
            return 12
        elif move == 'M':
            return 13
        elif move == 'S':
            return 14
        elif move == 'x':
            return 15
        elif move == 'y':
            return 16
        elif move == 'z':
            return 17

        return -1

    # Returns the power of a move with given suffix
    def movePow(self, chr):
        """
        Python 3.10 and higher

        match(chr):
            case "2":
                return 1
            case "'":
                return 2
            case "3":
                return 2
        return 0
        """

        if chr == "2":
            return 1
        elif chr == "'":
            return 2
        elif chr == "3":
            return 2
        return 0

    # Translates an alg according to the given translation table
    def transAlg(self, alg, trn):
        n = len(alg)
        i = 0
        out = ''
        while (i < n):
            move = self.moveId(alg[i : i+1])
            if (move != -1):
                pow = 0
                if (i < n - 1):
                    pow = self.movePow(alg[i + 1 : i+2])
                out = out + trn[move][0 : 1] + (self.ALG_POW[2 - pow] if len(trn[move]) > 1 else self.ALG_POW[pow]) + " "

            i = i + 1

        return out

    # Inverts a cube algorithm


    def invertAlg(self, alg):
        inverse = ""
        pow = 0
        i = len(alg) - 1
        while (i >= 0):
            move = self.moveId(alg[i : i+1])
            if (move != -1):
                inverse = inverse + alg[i : i+1] + self.ALG_POW[2 - pow] + " "
                pow = 0
            else:
                pow = self.movePow(alg[i : i+1])

            i = i - 1

        return inverse


    def generate(self):
        data = {}
        data['Inverse'] = self.invertAlg(self.alg)
        data['Rotate x'] = self.transAlg(self.alg, self.XTR)
        data['Rotate y'] = self.transAlg(self.alg, self.YTR)
        data['Rotate z'] = self.transAlg(self.alg, self.ZTR)
        data['Mirror L/R'] = self.transAlg(self.alg, self.MTR)
        data['Mirror F/B'] = self.transAlg(self.alg, self.STR)
        data['Mirror U/D'] = self.transAlg(self.alg, self.ETR)
        return data