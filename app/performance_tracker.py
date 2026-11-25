import time

class PerformanceTracker:

    def __init__(self):
        self.timings= {}

    def start(self, step):
        self.start_time = time.perf_counter()
        self.current_step = step
        print(f"\n[Start] {step}")

    def end(self):
        end_time = time.perf_counter()
        duration = end_time - self.start_time
        self.timings[self.current_step] = duration


        print(f"[DONE] {self.current_step}:{duration:.2f} seconds")

    def report(self):
        print("\n========== PERFORMANCE REPORT ==========")

        for step, duration in self.timings.items():
                  print(f"{step<30} {duration:.2f} sec")

        total = sum(self.timings.values())

        print("----------------------------------------")
        print(f"{'Total Execution Time':<30} {total:.2f} sec")
        print("========================================")