"""A script to complement missing keys in a JSON translationsfile."""

import json
from .log import log
from .getch import getch


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

    def add_missing_keys(self, auto=False):
        """Get asked for each key where a value is missing in dst-file."""
        for key in self.dst_missing_keys:
            if auto:
                self.dst_json[key] = self.src_json[key]
            else:
                log("Press n for next or q to quit: ", end='')
                i = getch()
                if i == "q":
                    log("Additions saved.")
                    return
                if i == "n":
                    log("Insert translation for (Press x to use source-value):")
                    log(f"Key: {key}", 1)
                    log(f"Value: {self.src_json[key]}", 1)
                    value = input("\t")
                    if value == "x":
                        self.dst_json[key] = self.src_json[key]
                    else:
                        self.dst_json[key] = value

                    self.dst_missing_keys.remove(key)

    def write_dst_file(self, dst_file=""):
        """write the changes in file"""
        if dst_file == "":
            dst_file = self.dst_file
        try:
            with open(dst_file, "w+") as file:
                file.write(json.dumps(self.dst_json, indent=2, sort_keys=True, ensure_ascii=False))
            log(f"Wrote file to {dst_file}")
        except FileNotFoundError:
            log(f"Could not write file to {dst_file}")
