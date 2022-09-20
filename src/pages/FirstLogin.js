import React from 'react';
import "./FirstLogin.css";
import logo from "../images/logo.png";

function FirstLogin() {
    return (
        <div className="first-login-container">
            <img src={logo} height="250"></img>
            <h1>mood FM</h1>
            <h3>Find the perfect movie soundtrack to each moment of your life</h3>
            <div className="login-button">
                <a className="button" href="/login">Sign In</a>
            </div>
            <p>Don’t have an account? <a className="linked-text" href="#">Sign up here.</a></p>

        </div>
    );
}

export default FirstLogin;