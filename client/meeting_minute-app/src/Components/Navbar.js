import React from 'react';
import { Link } from 'react-router-dom';
import './Navbar.css'; // Import CSS file for custom styles

const Navbar = () => {
  return (
    <nav className="navbar navbar-expand-lg navbar-dark" style={{ backgroundColor: '#4d637a' }}>
      <div className="container">
        <Link className="navbar-brand navbar-brand-hover" to="/">Meeting Minutes</Link>
        <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
          <span className="navbar-toggler-icon"></span>
        </button>
        <div className="collapse navbar-collapse" id="navbarNav">
          <ul className="navbar-nav ml-auto">
            <li className="nav-item">
              <Link className="nav-link" to="/bangla" style={{ fontSize: '18px' }}>Bangla</Link>
            </li>
            <li className="nav-item">
              <Link className="nav-link" to="/hindi" style={{ fontSize: '18px' }}>Hindi</Link>
            </li>
            <li className="nav-item">
              <Link className="nav-link" to="/english" style={{ fontSize: '18px' }}>English</Link>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
