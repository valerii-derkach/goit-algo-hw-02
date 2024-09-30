from palindrome_checker import is_palindrome

def main():
    input_string = input("Введіть рядок для перевірки: ")
    if is_palindrome(input_string):
        print(f"Рядок '{input_string}' є паліндромом.")
    else:
        print(f"Рядок '{input_string}' не є паліндромом.")

if __name__ == "__main__":
    main()
