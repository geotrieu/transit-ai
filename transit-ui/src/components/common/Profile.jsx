import React from "react";
import EmailLink from "./EmailLink";

import "../../styles/common/Profile.css"

const Profile = ({ data }) => {
    return (
        <div>
            <img
                className="profileImage"
                alt={data.name}
                width="100%"
                src={data.img}
            ></img>
            <p>
                <br />
                <b>{data.name}</b>
                <br />
                {data.program}
                <br />
                {data.organization}
                <br />
                <EmailLink email={data.email} />
            </p>
        </div>
    );
};

export default Profile;