import React from 'react';
import "./Home.css";
import Navbar from "../components/Navbar";
import {Grid} from "@mui/material";
import headphones from "../images/headphones.svg";
import chill from "../images/chill.gif";

function Home() {
    return (
        <div className="home-container">
            <Navbar></Navbar>

            <div className="home-content">
                <h1>Hey Mr. Goose!</h1>
                <div className="home-row">
                    <a className="read-room-link" href="/home">
                        <Grid container className="read-the-room" spacing={2}>
                            <Grid item className="card-text" md={8} xs={12}>
                                <h3 className="card-title">Read the Room.</h3>
                                <p className="card-content">You’re one step away from your personalized mixtape!</p>
                                <p className="card-content">Click here and scan your conversation to start.</p>
                            </Grid>

                            <Grid item className="headphone-icon" md={4} xs={12}>
                                <img src={headphones} alt="headphones"></img>
                            </Grid>
                        </Grid>
                    </a>

                    <img src={chill} alt="homepage-gif" className="homepage-gif"></img>
                </div>
                
            </div>
        </div>
    );
}

export default Home;