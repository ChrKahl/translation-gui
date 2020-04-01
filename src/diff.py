"""A script to complement missing keys in a JSON translationsfile."""

import json
import sys
from .log import log
from .getch import getch


class Diff():
    """A script to complement missing keys in a JSON translationsfile."""

    def __init__(self, src_file, dst_file, out):
        self.dst_missing_keys = []
        self.src_file = src_file
        self.dst_file = dst_file
        self.out = out

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

    def compare_keys(self):
        """
        compare values of same keys and let the
        user decide which one should be added
        """
        new_json = json.loads('{}')
        for key in self.src_keys:
            if key in self.dst_keys:
                if self.dst_json[key] != self.src_json[key]:
                    log("")
                    log(f"Key: {key}", 1)
                    log(f"SRC-Value(1): {self.src_json[key]}", 2)
                    log(f"DST-Value(2): {self.dst_json[key]}", 2)
                    i = getch()
                    if i == "1":
                        new_json[key] = self.src_json[key]
                        log(f"[src] {self.src_json[key]} written for {key}.")
                    elif i == "2":
                        new_json[key] = self.dst_json[key]
                        log(f"[dst] {self.dst_json[key]} written for {key}.")
                    else:
                        new_file = json.dumps(new_json, indent=2, sort_keys=True, ensure_ascii=False)
                        log(new_file)
                        sys.exit(0)
                else:
                    # log(f"[src] Values for key: {key} doesn't differ.")
                    new_json[key] = self.src_json[key]
            else:
                log(f"[src] Key: {key} is only in source-file. Writing it.")
                new_json[key] = self.src_json[key]

        for key in self.dst_keys:
            if key not in new_json:
                log(f"[dst] Added Value from destination-file for key: {key}", 2)
                new_json[key] = self.dst_json[key]

        self.write_file(new_json)

    def write_file(self, out_json=None):
        """write the changes in file"""
        json_to_write = out_json or self.dst_json
        try:
            with open(self.out, "w+") as file:
                file.write(
                    json.dumps(json_to_write,
                               indent=2,
                               sort_keys=True,
                               ensure_ascii=False))
            log(f"Wrote file to {self.out}")
        except FileNotFoundError:
            log(f"Could not write file to {self.out}")
