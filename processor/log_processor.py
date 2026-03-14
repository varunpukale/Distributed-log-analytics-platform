import json
from datetime import datetime

class LogProcessor:
    def __init__(self):
        self.logs = []

    def ingest_log(self, service_name, level, message):
        log_entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "service": service_name,
            "level": level,
            "message": message
        }
        self.logs.append(log_entry)
        return log_entry

    def search_logs(self, level=None):
        if level:
            return [log for log in self.logs if log["level"] == level]
        return self.logs


if __name__ == "__main__":
    processor = LogProcessor()

    processor.ingest_log("auth-service", "INFO", "User login successful")
    processor.ingest_log("payment-service", "ERROR", "Payment failed")

    results = processor.search_logs("ERROR")
    print(json.dumps(results, indent=2))
