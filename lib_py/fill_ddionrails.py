import os
import pandas as pd

def studies():
    os.system("cp metadata/studies.csv ddionrails")

def main():
    studies()

if __name__ == "__main__":
    main()
