import React, { useCallback } from "react";
import { Button } from "react-bootstrap";
import { useHistory } from "react-router-dom";

import "../../styles/common/NavButton.css";

const NavButton = ({variant, to, children}) => {
    const history = useHistory();
    const handleNavigation = useCallback(() => history.push(to), [to, history]);

    return (
        <Button className="nav-button" onClick={handleNavigation} variant={variant}>{children}</Button>
    )
}

export default NavButton;