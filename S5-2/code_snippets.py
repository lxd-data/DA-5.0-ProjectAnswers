# input.py
import calculator

def main():
    user_numbers = user_numbers = input("Please input two numbers separated by commas: ").replace(",", " ").split()
    n1 = float(user_numbers[0])
    n2 = float(user_numbers[1])
    
    print(calculator.add(n1,n2))

main()