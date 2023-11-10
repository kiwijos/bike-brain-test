function renderMainView() {
    const evtSource = new EventSource("//localhost:1337/eventsource", {
        withCredentials: true,
    });

    let container = document.getElementById("container");

    while (container.firstChild) {
        container.removeChild(container.firstChild);
    }

    container.innerHTML = `<div id="map" class="map"></div>`;

    const map = L.map('map').setView([62.173276, 14.942265], 5);

    L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
        attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
    }).addTo(map);

    evtSource.onmessage = function(event) {
        const data = JSON.parse(event.data);
        const position = JSON.parse(data.geometry);
        const revPos = [position[1], position[0]];

        L.marker(revPos).addTo(map);
    }

}

renderMainView();
