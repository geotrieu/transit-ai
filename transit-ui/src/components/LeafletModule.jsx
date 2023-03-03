import React from "react";
import { MapContainer } from "react-leaflet/MapContainer";
import { TileLayer } from "react-leaflet/TileLayer";
import { Marker, Polyline, Popup, useMap, CircleMarker } from "react-leaflet";
import "../styles/LeafletModule.css";

const DEFAULT_ZOOM = 10;

const ChangeView = ({ center, zoom }) => {
    const map = useMap();
    map.setView(center, zoom);
};

const LeafletModule = ({
    latitude,
    longitude,
    zoom,
    markers = [],
    lines = [],
}) => {
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
            {markers.map((marker) => (
                <Marker
                    key={marker.key}
                    position={[marker.latitude, marker.longitude]}
                ></Marker>
            ))}
            {lines.map((line) => (
                <Polyline
                    pathOptions={{ color: `${line["colour"]}` }}
                    positions={line["stations"].map((station) => [
                        station["lat"],
                        station["long"],
                    ])}
                ></Polyline>
            ))}
            {lines.map((line) =>
                line["stations"].map((station) => {
                    if (station["station"]) {
                        //return <Marker position={[station["lat"],station["long"]]}></Marker>
                        return (
                            <CircleMarker
                                key={[station["lat"], station["long"]]}
                                center={[station["lat"], station["long"]]}
                                radius={4}
                                pathOptions={{
                                    weight: 2,
                                    color: "black",
                                    fillOpacity: 1,
                                    fillColor: "white",
                                }}
                            ></CircleMarker>
                        );
                    }
                })
            )}
        </MapContainer>
    );
};

export default LeafletModule;
