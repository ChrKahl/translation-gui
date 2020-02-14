"""A script to complement missing keys in a JSON translationsfile."""

import os
import json
from log import log


class Diff():
    """A script to complement missing keys in a JSON translationsfile."""

    def __init__(self, src_file, dst_file):
        self.dst_missing_keys = []
        self.src_file = src_file
        self.dst_file = dst_file

        with open(self.src_file, "r") as file:
            src_string = file.read()

        with open(self.dst_file, "r") as file:
            dst_string = file.read()

        self.src_json = json.loads(src_string)
        self.dst_json = json.loads(dst_string)

        self.src_keys = self.src_json.keys()
        self.dst_keys = self.dst_json.keys()
        self.get_keys_not_in_dst()

    def get_keys_not_in_dst(self):
        """Get the difference between src- and dst-file."""
        for key in self.src_keys:
            if key not in self.dst_keys:
                self.dst_missing_keys.append(key)
        return self.dst_missing_keys

    def display_count_keys_not_in_dst(self):
        """Logging the count of missing keys in destination file."""
        log(f"Missing values: {len(self.dst_missing_keys)}")

    def display_keys_not_in_dst(self):
        """Logging missing keys of destination file."""
        log(self.dst_missing_keys)

    def add_missing_keys(self):
        """Get asked for each key where a value is missing in dst-file."""
        for key in self.dst_missing_keys:
            i = input("Press n for next or q to quit: ")
            if i == "q":
                log("Additions saved.")
                return
            if i == "n":
                log("Insert translation for:")
                log(f"Key: {key}", 1)
                log(f"Value: {self.src_json[key]}", 1)
                value = input("\t")
                self.dst_json[key] = value
                self.dst_missing_keys.remove(key)

    def write_dst_file(self, dst_file=""):
        """write the changes in file"""
        if dst_file == "":
            dst_file = self.dst_file
        with open(dst_file, "w") as file:
            file.write(json.dumps(self.dst_json))


if __name__ == "__main__":
    DIRNAME = os.path.dirname(__file__)
    DIFF = Diff(os.path.join(DIRNAME, "../data/de.json"),
                os.path.join(DIRNAME, "../data/en.json"))
    DIFF.display_count_keys_not_in_dst()
    DIFF.add_missing_keys()
    DIFF.write_dst_file(os.path.join(DIRNAME, "../data/en1.json"))
