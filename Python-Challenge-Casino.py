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

def estimate_average_slot_payout(n_runs):
    
    """Run the slot machine n_runs times and return the average net profit per run.
    Example calls (note that return value is nondeterministic!):
    >>> estimate_average_slot_payout(1)
    -1
    >>> estimate_average_slot_payout(1)
    0.5
    """
    # Play slot machine n_runs times, calculate payout of each
    payouts = [play_slot_machine()-1 for i in range(n_runs)]
    # Calculate the average value
    avg_payout = sum(payouts) / n_runs
    return avg_payout

# for example:

estimate_average_slot_payout(10000)
