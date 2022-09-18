import React from "react";
import Navbar from "./components/Navbar";
import "./Insights.css"
import trends from "./images/mood-trends.png";
import breakdown from "./images/mood-breakdown.png";

function Insights() {
    return (
        <div className="insights-container">
            <Navbar></Navbar>
            <h1>Your 7-day Insights</h1>

            <div className="insights-content">
                <h3>Mood Trends</h3>
                <img src={trends} height="250"></img>

            </div>
        </div>
    );
}

export default Insights;