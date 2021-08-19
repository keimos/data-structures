# Calculating Annual Payment

def SetAnnual():
    global annual
    annual = 10000


def MonthlyPayment():
    print("Your monthly payment is " + str(annual / 12) + " USD.")


SetAnnual()
MonthlyPayment()


