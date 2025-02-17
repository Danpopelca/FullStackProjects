import random


class Shift:
    """Reprezintă un schimb de lucru cu ospătarii și secțiunile alocate"""

    def __init__(self, shift_date, shift_type, waiters, sections):
        self.shift_date = shift_date
        self.shift_type = shift_type
        self.waiters = waiters
        self.sections = sections

    def assign_sections(self):
        """Atribuie aleatoriu ospătarii la secțiuni"""
        random.shuffle(self.waiters)  # Amestecă lista de ospătari

        for section in self.sections:
            if self.waiters:
                section.assign_waiter(self.waiters.pop())  # Asignează ospătarul la secțiune

    def display_assignments(self):
        """Afișează alocarea secțiunilor în shift"""
        print(f"\nShift: {self.shift_date} - {self.shift_type}")
        for section in self.sections:
            print(section)