from datetime import date
from models import Waiter, Section
from services.assignment import assign_sections
from services.data_handler import get_available_servers, save_servers
from services.section_handler import load_section_configurations

# Load section configurations from JSON
SECTION_CONFIGURATIONS = load_section_configurations()

# Get the number of servers
while True:
    try:
        num_servers = int(input("How many servers are working this shift? (3-10): "))
        if num_servers in SECTION_CONFIGURATIONS:
            break
        print("⚠️ Invalid number! Please enter a number between 3 and 10.")
    except ValueError:
        print("⚠️ Please enter a valid number.")

# If only one option exists, auto-select it
section_options = SECTION_CONFIGURATIONS[num_servers]
if len(section_options) == 1:
    selected_option = list(section_options.keys())[0]
else:
    print("\nSelect the section configuration:")
    for option, sections in section_options.items():
        print(f"{option}. {', '.join(sections)}")

    while True:
        selected_option = input("\nEnter the option letter: ").strip().upper()
        if selected_option in section_options:
            break
        print("⚠️ Invalid option! Try again.")

# Create the selected sections
sections = [Section(name) for name in section_options[selected_option]]

# Load available servers
available_servers = get_available_servers()
selected_servers = []

print("\nSelect the servers for this shift:")
for i in range(num_servers):
    print("\nAvailable Servers:")
    for index, server in enumerate(available_servers, start=1):
        print(f"{index}. {server}")
    print(f"{len(available_servers) + 1}. Add a new server")

    while True:
        try:
            choice = int(input(f"Select server {i + 1}: "))
            if 1 <= choice <= len(available_servers):
                selected_servers.append(Waiter(available_servers[choice - 1]))
                break
            elif choice == len(available_servers) + 1:
                new_server = input("Enter new server name: ").strip()
                if new_server:
                    available_servers.append(new_server)
                    save_servers(available_servers)
                    selected_servers.append(Waiter(new_server))
                    break
            print("⚠️ Invalid choice! Try again.")
        except ValueError:
            print("⚠️ Please enter a valid number.")

# Assign sections
assigned_sections = assign_sections(selected_servers, sections)

# Display assignments
print(f"\nShift: {date.today()} - AM")
for section in assigned_sections:
    print(section)