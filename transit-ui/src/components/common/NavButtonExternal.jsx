import React, { useCallback } from "react";
import { Button } from "react-bootstrap";
import { useHistory } from "react-router-dom";

import "../../styles/common/NavButton.css";

const NavButtonExternal = ({ variant, to, children }) => {
    const history = useHistory();
    const handleNavigation = () => {
        window.open(to, "_blank");
    };

    return (
        <Button
            className="nav-button"
            onClick={handleNavigation}
            variant={variant}
        >
            {children}
        </Button>
    );
};

export default NavButtonExternal;
