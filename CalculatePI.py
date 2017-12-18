import math
import random

def Compute_PI (numThrows):
    count = 0
    throw = 0
    while (throw < numThrows):
        xPos = random.uniform (-1.0, 1.0)
        yPos = random.uniform (-1.0, 1.0)
        if (math.hypot(xPos, yPos) < 1):
            count += 1
            throw += 1
        else:
            throw += 1

    calculated_pi = ((count / numThrows)*4)
    return calculated_pi

def main ():
    #trial 1 - 100 throws
    a = (Compute_PI (100))
    plus = ""
    if (a-math.pi > 0):
        plus = "+"
    print ("num = 100        ", "Calculated PI =", format(a, ".6f"), "  Difference =", plus + format(a-math.pi, ".6f"))

    #trial 2 - 1000 throws
    b = (Compute_PI (1000))
    plus = ""
    if (b-math.pi > 0):
        plus = "+"
    print ("num = 1000      ", "Calculated PI =", format(b, ".6f"), "  Difference =", plus + format(b-math.pi, ".6f"))

    #trial 3 - 10000 throws
    c = (Compute_PI (10000))
    plus = ""
    if (c-math.pi > 0):
        plus = "+"
    print ("num = 10000     ", "Calculated PI =", format(c, ".6f"), "  Difference =", plus + format(c-math.pi, ".6f"))

    #trial 4 - 100000 throws
    d = (Compute_PI (100000))
    plus = ""
    if (d-math.pi > 0):
        plus = "+"
    print ("num = 100000    ", "Calculated PI =", format(d, ".6f"), "  Difference =", plus + format(d-math.pi, ".6f"))

    #trial 5 - 1000000 throws
    e = (Compute_PI (1000000))
    plus = ""
    if (e-math.pi > 0):
        plus = "+"
    print ("num = 1000000   ", "Calculated PI =", format(e, ".6f"), "  Difference =", plus + format(e-math.pi, ".6f"))

    #trial 6 - 10000000 throws
    f = (Compute_PI (10000000))
    plus = ""
    if (f-math.pi > 0):
        plus = "+"
    print ("num = 10000000  ", "Calculated PI =", format(f, ".6f"), "  Difference =", plus + format(f-math.pi, ".6f"))

main ()
