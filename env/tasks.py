def load_task(level):
    if level == "easy":
        return {
            "emails": [
                {"id": 0, "subject": "Urgent meeting", "body": "Join ASAP", "sender": "boss"},
                {"id": 1, "subject": "Big Sale", "body": "Buy now!!!", "sender": "spam"}
            ],
            "labels": {0: "urgent", 1: "spam"}
        }

    elif level == "medium":
        return {
            "emails": [
                {"id": 0, "subject": "Invoice due", "body": "Payment pending", "sender": "client"},
                {"id": 1, "subject": "Hello", "body": "Just checking in", "sender": "friend"},
                {"id": 2, "subject": "Limited offer", "body": "Discount available", "sender": "spam"}
            ],
            "labels": {0: "urgent", 1: "normal", 2: "spam"}
        }

    else:  # HARD
        return {
            "emails": [
                {"id": 0, "subject": "Server issue", "body": "System unstable", "sender": "ops"},
                {"id": 1, "subject": "Weekly newsletter", "body": "Updates inside", "sender": "marketing"},
                {"id": 2, "subject": "Project follow-up", "body": "Need update soon", "sender": "manager"},
                {"id": 3, "subject": "Exclusive deal", "body": "Special offer just for you", "sender": "spam"}
            ],
            "labels": {0: "urgent", 1: "normal", 2: "normal", 3: "spam"}
        }