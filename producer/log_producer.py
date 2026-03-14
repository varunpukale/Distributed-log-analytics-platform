import json
from datetime import datetime

class LogProducer:

    def create_log(self, service, level, message):
        log = {
            "timestamp": datetime.utcnow().isoformat(),
            "service": service,
            "level": level,
            "message": message
        }
        return json.dumps(log)


if __name__ == "__main__":
    producer = LogProducer()

    log1 = producer.create_log(
        "auth-service",
        "INFO",
        "User login successful"
    )

    print(log1)
