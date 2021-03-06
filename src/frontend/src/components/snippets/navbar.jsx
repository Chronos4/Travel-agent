import React from 'react';


const Navbar = (props) => {
    return (
        <nav class="navbar navbar-light bg-light navbar-expand-md shadow-lg fixed">
    <a id="navbar-img" class="navbar-brand font-italic ml-5 display-5" href="/">TraveliT</a>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navNavId"
        aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navNavId">
        <ul class="navbar-nav mx-auto font-weight-bold">
            <li class="nav-item active">
                <a class="nav-link" href="/"><i class="fas fa-home"></i> Home
                    <span class="sr-only">(current)</span></a>
            </li>
            <li class="nav-item">
                <a class="nav-link" href="#"><i class="fas fa-globe-africa"></i>
                    Destinations</a>
            </li>
            <li class="nav-item">
                <a class="nav-link " href="{% url 'login' %}"><i class="fas fa-sign-in-alt"></i> Login</a>
            </li>
            <li class="nav-item">
                <a class="nav-link " href="#"><i class="fas fa-bell"></i> Notifications</a>
            </li>
            <li class="nav-item dropdown">
                <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown"
                    aria-haspopup="true" aria-expanded="false">
                    <i class="fas fa-user-circle"></i> Account
                </a>
                <div class="dropdown-menu" aria-labelledby="navbarDropdown">
                    <a class="dropdown-item" href="#">Profile</a>
                    <a class="dropdown-item" href="#">Settings</a>
                    <div class="dropdown-divider"></div>
                    <a class="dropdown-item" href="#">Logout</a>
                </div>
            </li>
        </ul>
    </div>
</nav>
    );
}


export default Navbar;