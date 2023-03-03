import React from "react";
import { Container, Row } from "react-bootstrap";

import "../styles/NavigationContainer.css";
import NavButton from "./common/NavButton";
import NavButtonExternal from "./common/NavButtonExternal";

const NavigationContainer = () => {
    return (
        <div className="navigation-container content">
            <Container>
                <Row>
                    <NavButton variant="outline-primary" to="/">
                        Transit Model
                    </NavButton>
                </Row>
                <Row>
                    <NavButton variant="outline-success" to="/about">
                        The Team
                    </NavButton>
                </Row>
                <Row>
                    <NavButtonExternal
                        variant="outline-warning"
                        to="https://github.com/geotrieu/transit-ai"
                    >
                        GitHub
                    </NavButtonExternal>
                </Row>
                <Row>
                    <NavButtonExternal
                        variant="outline-info"
                        to="/CUCAI_Paper_2023.pdf"
                    >
                        Research Paper
                    </NavButtonExternal>
                </Row>
            </Container>
        </div>
    );
};

export default NavigationContainer;
