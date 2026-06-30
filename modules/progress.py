import time


class ProgressTracker:

    def __init__(self):
        self.start_time = time.time()
        self.attempts = 0

    def update(self):
        self.attempts += 1

    def elapsed(self):
        return time.time() - self.start_time

    def speed(self):
        elapsed = self.elapsed()

        if elapsed <= 0:
            return 0

        return self.attempts / elapsed

    def print_status(self, current_password):

        print(
            f"\rAttempts: {self.attempts:,} | "
            f"Speed: {self.speed():,.0f} H/s | "
            f"Current: {current_password[:30]}",
            end=""
        )