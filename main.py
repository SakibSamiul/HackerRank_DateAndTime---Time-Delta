import math
import os
import random
import re
import sys
from datetime import datetime

# Complete the time_delta function below.
def time_delta(t1, t2):
    date_format = "%a %d %b %Y %H:%M:%S %z"
    datet1 = datetime.strptime(t1, date_format)
    datet2 = datetime.strptime(t2, date_format)

    delta_second = int(abs(datet1 - datet2).total_seconds())

    print(str(delta_second)) 
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

    #     fptr.write(delta + '\n')

    # fptr.close()
