class Calculations:
    def __init__(self, a, b, operations):
        self.a = a
        self.b = b
        self.operations = operations  # Store the operations function

    def get_answer(self):
        # Call the stored operations with a and b
        return self.operations(self.a, self.b)