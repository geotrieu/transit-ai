import React, { useState } from "react";

import "../styles/ModelContainer.css";
import SelectMenu from "./common/SelectMenu";
import LeafletModule from "./LeafletModule";

const cityDetails = {
    YYZ: {
        name: "Toronto",
        latitude: 43.65628,
        longitude: -79.38836,
    },
    YVR: {
        name: "Vancouver",
        latitude: 49.28012,
        longitude: -123.12082,
    },
    YGK: {
        name: "Kingston",
        latitude: 44.22528,
        longitude: -76.49514,
    },
};

const markers = [
    {
        key: "YYZ",
        latitude: 43.65628,
        longitude: -79.38836,
        text: "Toronto YYZ Marker",
    },
    {
        key: "YVR",
        latitude: 49.28012,
        longitude: -123.12082,
        text: "Vancouver YVR Marker",
    },
    {
        key: "YGK",
        latitude: 44.22528,
        longitude: -76.49514,
        text: "Kingston YGK Marker",
    },
];

const lines = [
    [
        [44.218484107467475, -76.56439441051982], 
        [44.24979684107127, -76.39842891483462], 
        [44.15450479769611, -76.2435922683199]
    ],
    [
        [43.76147441459196, -79.39056394143952], 
        [43.66411994511931, -79.21264095321258], 
        [43.58931322232908, -79.55104767580175],
        [43.82549135563934, -79.63611722712024]
    ],
];

const ModelContainer = () => {
    const cityOptions = Object.entries(cityDetails).map(([key, value]) => ({
        option: value.name,
        value: key,
    }));

    const [city, setCity] = useState(cityOptions.at(0).value);

    return (
        <div className="model-container content">
            <h3>Transit AI Predictor</h3>
            <p>
                There are pins for Toronto, Vancouver, and Kingston.
            </p>
            <span>
                <SelectMenu
                    className="model-location-select"
                    onSelect={setCity}
                    options={cityOptions}
                />
                <h6 className="model-location">Now Showing: {city}</h6>
            </span>
            <LeafletModule
                latitude={cityDetails[city].latitude}
                longitude={cityDetails[city].longitude}
                zoom={14}
                markers={markers}
                lines={lines}
            />
        </div>
    );
};

export default ModelContainer;
