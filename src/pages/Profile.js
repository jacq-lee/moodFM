import React from 'react';
import "./Profile.css";
import Navbar from "../components/Navbar";
import profile2 from "../images/profile.svg";

function Profile() {
    return (
        <div className="profile-container">
            <Navbar></Navbar>

            <div className="profile-content">
                <img src={profile2} height="150"></img>
                <h2 className="profile-name">Mr. Goose</h2>
                <h4 className="profile-text">garygoose@uwaterloo.ca</h4>
                <h4 className="profile-text">(123) - 456 - 7890</h4>
                
                <div className="sign-out">
                    <a className="button" href="/">Log Out</a>
                </div>

                <hr className="horizontal-rule"></hr>
            </div>
        </div>
    );
}

export default Profile;