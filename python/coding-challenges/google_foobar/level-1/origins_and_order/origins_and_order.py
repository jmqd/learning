def stringify(x):
    x = str(x)
    if len(x) < 2:
        return str(0) + x
    else: return x
def date_me(month, day, year):
    return month + "/" + day + "/" + year
def answer(x,y,z):
    inputs = [x,y,z]
    sorted(inputs)
    month = inputs[0]
    if (inputs[1] <= 12 and inputs[1] != month):
        return "Ambiguous"
    if month in [1,3,5,7,8,10,12]:
        if (inputs[2] <= 31 and inputs[1] != inputs[2]):
            return "Ambiguous"
        else:
            day  = inputs[1]
            year = inputs[2]
    elif month in [4,6,9,11]:
        if (inputs[2] <= 30 and inputs[1] != inputs[2]):
            return "Ambiguous"
        else:
            day  = inputs[1]
            year = inputs[2]
    else:
        if (inputs[2] <= 28 and inputs[1] != inputs[2]):
            return "Ambiguous"
        else:
            day  = inputs[1]
            year = inputs[2]
    return date_me(stringify(month), stringify(day), stringify(year))
