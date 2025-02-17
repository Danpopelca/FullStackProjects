class Section:
    """Reprezintă o secțiune din restaurant"""

    def __init__(self, name):
        self.name = name
        self.assigned_waiter = None

    def assign_waiter(self, waiter):
        """Asignează un ospătar la secțiune"""
        self.assigned_waiter = waiter

    def __repr__(self):
        return f"{self.name} - {self.assigned_waiter if self.assigned_waiter else 'N/A'}"