from generate_balance_file import generate_balance_file
from interval import set_interval

def main():
    set_interval(generate_balance_file, 2)

if __name__ == "__main__":
    main()