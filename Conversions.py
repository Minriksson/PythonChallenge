import math
from math import pi

# ==================================================================
# Angular unit transformations
# ------------------------------------------------------------------
# SI unit      1 radian [rad]
# Other units  1 degree [deg] = pi/180 rad
#              1 gradian [grad] = 400/360 deg = 1/0.9 deg

def Rad2Deg( rad ):
    """Convert an angular value from Radian to Degree"""
    return rad * 180 / pi

def Deg2Rad( deg ):
    """Convert an angular value from Degree to Radian """
    return deg * pi / 180

def Dec2Binx( numDec : int ):
    """Convert an numeric value from decimal (base 10) to binary (base 2) """
    
    # End of recursion
    if numDec == 0:
        return ""

    # Divide value by 2 and recurse
    # Append a '1' if the current value is even, or '0' otherwise
    return Dec2Binx( numDec // 2 ) + str( numDec % 2)

def Dec2Bin( numDec : int ):
    """Convert an numeric value from decimal (base 10) to binary (base 2) """
    
    # Start with an empty string
    strBin = ""

    while numDec > 0:
        # Divide the value with the base (e.g. 2) and use the reminder as the next character
        strBin = str( numDec % 2) + strBin
        # Divide remaining value by the base (e.g. 2) and continue loop
        numDec = numDec // 2

    return strBin

def Dec2Hex( numDec : int ):
    """Convert an numeric value from decimal (base 10) to hexadecimal (base 16) """
    
    dictHex = {
        0:"0",
        1:"1",
        2:"2",
        3:"3",
        4:"4",
        5:"5",
        6:"6",
        7:"7",
        8:"8",
        9:"9",
        10:"A",
        11:"B",
        12:"C",
        13:"D",
        14:"E",
        15:"F"
    }
    # Start with an empty string
    strHex = ""

    while numDec > 0:
        # Divide the value with the base (e.g. 16) and use the reminder as the next character
        strHex = dictHex[numDec % 16] + strHex
        # Divide remaining value by the base (e.g. 16) and continue loop
        numDec = numDec // 16

    return strHex


########### This is the main entry point #########

#print( Deg2Rad(180) )
print( Dec2Bin(345) )
print( Dec2Binx(345) )
print( Dec2Hex(255) )