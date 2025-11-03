import time, sys
# UTILITY: Display formatted success message to the user
def success_message(message, delay_seconds):
    print(f"SUCCESS: {message}", end="", flush=True)
    time.sleep(delay_seconds)
