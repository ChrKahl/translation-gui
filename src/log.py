"""helper for logging"""


def log(value, indent=0, end='\n'):
    """A projectspecific helper function to log nicely."""
    spacing = indent * "\t"
    print(f"[+] {spacing}" + str(value))
