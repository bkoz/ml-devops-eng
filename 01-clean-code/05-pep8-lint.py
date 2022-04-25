# your task is to clean this script in 
# a way that uses the code as a single function 
# that takes a path and returns the total_price variable
# that meets pep8 standards and receives a 10 score using pylint

# You may need to:
# pip install autopep8 
# pip install pylint

import time
import numpy as np

def get_total_price(filepath):

    with open(filepath) as f:
        gift_costs = f.read().split('\n')

    # Remove the trailing null char or the following numpy call will fail.
    # that converts strings to ints.
    gift_costs = gift_costs[0:-1]
    gift_costs = np.array(gift_costs).astype(int)  

    return (gift_costs[gift_costs < 25]).sum() * 1.08

if __name__ == "__main__":
    """
    Shell command to generate data a file with 1M integers:
    $ for i in `seq 2 1000000`; do echo $((1 + $RANDOM % 100)) >> gift_costs.txt ; done
    """
    start = time.time()
    total_price = get_total_price('gift_costs.txt')
    print(f'Total ${total_price:0.2f}, Duration: {time.time() - start:0.2f} secs.')
