from delimiter_checker import is_valid

def main():
    input_string = input("Введіть рядок з дужками для перевірки: ")

    if is_valid(input_string):
        print(f"У строці '{input_string}' послідовність дужок валідна")
    else:
        print(f"У строці '{input_string}' послідовність дужок не валідна")

if __name__ == "__main__":
    main()
