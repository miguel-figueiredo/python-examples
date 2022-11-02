import psutil
from prometheus_client import Gauge


class SystemMetrics:
    def __init__(self):
        self.memory_used = Gauge("memory_used_bytes", "Used memory in bytes.")
        self.memory_free = Gauge("memory_free_bytes", "Free memory in bytes.")
        self.memory_total = Gauge("memory_total_bytes", "Total memory in bytes.")
        self.cpu = Gauge("cpu_utilization_percent", "Percentage of CPU utilization.")

    async def update(self):
        memory = psutil.virtual_memory()
        self.memory_used.set(memory.used)
        self.memory_free.set(memory.free)
        self.memory_total.set(memory.total)
        self.cpu = psutil.cpu_percent(interval=None)
