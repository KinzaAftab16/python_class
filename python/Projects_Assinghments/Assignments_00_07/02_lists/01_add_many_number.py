def sum_numbers(numbers)-> int:
    total_so_far: int = 0
    for number in numbers:
        total_so_far += number

    return total_so_far

def main():
    numbers: list[int] = [6, 2, 8, 4, 5] 
    sum_of_numbers: int = sum_numbers(numbers)  
    print(sum_of_numbers)

if __name__ == '__main__':
    main()