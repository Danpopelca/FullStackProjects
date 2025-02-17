import random
from models.waiter import Waiter
from models.section import Section

def assign_sections(waiters, sections):
    """Randomly assigns servers to sections"""
    random.shuffle(waiters)  # Shuffle the list of servers

    for section in sections:
        if waiters:
            section.assign_waiter(waiters.pop())  # Assign a server to each section

    return sections