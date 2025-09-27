INCHES_IN_FOOT : int= 12


def main():
    feet: float = input("Enter the number of feet: ")
    inches: float  = feet * INCHES_IN_FOOT

    print (f'This is value {inches} in inches!')

if __name__ == "__main__":
    main()