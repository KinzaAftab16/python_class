def main():
    list = []

    value = input("Enter a value: ") 
    while value: 
        list.append(value) 
        value = input("Enter a value: ")  

    print("Here's the list:", list)

if __name__ == '__main__':
    main()