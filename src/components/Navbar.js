import React from 'react';
import {useRef} from "react";
import "./Navbar.css";
import logo from "/Users/amenasyed/frontend/src/images/moodFM_logo.png";
import profile from "/Users/amenasyed/frontend/src/images/profile.png";

function Navbar() {

    const navRef = useRef();

    const showNavbar = () => {
        navRef.current.classList.toggle("responsive_nav");
    }

    return (
        <div className="navigation">
            <header className="nav-container">
            <a href="/home" className="nav-logo">
                <img src={logo} height="50"></img>
            </a>

            <nav className="nav-menu" ref={navRef}>
                <div className="nav-button">
                    <a href="/home" className="nav-item">Home</a>
                </div>

                <div className="nav-button">
                    <a href="/insights" className="nav-item">Insights</a>
                </div>

                <div className="nav-button">
                    <a href="/profile" className="nav-profile">
                        <img src={profile} height="45"></img>
                    </a>
                </div>
            </nav>

         </header>
        </div>
    );
}

export default Navbar;