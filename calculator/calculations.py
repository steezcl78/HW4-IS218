class Calculations:
    def __init__(self, a, b, operations):
        self.a = a
        self.b = b
        self.operations = operations  # Store the operation function

    def get_answer(self):
        # Call the stored operation with a and b
        return self.operations(self.a, self.b)