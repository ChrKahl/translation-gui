"""helper for logging"""


def log(value, indent=0):
    """A projectspecific helper function to log nicely."""
    spacing = indent * "\t"
    print(f"[+] {spacing}" + str(value))
