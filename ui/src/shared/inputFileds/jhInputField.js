import React, { useState } from 'react';

import "./Choice.css"
const FormSection = (props) => {
    const [testVal, setTestVal] = useState("");

    const textChangeHandler = () => {
        setTestVal()
        props.onEmail(testVal);
    }
    return (
        <div className='text-box'>
            <label>{this.props.fieldName}</label>
            <input type={'text'} placeholder={this.props.placeholder} onChange={textChangeHandler} />
        </div>
    )
}

export default FormSection
