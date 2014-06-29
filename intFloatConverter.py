def intFloatConverter(data, type):
    if type == 'int':
        output = int(data)
        roundCheck = output + .4
        if data > roundCheck:
            # Rounding up
            output = output + 1
            return output
        else:
            # Rounding down
            return output

    elif type == 'float':
        output = float(data)
        return output