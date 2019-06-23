
# cast percentage to int
def percentage_2_int(x):
    return int(x.strip('%'))


def dolar_2_float(x):
    return float(x.strip('$'))

def get_amenitie(x):
    t = x.strip('{')
    t = t.strip('}')
    t = t.replace('"', '')
    t = t.split(',')
    return t