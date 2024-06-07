import React from 'react';

function Footer() {
  return (
    <footer className="bg-light py-4 mt-5">
      <div className="container">
        <div className="row">
          <div className="col-md-12 col-lg-12 col-xl-12 text-center">
            <h5>Contact Us</h5>
            <p>
              123 Main Street<br />
              Anytown, USA 12345<br />
              Email: info@example.com<br />
              Phone: (123) 456-7890
            </p>
          </div>
        </div>
        <div className="text-center mt-3">
          <p className="mb-0">&copy; 2024 My Website. All rights reserved.</p>
        </div>
      </div>
    </footer>
  );
}

export default Footer;