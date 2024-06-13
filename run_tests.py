import doctest
import scripts.utils

def run_all_doctests():
    doctest.testmod(scripts.utils)

if __name__ == "__main__":
    run_all_doctests()
