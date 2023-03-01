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
                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
                eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut
                enim ad minim veniam, quis nostrud exercitation ullamco laboris
                nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor
                in reprehenderit in voluptate velit esse cillum dolore eu fugiat
                nulla pariatur. Excepteur sint occaecat cupidatat non proident,
                sunt in culpa qui officia deserunt mollit anim id est laborum.
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
            />
        </div>
    );
};

export default ModelContainer;
