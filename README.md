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

estimate_average_slot_payout(10000000)
This should return an answer close to 0.025!
