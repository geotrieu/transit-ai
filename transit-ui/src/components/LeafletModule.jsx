import React from "react";
import { MapContainer } from "react-leaflet/MapContainer";
import { TileLayer } from "react-leaflet/TileLayer";
import { Marker, Polyline, Popup, useMap } from "react-leaflet";

import "../styles/LeafletModule.css";

const DEFAULT_ZOOM = 10;

const ChangeView = ({ center, zoom }) => {
    const map = useMap();
    map.setView(center, zoom);
};

const LeafletModule = ({ latitude, longitude, zoom, markers, lines }) => {
    const zoomLevel = zoom ? zoom : DEFAULT_ZOOM;
    console.log(markers);
    return (
        <MapContainer
            className="leaflet-map"
            center={[latitude, longitude]}
            zoom={zoomLevel}
            scrollWheelZoom={true}
        >
            <ChangeView center={[latitude, longitude]} zoom={zoomLevel} />
            <TileLayer
                attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
                url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
            />
            {markers.map((marker) => (
                <Marker
                    key={marker.key}
                    position={[marker.latitude, marker.longitude]}
                >
                    <Popup>{marker.text}</Popup>
                </Marker>
            ))}
            {lines.map((line) => (
                <Polyline
                    positions={line}
                >
                </Polyline>
            ))}

        </MapContainer>
    );
};

export default LeafletModule;
