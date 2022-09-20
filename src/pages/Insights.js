import React from 'react';
import "./Insights.css";
import Navbar from "../components/Navbar";
import {Grid} from "@mui/material";
import breakdown from "../images/breakdown.svg";
import lineChart from "../images/line-chart.svg";
import barChart from "../images/bar-chart.svg";


function Insights() {
    return (
        <div className="insights-container">
            <Navbar></Navbar>

            <div className="insights-content">
                <h1>Your 7-Day Insights.</h1>

                <Grid container className="mood-trends" spacing={2}>
                    <Grid item className="card-text" md={6} xs={6}>
                        <h3 className="card-title">Mood Trends.</h3>
                        <img src={lineChart} alt="line-chart"></img>
                    </Grid>
                </Grid>

                <Grid container className="mood-trends" spacing={2}>
                    <Grid item className="card-text" md={8} xs={12}>
                        <h3 className="card-title">Your Mood Breakdown.</h3>
                                
                        <div className="bar-chart">
                            <img src={barChart} alt="bar-chart"></img>
                        </div>
                    </Grid>

                    <Grid item className="breakdown-icon" md={4} xs={12}>
                        <img src={breakdown} alt="breakdown" height="150"></img>
                    </Grid>
                </Grid>
            </div>
        </div>
    );
}

export default Insights;