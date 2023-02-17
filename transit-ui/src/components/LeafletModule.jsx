import React from "react";
import { MapContainer } from "react-leaflet/MapContainer";
import { TileLayer } from "react-leaflet/TileLayer";
import { CircleMarker, Polyline, Popup, useMap } from "react-leaflet";

import "../styles/LeafletModule.css";

const DEFAULT_ZOOM = 10;

const ChangeView = ({ center, zoom }) => {
    const map = useMap();
    map.setView(center, zoom);
};

const LeafletModule = ({ latitude, longitude, zoom, markers, lines }) => {
    const zoomLevel = zoom ? zoom : DEFAULT_ZOOM;
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
            {lines.map((line) => (
                <Polyline
                    key={line.key}
                    positions={line.positions}
                    pathOptions={{
                        weight: 5,
                        color: line.color,
                        smoothFactor: 5,
                    }}
                />
            ))}
            {markers.map((marker) => (
                <CircleMarker
                    key={marker.key}
                    center={[marker.latitude, marker.longitude]}
                    radius={5}
                    pathOptions={{
                        weight: 2,
                        color: "black",
                        fillOpacity: 0.8,
                        fillColor: "white",
                    }}
                >
                    {marker.text ? <Popup>{marker.text}</Popup> : <></>}
                </CircleMarker>
            ))}
        </MapContainer>
    );
};

export default LeafletModule;
