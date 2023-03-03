import React, { useState } from "react";

import "../styles/ModelContainer.css";
import SelectMenu from "./common/SelectMenu";
import LeafletModule from "./LeafletModule";

let yyz_lines = [];
let yvr_lines = [];
let yyc_lines = [];

for (let i = 1; i <= 10; i++) {
    yyz_lines.push(require(`../data/yyz_${i}.json`));
    yvr_lines.push(require(`../data/yvr_${i}.json`));
    yyc_lines.push(require(`../data/yyc_${i}.json`));
}
let current_city_lines = yyz_lines;

let lines = yyz_lines[yyz_lines.length - 1];

const cityDetails = {
    YYZ: {
        name: "Toronto",
        latitude: 43.71716,
        longitude: -79.3815,
    },
    YVR: {
        name: "Vancouver",
        latitude: 49.28012,
        longitude: -123.12082,
    },
    YYC: {
        name: "Calgary",
        latitude: 51.04735,
        longitude: -114.06953,
    },
};

const ModelContainer = () => {
    const cityOptions = Object.entries(cityDetails).map(([key, value]) => ({
        option: value.name,
        value: key,
    }));

    const [city, setCity] = useState(cityOptions.at(0).value);

    let lineOptions = [];
    for (let i = current_city_lines.length; i > 0; i--) {
        lineOptions.push({ value: i, option: `Number of Lines: ${i}` });
    }

    const [numLines, setNumLines] = useState(lineOptions.at(0).value);

    if (city === "YYZ") {
        current_city_lines = yyz_lines;
        lines = yyz_lines[numLines - 1];
    } else if (city == "YVR") {
        current_city_lines = yvr_lines;
        lines = yvr_lines[numLines - 1];
    } else if (city == "YYC") {
        current_city_lines = yyc_lines;
        lines = yyc_lines[numLines - 1];
    }

    return (
        <div className="model-container content">
            <div>
                <h3>Transit AI Predictor</h3>
                <p>Optimized subway lines for Toronto, Vancouver and Calgary</p>
            </div>
            <div>
                <span>
                    <SelectMenu
                        className="model-location-select"
                        onSelect={setCity}
                        options={cityOptions}
                    />
                    <SelectMenu
                        className="model-lines-select"
                        onSelect={setNumLines}
                        options={lineOptions}
                    />
                    <h6 className="model-location">Now Showing: {city}</h6>
                </span>
                <LeafletModule
                    latitude={cityDetails[city].latitude}
                    longitude={cityDetails[city].longitude}
                    zoom={11}
                    lines={lines.lines}
                />
            </div>
        </div>
    );
};

export default ModelContainer;
