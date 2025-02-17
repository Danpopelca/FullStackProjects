from django.shortcuts import render
from django.http import JsonResponse
import json
from services.section_handler import load_section_configurations
from services.data_handler import get_available_servers, save_servers  # Import corect

from django.shortcuts import render
from django.http import JsonResponse
import json
import random
from services.section_handler import load_section_configurations
from services.data_handler import get_available_servers

def assign_sections_view(request):
    """View to assign sections to servers"""
    raw_configurations = load_section_configurations()
    formatted_configurations = {}

    for num_servers, options in raw_configurations.items():
        formatted_configurations[num_servers] = {}

        for key, sections in options.items():
            downstairs = sum(1 for sec in sections if "UPSTAIRS" not in sec and "PORCH" not in sec and "LOUNGE" not in sec)
            upstairs = len(sections) - downstairs
            label = f"DOWNSTAIRS: {downstairs}" + (f" UPSTAIRS: {upstairs}" if upstairs > 0 else "")
            formatted_configurations[num_servers][label] = sections

    servers = sorted(get_available_servers(), key=lambda x: x.lower())
    assigned_sections = None

    if request.method == "POST":
        num_servers = request.POST.get("num_servers")
        selected_config = request.POST.get("section_config")
        selected_servers = request.POST.getlist("servers")

        print("DEBUG - Received Data:")
        print("Num Servers:", num_servers)
        print("Selected Config:", selected_config)
        print("Selected Servers:", selected_servers)  # Ar trebui să fie o listă

        if num_servers and selected_config and len(selected_servers) == int(num_servers):
            sections = formatted_configurations[num_servers][selected_config]
            random.shuffle(selected_servers)  # Amestecăm serverii
            assigned_sections = list(zip(sections, selected_servers))

            print("DEBUG - Assigned Sections:", assigned_sections)  # 🛠️ Debugging

            # Trimite către un template nou (pop-up / pagină nouă)
            return render(request, "core/assigned_sections.html", {
                "assigned_sections": assigned_sections
            })

    return render(request, "core/assign_sections.html", {
        "servers": servers,
        "section_configurations": formatted_configurations
    })
def save_server(request):
    """Save a new server to the JSON file"""
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            new_server = data.get("server", "").strip()

            if new_server:
                servers = get_available_servers()

                if new_server not in servers:
                    servers.append(new_server)
                    save_servers(servers)
                    return JsonResponse({"message": "Server added successfully!", "servers": servers})
                else:
                    return JsonResponse({"message": "Server already exists!", "servers": servers}, status=200)
            else:
                return JsonResponse({"error": "Invalid server name"}, status=400)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid request format"}, status=400)

    return JsonResponse({"error": "Invalid request method"}, status=405)