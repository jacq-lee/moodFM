import React from "react";
import Navbar from "./components/Navbar";
import profile from "/Users/amenasyed/frontend/src/images/profile.png";
import "./Profile.css"

function Profile() {
    return (
        <div className="profile-container">
            <Navbar></Navbar>

            <div className="profile-content">
                <img src={profile} height="100"></img>
                <h1>Mr. Goose</h1>
                <h3>mr.goose@gmail.com</h3>
                <h3>(123) - 456 - 7890</h3>
            </div>
        </div>
    );
}

export default Profile;