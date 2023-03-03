import React, { useState } from "react";

import "../styles/ModelContainer.css";
import SelectMenu from "./common/SelectMenu";
import LeafletModule from "./LeafletModule";
//import lines2 from './data/dict2.json';
import { LatLngBounds } from 'leaflet';
import { MapContainer, TileLayer, useMap , Popup } from 'react-leaflet';
import Select from 'react-select';

let batch_lines;
let yyz_lines = []
let ygk_lines = []
//const fs = require('fs');

for (let i = 1; i < 4; i++) {
    yyz_lines.push(require(`./data/yyz_${i}.json`))
    ygk_lines.push(require(`./data/ygk_${i}.json`))
}
let current_city_lines = yyz_lines

let lines = yyz_lines[yyz_lines.length-1]

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

    let options = []
    for (let i = current_city_lines.length; i > 0; i--) {
        options.push({value: i, label: `Number of Lines: ${i}`})
    }

    let [selectedValue, setSelectedValue] = useState(null);
    if (selectedValue === null) {
        selectedValue = options[options.length-1]
    }
    console.log(selectedValue)
        
    if (city === "YYZ") {
        current_city_lines = yyz_lines
        lines = yyz_lines[selectedValue.value-1]
        
    } else if (city == "YGK") {
        current_city_lines = ygk_lines
        lines = ygk_lines[selectedValue.value-1]
    }

    

    //console.log(lines.lines.length)

    
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
                     <SelectMenu
                        className="model-number-of-lines-select"
                        options={options}
                        onSelect={setNumberOfLines}
                     />
                </span>
                <span>
                     <LeafletModule
                         latitude={cityDetails[city].latitude}
                         longitude={cityDetails[city].longitude}
                         zoom={14}
                         markers={markers}
                         lines={lines.lines.slice(0, numberOfLines)}
                     />
                </span>
            </div>
        </div>
    );
};

export default ModelContainer;
