import React from "react";
import { Container, Col, Row } from "react-bootstrap";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";

import "../styles/MainContainer.css";
import ModelContainer from "./ModelContainer";
import NavigationContainer from "./NavigationContainer";
import TeamContainer from "./TeamContainer";

const footer = "© 2023 QMIND Transit AI";

const MainContainer = () => {
    return (
        <div className="page">
            <Router>
                <Container>
                    <Row>
                        <Col>
                            <Switch>
                                <Route exact path="/">
                                    <ModelContainer />
                                </Route>
                                <Route path="/about">
                                    <TeamContainer />
                                </Route>
                            </Switch>
                        </Col>
                        <Col xs="auto">
                            <NavigationContainer />
                        </Col>
                    </Row>
                </Container>
            </Router>
            <footer className="footer">{footer}</footer>
        </div>
    );
};

export default MainContainer;
