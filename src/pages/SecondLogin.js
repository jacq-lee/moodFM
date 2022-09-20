import React from 'react';
import "./SecondLogin.css";
import logo from "../images/logo.png";
import {Grid} from "@mui/material";

function SecondLogin() {
    return (
        <div className="second-login-container">
            <div className="login-heading">
                <h1>Welcome Back!</h1>
                <p>Login below.</p>
            </div>

            <Grid container className="login-box-container">
                <Grid item md={12} xs={12}>
                    <div className="login-box">
                        <img className="login-image" src={logo} height="200"></img>

                        <form className="login-form">
                            <label className="login-labels" for="fname">Email</label><br></br>
                            <input className="login-boxes" type="text" id="fname" name="fname"></input><br></br>
                            <label className="login-labels" for="lname">Password</label><br></br>
                            <input className="login-boxes"type="password" id="lname" name="lname"></input><br></br>
                        </form>

                        <div className="login-button">
                            <a className="button" href="/read-room">Sign In</a>
                        </div>
                        <a className="linked-text" href="#">Forgot Password.</a>
                    </div>
                </Grid>
            </Grid>
        </div>
    );
}

export default SecondLogin;