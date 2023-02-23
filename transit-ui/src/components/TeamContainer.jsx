import React from 'react';
import {Row, Col} from 'react-bootstrap';

import Profile from './common/Profile';

import profileData from "../profiles.json"
import "../styles/TeamContainer.css";

const TeamContainer = () => {

    return (
        <div className="team-container content">
            <h3>About Us</h3>
            <h6>This Transit AI project is developed in 2022-2023 by QMIND's Transit AI Team.<br />
                Director of Design: Jacob Laframboise (not pictured)<br />
                Project Manager: George Trieu
            </h6>
            <Row className="justify-content-md-center">
                {profileData.map((profile) => (
                    <Col key={profile.name + "_col"} sm={2}>
                        <Profile
                            key={profile.name + "_profile"}
                            data={profile}
                        />
                    </Col>
                ))}
            </Row>
        </div>
    );
}
 
export default TeamContainer;