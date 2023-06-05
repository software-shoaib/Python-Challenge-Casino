# Python-Challenge-Casino
Python Challenge Casino has a slot machine. You can get a result from the slot machine by calling play_slot_machine(). The number it returns is your winnings in dollars. Usually it returns 0. But sometimes you'll get lucky and get a big payday.

On average, how much money can you expect to gain (or lose) every time you play the machine? The casino keeps it a secret, but you can estimate the average value of each pull using a technique called the Monte Carlo method. To estimate the average outcome, we simulate the scenario many times, and return the average result.

# QUESTION SOLVED 
The exact expected value of one pull of the slot machine is 0.025 - i.e. a little more than 2 cents. See? Not every game in the Python Challenge Casino is rigged against the player!

In order to get this answer, you'll need to implement the estimate_average_slot_payout(n_runs) function to simulate pulling the slot machine n_runs times. It should return the payout averaged over those n_runs.

Then, once the function is defined, in order to estimate the average slot payout, we need only call the function.

Because of the high variance of the outcome (there are some very rare high payout results that significantly affect the average) you might need to run your function with a very high value of n_runs to get a stable answer close to the true expectation. For instance, you might use a value for n_runs of 1000000.

Here's an example for how the function could look:

def estimate_average_slot_payout(n_runs):
    # Play slot machine n_runs times, calculate payout of each
    payouts = [play_slot_machine()-1 for i in range(n_runs)]
    # Calculate the average value
    avg_payout = sum(payouts) / n_runs
    return avg_payout



In this example, the play_slot_machine() function generates a random number using the random.random() function from the random module. The function then uses different probability ranges to determine the outcome of the slot machine.

There's a 95% chance of winning $0 (0.95 probability range).
There's a 5% chance of winning $10 (0.995 probability range).
There's a 0.4% chance of winning $100 (0.999 probability range).
There's a 0.1% chance of winning $1000 (1.0 probability range).
Feel free to adjust the probabilities and winnings according to your specific requirements.
estimate_average_slot_payout(10000000)
This should return an answer close to 0.025!

import random


def play_slot_machine():
    # Generate a random number between 0 and 1
    random_number = random.random()

    # Determine the outcome based on the random number
    if random_number < 0.95:
        # 95% chance of winning $0
        return 0
    elif random_number < 0.995:
        # 5% chance of winning $10
        return 10
    elif random_number < 0.999:
        # 0.4% chance of winning $100
        return 100
    else:
        # 0.1% chance of winning $1000
        return 1000
