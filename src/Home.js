import React from "react";
import Navbar from "./components/Navbar";
import "./Home.css"
import readroom from "/Users/amenasyed/frontend/src/images/read-room.png";
import breakdown from "/Users/amenasyed/frontend/src/images/mood-breakdown.png";
import chill from "/Users/amenasyed/frontend/src/images/chill.gif";

function Home() {
    return (
        <div className="home-container">
            <Navbar></Navbar>

            <h1>Hey there!</h1>

            <div className="read">
                <div className="row">
                    
                    <img src={readroom} ></img>
                    <img src={chill} height="300"></img>
                </div>

                <div className="row-2">
                    
                    <img src={breakdown} ></img>
                </div>
                

            </div>
        </div>
    );
}

export default Home;