import json

SERVER_FILE = "servers.json"

# Default server list
DEFAULT_SERVERS = ["Ala", "Alexis", "Andres", "Arely", "Armando", "Audrey", "Caner", "Cathie", "Dan", "Evan", "Gabriel",
                   "Joanet", "Jose", "Josh", "Juliana", "Kate", "Kelsey", "Lana", "Laura", "Layla", "Leah", "Lisbeth",
                   "Lizzy", "Madison", "Madisyn", "Max", "Maya", "Natalya", "Nick", "PJ", "Quy", "Summer", "Tracy"]

def load_servers():
    """Load the list of servers from JSON or use default if file doesn't exist"""
    try:
        with open(SERVER_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        with open(SERVER_FILE, "w", encoding="utf-8") as f:
            json.dump(DEFAULT_SERVERS, f, indent=4, ensure_ascii=False)
        return DEFAULT_SERVERS

def save_servers(new_servers):
    """Load existing servers, add new ones, clean names, remove duplicates, and sort alphabetically"""
    try:
        with open(SERVER_FILE, "r", encoding="utf-8") as f:
            existing_servers = json.load(f)
    except FileNotFoundError:
        existing_servers = []

    # Curățăm numele, eliminăm dublurile și sortăm corect
    cleaned_servers = sorted(
        {server.strip() for server in (existing_servers + new_servers) if server.strip()},
        key=lambda x: x.lower()  # Asigură că sortarea este corectă indiferent de majuscule
    )

    # Verificăm și afișăm pentru debug
    print("DEBUG - Sorted Servers:", cleaned_servers)

    # Salvăm înapoi în fișier (JSON rescris)
    with open(SERVER_FILE, "w", encoding="utf-8") as f:
        json.dump(cleaned_servers, f, indent=4, ensure_ascii=False)
    # Salvăm înapoi în fișier
    with open(SERVER_FILE, "w", encoding="utf-8") as f:
        json.dump(cleaned_servers, f, indent=4, ensure_ascii=False)

def get_available_servers():
    """Return a list of available servers"""
    return load_servers()