import math
def main():
   
   ab :float = float(input("Enter the lenght of AB: ")) 
   ac :float = float(input("Enter the length of AC: "))
   bc:float = math.sqrt(ab**2 + ac**2)

   print(f"The lenght of Bc the hypotenuse is {bc}")
if __name__ == '__main__':
    main()