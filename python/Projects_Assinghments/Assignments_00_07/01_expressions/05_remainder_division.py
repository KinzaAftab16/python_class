def main():
    
    dividend = int(input("Enter the dividend: "))
    divisor = int(input("Enter the divisor: "))

    quotient: int  = dividend // divisor
    remainder: int = dividend % divisor

    print (f"  \033[1;3m The quotient is: {quotient} and the remainder is: {remainder}  \033[0m")
if __name__ == '__main__':
    main() 