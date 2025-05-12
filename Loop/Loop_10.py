# Exponential backoff

# Implement an exponential backoof strategy that doubles the wait time between retries, startinf form 1 second, but stps after 5 retries.

import time

wait_time = 1
max_retries = 5
attempts  = 0

while attempts < max_retries:
    print("Attempt", attempts + 1 , "in", wait_time, "seconds")
    time.sleep(wait_time)
    wait_time *= 2
    attempts += 1