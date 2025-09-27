def main():
   
   num = input(" \033[1;3m Enter the number to get the square: \033[0m")
   num = int(num)
   square = num ** 2
   print(" The square of the number is: ", square)

if __name__ == '__main__':
    main()