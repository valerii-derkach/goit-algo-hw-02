def is_valid(input_string):
    brackets = {
        '(': ')',
        '[': ']',
        '{': '}'
    }
    # використовуємо стек для перевірки
    stack = []

    for char in input_string:
        # якщо символ є відкриваючою дужкою
        if char in brackets:
            stack.append(char)
        # якщо символ є закриваючою дужкою
        elif char in brackets.values():
            # якщо стек порожній або дужки не відповідають
            if not stack or brackets[stack.pop()] != char:
                return False

    # якщо після проходження по всьому рядку стек порожній, то строка з дужками валідна
    return len(stack) == 0
