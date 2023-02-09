import React from "react";
import { Form } from "react-bootstrap";

const SelectMenu = ({ className, options, onSelect }) => {
    const handleSelect = (e) => {
        onSelect(e.target.value);
    };

    return (
        <div className={className}>
            <Form.Select onChange={handleSelect}>
                {options.map((o) => {
                    const val = o.value ? o.value : o.option;
                    return (
                        <option key={o.option} value={val}>
                            {o.option}
                        </option>
                    );
                })}
            </Form.Select>
        </div>
    );
};

export default SelectMenu;
