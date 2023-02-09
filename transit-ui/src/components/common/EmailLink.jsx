import React from "react";

const EmailLink = ({email}) => {
    return (
        <a href={"mailto:" + email}>
            {email}
        </a>
    )
}

export default EmailLink;