from queue_processor import QueueProcessor
import time
import random

def main():
    processor = QueueProcessor()

    try:
        while True:
            # генеруємо нові заявки
            if random.choice([True, False]):
                processor.generate_request()

            # виводимо поточний стан черги
            processor.display_queue()

            # обробляємо заявки
            if random.choice([True, False]):
                processor.process_request()

            # імітуємо затримку між операціями
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nПрограма зупинена користувачем.")

if __name__ == "__main__":
    main() 
