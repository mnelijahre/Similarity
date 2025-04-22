import sys
import time

class ProgressBar:
    def __init__(self, iterations):
        self.iterations = iterations
        self.prefix = "Status"
        self.suffix = "Complete"
        self.length = 50
        self.fill = '█'
        self.print_end='\r'

    def print_bar(self, iteration):
        percent = ("{0:.1f}").format(100 * (iteration / float(self.iterations)))
        filled_length = int(self.length * iteration // self.iterations)
        bar = self.fill * filled_length + '-' * (self.length - filled_length)
        sys.stdout.write(f'\r{self.prefix} |{bar}| {percent}% {self.suffix}')
        sys.stdout.flush()

    def run(self):
        for i in range(self.iterations + 1):
            time.sleep(0.1)  # Simulating work with a sleep
            self.print_bar(i)

        sys.stdout.write(self.print_end)
        sys.stdout.flush()
