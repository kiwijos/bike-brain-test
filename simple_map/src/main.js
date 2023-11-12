function renderMainView() {
    const evtSource = new EventSource("http://localhost:1337/eventsource", {
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

    let markers = {};

    evtSource.onmessage = function(event) {
        const data = JSON.parse(event.data);
        let marker;

        if (data.id in markers) {
            marker = markers[data.id];
            marker.setLatLng(data.geoJSON.geometry.coordinates)
        } else {
            marker = L.marker(data.geoJSON.geometry.coordinates);
            markers[data.id] = marker;
            marker.addTo(map);
        }


    }

    evtSource.onerror = function(event) {
        console.error("EventSource failed:", event);
    };

}

renderMainView();
