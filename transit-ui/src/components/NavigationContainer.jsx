import React from 'react';
import { Container, Row } from 'react-bootstrap';

import "../styles/NavigationContainer.css";
import NavButton from './common/NavButton';

const NavigationContainer = () => {

    return (
        <div className="navigation-container content">
            <Container>
                <Row>
                    <NavButton variant="outline-primary" to="/">Transit Model</NavButton>
                </Row>
                <Row>
                    <NavButton variant="outline-success" to="/about">The Team</NavButton>
                </Row>
            </Container>
        </div>
    );
}
 
export default NavigationContainer;