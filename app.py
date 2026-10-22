O
XXO
X"""Marks Tool - print a short report for a list of marks."""
from config import load_env
from stats import average, highest,lowest
MARKS = [72, 65, 88, 91, 54]
def main():
    settings = load_env()
    print(settings["APP_NAME"])
    print("Count :", len(MARKS))
    print("Average:", average(MARKS))
    print("Highest:", highest(MARKS))
    print("lowest:",lowest(MARKS))
if __name__ == "__main__":
    main()
from stats import average, highest, lowest, pass_count
...
    pass_mark = int(settings["PASS_MARK"])
    print("Passed :", pass_count(MARKS, pass_mark), "of", len(MARKS))
