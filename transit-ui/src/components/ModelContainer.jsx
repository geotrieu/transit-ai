import React, { useState } from "react";

import "../styles/ModelContainer.css";
import SelectMenu from "./common/SelectMenu";
import LeafletModule from "./LeafletModule";
import lines from './data/dict.json';
import json_data from './dict.json';
import { LatLngBounds } from 'leaflet';
import { MapContainer, TileLayer, useMap , Popup } from 'react-leaflet'
import Select from 'react-select';

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
    
    const options = [
        { value: 'option1', label: 'Number of Lines: 6' },
        { value: 'option2', label: 'Number of Lines: 5' },
        { value: 'option3', label: 'Number of Lines: 4' },
        { value: 'option4', label: 'Number of Lines: 3' },
        { value: 'option5', label: 'Number of Lines: 2' },
        { value: 'option6', label: 'Number of Lines: 1' },
    ];

    const customStyles = {
        option: (provided, state) => ({
        ...provided,
        zIndex: 9999,
    }),
        menu: (provided, state) => ({
        ...provided,
        zIndex: 9999,
        width: '375px',
        minHeight: '30px',
    }),
        control: (provided, state) => ({
        ...provided,
        width: '375px',
        minHeight: '30px',
    }),
    };
    
    const [selectedValue, setSelectedValue] = useState(null);

    return (
        <div className="model-container content">
            <div>
                <h3>Transit AI Predictor</h3>
                <p>
                    There are pins for Toronto, Vancouver, and Kingston.
                </p>
            </div>
            <div>
                <span>
                    <SelectMenu
                        className="model-location-select"
                        onSelect={setCity}
                        options={cityOptions}
                    />
                    <h6 className="model-location">Now Showing: {city}</h6>
                </span>
                <span>
                    <Select
                         options={options}
                         value={selectedValue}
                         onChange={setSelectedValue}
                         styles={customStyles}
                    />
                </span>
                <LeafletModule
                    latitude={cityDetails[city].latitude}
                    longitude={cityDetails[city].longitude}
                    zoom={14}
                    markers={markers}
                    lines={lines}
                />
            </div>
        </div>
    );
};

export default ModelContainer;
