import math
from collections import Counter

# retourne l'entropie Shannon du fichier passé en parametre
def get_entropy(filename):
    
    # ouvre le fichier en lecture readbyte
    with open(filename,"rb") as file:
        data=file.read()
    
    possible = dict(((chr(x), 0) for x in range(0, 256)))

    for byte in data:
        possible[chr(byte)] +=1

    data_len = len(data)
    entropy = 0.0
    
    for i in possible:
        if possible[i] == 0:
            continue

        p = float(possible[i] / data_len)
        entropy -= p * math.log(p, 2)
    return entropy


def identification(x):
    assert (8 > x > 0)
    if x > 7.9:
        return("Very high entropy : certainly enciphered or compressed")
    
    elif x > 7.5 :
        return("High entropy, surely compressed or enciphered")
      
    elif x < 3:
        return("Medium entropy : probably a regular file")       
        
    else:
        return("Regular File")