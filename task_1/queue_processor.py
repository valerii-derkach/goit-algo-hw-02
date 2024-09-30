from queue import Queue
from request import Request

class QueueProcessor:
    def __init__(self):
        self.queue = Queue()
        self.request_counter = 0

    def generate_request(self):
        self.request_counter += 1
        new_request = Request(self.request_counter)
        self.queue.put(new_request)
        print(f"Заявка з ID {new_request.request_id} додана до черги.")

    def process_request(self):
        if not self.queue.empty():
            current_request = self.queue.get()
            current_request.process()
        else:
            print("Черга пуста. Немає заявок для обробки.")

    # візуалізація поточного стану черги
    def display_queue(self):
        if self.queue.empty():
            print("Черга пуста.")
        else:
            queue_list = list(self.queue.queue)
            ids_in_queue = [request.request_id for request in queue_list]
            print(f"Поточний стан черги: {ids_in_queue}")
