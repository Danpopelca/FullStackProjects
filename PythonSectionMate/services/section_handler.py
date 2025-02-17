import json

SECTION_FILE = "sections.json"

def load_section_configurations():
    """Load section configurations from JSON or use default if file doesn't exist"""
    default_configurations = {
        3: {"DOWNSTAIRS": ["YELLOW", "BLUE", "RED"]},
        4: {
            "DOWNSTAIRS": ["YELLOW", "BLUE", "RED", "GREEN"],
            "MIXED": ["YELLOW", "BLUE", "RED", "UPSTAIRS"]
        },
        5: {
            "DOWNSTAIRS": ["YELLOW", "BLUE", "RED", "GREEN", "PINK"],
            "MIXED": ["YELLOW", "BLUE", "RED", "GREEN", "UPSTAIRS"]
        },
        6: {
            "DOWNSTAIRS": ["YELLOW", "BLUE", "RED", "GREEN", "PINK", "UPSTAIRS"],
            "MIXED": ["YELLOW", "BLUE", "RED", "GREEN", "UPSTAIRS LEFT", "UPSTAIRS RIGHT"]
        },
        7: {
            "DOWNSTAIRS": ["YELLOW", "BLUE", "RED", "GREEN", "PINK", "PURPLE", "UPSTAIRS"],
            "MIXED": ["YELLOW", "BLUE", "RED", "GREEN", "PINK", "UPSTAIRS LEFT", "UPSTAIRS RIGHT"]
        },
        8: {
            "MIXED": ["YELLOW", "BLUE", "RED", "GREEN", "PINK", "PURPLE", "UPSTAIRS LEFT", "UPSTAIRS RIGHT"]
        },
        9: {
            "MIXED": ["YELLOW", "BLUE", "RED", "GREEN", "PINK", "PURPLE", "UPSTAIRS LEFT", "UPSTAIRS RIGHT"],
            "EXTENDED": ["YELLOW", "BLUE", "RED", "GREEN", "PINK", "PURPLE", "UPSTAIRS LEFT", "UPSTAIRS RIGHT", "LOUNGE"]
        },
        10: {
            "MIXED": ["YELLOW", "BLUE", "RED", "GREEN", "PINK", "PURPLE", "TEAL", "UPSTAIRS LEFT", "UPSTAIRS RIGHT", "LOUNGE"]
        }
    }

    try:
        with open(SECTION_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        with open(SECTION_FILE, "w", encoding="utf-8") as f:
            f.write(json.dumps(default_configurations, ensure_ascii=False, indent=4))
        return default_configurations