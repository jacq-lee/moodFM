import React from 'react';
import "./HomePressed.css";
import Navbar from '../components/Navbar';
import {Grid} from "@mui/material";
import happy from "../images/happy.gif";
import playButtons from "../images/play-buttons.svg";
import playBar from "../images/play-bar.svg";
import breakdown from "../images/breakdown.svg";
import pieChart from "../images/pie-chart.svg";

function HomePressed() {
    return (
        <div className="home-pressed-container">
            <Navbar></Navbar>

            <div className="home-content">
                <h1>Hey Mr. Goose!</h1>

                <div className="home-row">
                    <div className="read-room-link">
                        <Grid container className="read-the-room-happy" spacing={2}>
                            <Grid item className="card-text" md={12} xs={12}>
                                <h3 className="card-title">You're feeling Happy.</h3>
                                <div className="centered-card-text">
                                    <p className="card-content bolded-text song">Happy</p>
                                    <p className="card-content bolded-text song">Pharrell Williams</p>
                                    <img src={playButtons} alt="play-buttons"></img><br></br>
                                    <img src={playBar} alt="play-bar"></img>
                                </div>
                            </Grid>
                        </Grid>

                        <Grid container className="mood-breakdown-home" spacing={2}>
                            <Grid item className="card-text" md={8} xs={12}>
                                <h3 className="card-title">Your Mood Breakdown.</h3>
                                
                                <div className="pie-chart">
                                    <img src={pieChart} alt="pie-chart"></img>
                                    <p className="card-content pie-text">40% Happy</p>
                                </div>
                            </Grid>

                            <Grid item className="headphone-icon" md={4} xs={12}>
                                <img src={breakdown} alt="breakdown" height="150"></img>
                            </Grid>
                        </Grid>
                    </div>

                    <img src={happy} alt="homepage-gif" className="homepage-gif"></img>
                </div>
                
            </div>
        </div>
    );
}

export default HomePressed;