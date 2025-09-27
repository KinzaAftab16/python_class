def main():
    
    tempe = input ("👋 Hey! Enter temperature in Fahrenheit:")
    tempe = float(tempe)

    celcius = (tempe - 32) * 5/9
    print(f"The temperature is {celcius} degrees Celsius")
if __name__ == '__main__':
    main()