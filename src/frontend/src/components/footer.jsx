import React from 'react';


const Footer = (props) => {
    return (
        <footer class="page-footer  font-small blue pt-4">
    <div class="row text-center">
	        <div class="col-md-4 my-3">
	            <h3 class="mb-3">About us</h3>
	            <p class="lead">
	                A small team trying to help each other meet new people, make friends
	                and travel all over the world.Our target? Even the lonely ones will have
	                a partner to travel.
	            </p>
	        </div>
	        <div class="col-md-4 my-3">
	            <h3 class="mb-4">Our Location </h3>
	         
	        </div>
	        <div class="col-md-4 my-3">
	            <h3>Contact Us</h3>
	            <ul class="mt-4">
	                <li>Phone : 123 - 456 - 789</li>
	                <li>E-mail : info@comapyn.com</li>
	                <li>Fax : 123 - 456 - 789</li>
	            </ul>
	            <p class="lead">
	                For any information that you need you are free to contact with us!
	            </p>
	        </div>
	        <div class="footer-copyright text-center py-3 mx-auto">© 2018 Copyright:
	            <a href="#"> TraveliT team</a>
	        </div>
      </div>
</footer>
    );
}


export default Footer;