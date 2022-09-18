import React from "react";
import "./Landing.css"
import logo from "./Assets/logo_0_chill.png";

function Landing() {
    return (
        <div className="landing-container">
            <div className="landing-content">
                <img src={logo} height="300"></img>
                <h1 style={{ marginLeft: 0 }}>mood FM</h1>
                <h3>Find the perfect movie soundtrack to each moment of your life.</h3>
                <div className="button-container">
                    <a className="button" href="/home">Let's Get Started</a>
                </div>
                <p>Don’t have an account? <a href="#">Sign up here.</a></p>
            </div>
        </div>
    );
}

export default Landing;