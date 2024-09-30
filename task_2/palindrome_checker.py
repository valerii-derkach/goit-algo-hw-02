from collections import deque

def is_palindrome(input_string):
    normalized_str = ''.join(input_string.lower().split())

    char_deque = deque(normalized_str)

    while len(char_deque) > 1:
        left_char = char_deque.popleft()
        right_char = char_deque.pop()
        if left_char != right_char:
            return False  # рядок не є паліндромом

    return True  # рядок є паліндромом
