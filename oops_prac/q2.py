from datetime import datetime, timedelta


class AccessLogger:
    def __init__(self):
        self.user_history = {}

    def parse_time(self, timestamp_str):
        dt = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
        return dt

    def log_access(self, user_id, timestamp_str):
        parsed_time = self.parse_time(timestamp_str)
        if user_id not in self.user_history:
            self.user_history[user_id] = {
                "id": user_id,
                "history": [],
            }
            self.user_history[user_id]["history"].append(parsed_time)
        else:
            self.user_history[user_id]["history"].append(parsed_time)

    def count_recent_requests(self, user_id, current_time_obj, window_seconds):
        if user_id not in self.user_history:
            return 0
        user_timestamps = self.user_history[user_id]["history"]
        cutoff_time = current_time_obj - timedelta(seconds=window_seconds)
        count = 0
        for time in user_timestamps:
            if time > cutoff_time:
                count += 1
        return count

    def get_active_users(self):
        users = self.user_history.values()
        users = sorted(users, key=lambda user: (-len(user["history"]), user["id"]))
        user_ids = [user["id"] for user in users]
        return user_ids

    def process_ticket(self, user_id, timestamp_str): ...
