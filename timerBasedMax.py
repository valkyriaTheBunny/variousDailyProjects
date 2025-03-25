import threading
import time

def set_max_timer(t1, t2):
    max_timer = [0]  # Using a list to allow modification within threads

    def timer_function(duration):
        time.sleep(duration)
        max_timer[0] = max(max_timer[0], duration)

    # Create two threads for the timers
    timer1 = threading.Thread(target=timer_function, args=(t1,))
    timer2 = threading.Thread(target=timer_function, args=(t2,))

    # Start both threads
    timer1.start()
    timer2.start()

    # Wait for both timers to finish
    timer1.join()
    timer2.join()

    return max_timer[0]

# Example usage
result = set_max_timer(3, 5)
print(f"The maximum timer value is: {result}")
