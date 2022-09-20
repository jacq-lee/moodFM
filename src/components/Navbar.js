import React from 'react';
import {useRef} from "react";
import "./Navbar.css";
import {Grid} from  "@mui/material";
import logo from "../images/logo.png";
import profile from "../images/profile.png";

function Navbar() {

    const navRef = useRef();

    const showNavbar = () => {
        navRef.current.classList.toggle("responsive_nav");
    }

    return (
        <div className="navigation">
            <header className="nav-container">
                <Grid container spacing={2} p={12}>
                    <Grid item md={1} xs={1} className="nav-logo-container">
                        <a href="/" className="nav-logo">
                            <img src={logo} alt="logo" height="50"></img>
                        </a>
                    </Grid>

                    <Grid item md={11} xs={11}>
                        <nav className="nav-menu" ref={navRef}>
                            <div className="nav-button">
                                <a href="/home" className="nav-item">Home</a>
                            </div>

                            <div className="nav-button">
                                <a href="/insights" className="nav-item">Insights</a>
                            </div>

                            <a href="/profile" className="nav-profile">
                                <img src={profile} alt="profile-logo" height="45"></img>
                            </a>
                        </nav>
                    </Grid>
                </Grid>
            </header>
        </div>
    );
}

export default Navbar;