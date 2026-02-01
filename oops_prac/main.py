"""
Scenario: You are building a Simple File Storage System (like a mini Google Drive).

Level 1 Requirements: You need to implement a class CloudStorage with two methods:

add_file(file_id, size): Adds a file with the given file_id (string) and size (integer).
If the file already exists, return "false" (string).Otherwise, save it and return "true".

get_file_size(file_id): Returns the size of the file as a string (e.g. "500").
If the file doesn't exist, return "" (empty string).
"""


class CloudStorage:
    def __init__(self):
        self.files = {}

    def add_file(self, file_id, size):
        if file_id in self.files:
            return "false"
        self.files[file_id] = {"id": file_id, "size": size}
        return "true"

    def get_file_size(self, file_id):
        if file_id in self.files:
            return str(self.files[file_id]["size"])
        else:
            return ""

    def copy_file(self, source_id, dest_id):
        cond = (source_id not in self.files) or (dest_id in self.files)
        if cond:
            return "false"
        else:
            self.files[dest_id] = {"id": dest_id, "size": self.files[source_id]["size"]}
            return "true"

    def find_large_files(self, min_size):
        required_files = []
        for value in self.files.values():
            if value["size"] >= min_size:
                required_files.append(str(value["id"]))
        required_files = sorted(required_files)
        return ", ".join(required_files)
