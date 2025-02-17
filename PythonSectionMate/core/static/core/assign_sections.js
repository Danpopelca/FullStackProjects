document.addEventListener("DOMContentLoaded", function() {
    let sectionConfigurations = JSON.parse(document.getElementById("section_configurations").textContent);
    let availableServers = JSON.parse(document.getElementById("server_list").textContent);
    let selectedServers = [];

    function updateSections() {
        let numServers = document.getElementById("num_servers").value;
        let sectionDropdown = document.getElementById("section_config");
        let sectionLabel = document.getElementById("section_label");

        sectionDropdown.innerHTML = "";
        document.getElementById("server_selection").style.display = "none";

        if (numServers && sectionConfigurations[numServers]) {
            sectionLabel.style.display = "block";
            sectionDropdown.style.display = "block";

            let options = Object.keys(sectionConfigurations[numServers]).slice(0, 2);
            sectionDropdown.innerHTML = '<option value="">-- Select --</option>';
            options.forEach(option => {
                let opt = document.createElement("option");
                opt.value = option;
                opt.textContent = option;
                sectionDropdown.appendChild(opt);
            });
        } else {
            sectionLabel.style.display = "none";
            sectionDropdown.style.display = "none";
        }
    }

    function showServerDropdowns() {
        let numServers = parseInt(document.getElementById("num_servers").value);
        let serverDiv = document.getElementById("server_selection");
        serverDiv.innerHTML = "";
        selectedServers = new Array(numServers); // Crează un array gol pentru numărul de ospătari

        if (numServers) {
            serverDiv.style.display = "block";
            addServerDropdown(0, numServers);
        }
    }

    function addServerDropdown(index, total) {
        if (index >= total) {
            generateSections(); // După selectarea ospătarilor, generăm secțiunile
            return;
        }

        let serverDiv = document.getElementById("server_selection");
        let dropdown = document.createElement("select");
        dropdown.className = "form-select mt-2";

        dropdown.onchange = function() {
            let selected = dropdown.value;

            if (selected === "add_new") {
                let newServer = prompt("Enter new server name:");
                if (newServer && !availableServers.includes(newServer)) {
                    availableServers.push(newServer);
                    fetch('/save_server/', {
                        method: 'POST',
                        body: JSON.stringify({ server: newServer }),
                        headers: { 'Content-Type': 'application/json', 'X-CSRFToken': getCSRFToken() }
                    }).then(response => response.json())
                      .then(data => console.log(data));
                }
                updateDropdown(dropdown);
            } else {
                if (selectedServers.includes(selected)) {
                    alert("This server is already assigned.");
                    dropdown.value = ""; // Resetează selecția
                    return;
                }

                selectedServers[index] = selected;
                addServerDropdown(index + 1, total); // Adaugă următorul dropdown
            }
        };

        updateDropdown(dropdown);
        serverDiv.appendChild(dropdown);
    }

    function updateDropdown(dropdown) {
        dropdown.innerHTML = '<option value="">-- Select Server --</option>';

        availableServers.forEach(server => {
            let opt = document.createElement("option");
            opt.value = server;
            opt.textContent = server;
            dropdown.appendChild(opt);
        });

        dropdown.innerHTML += '<option value="add_new">+ Add New Server</option>';
    }

    function generateSections() {
        let numServers = document.getElementById("num_servers").value;
        let selectedSectionConfig = document.getElementById("section_config").value;
        let sectionDiv = document.getElementById("section_display");

        sectionDiv.innerHTML = "";

        console.log("DEBUG - Num Servers:", numServers);
        console.log("DEBUG - Selected Section Config:", selectedSectionConfig);
        console.log("DEBUG - Selected Servers:", selectedServers.filter(s => s));

        if (!numServers || !selectedSectionConfig || selectedServers.includes(undefined)) {
            console.log("DEBUG - Not all servers selected, returning...");
            return;
        }

        let sections = sectionConfigurations[numServers][selectedSectionConfig];

        console.log("DEBUG - Sections:", sections);

        let list = document.createElement("ul");
        list.className = "list-group mt-3";

        sections.forEach((section, index) => {
            let listItem = document.createElement("li");
            listItem.className = "list-group-item";
            listItem.textContent = `Section ${section}: ${selectedServers[index]}`;
            list.appendChild(listItem);
        });

        sectionDiv.appendChild(list);
    }

    function getCSRFToken() {
        return document.querySelector('[name=csrfmiddlewaretoken]').value;
    }

    document.getElementById("num_servers").addEventListener("change", updateSections);
    document.getElementById("section_config").addEventListener("change", showServerDropdowns);
});