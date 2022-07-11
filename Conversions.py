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

########### This is the main entry point #########

print( Deg2Rad(180) )
