class Request:
    def __init__(self, request_id):
        self.request_id = request_id

    def process(self):
        print(f"Обробка заявки з ID: {self.request_id}")
