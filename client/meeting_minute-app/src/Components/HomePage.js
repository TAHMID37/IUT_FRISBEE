import React from 'react';
import { Link } from 'react-router-dom';
import Navbar from './Navbar';
import './HomePage.css'; // Import CSS file for HomePage styling

const HomePage = () => {
  return (
    <div>
      <Navbar />
      <div className="home-page-container">
        <h1>Welcome to Meeting Minutes</h1> {/* Animated intro */}
        <h1>Select Language</h1>
        <div className="button-container">
          <Link to="/bangla" className="language-button">
            Bengali
          </Link>
          <Link to="/hindi" className="language-button">
            Hindi
          </Link>
          <Link to="/english" className="language-button">
            English
          </Link>
        </div>
      </div>
    </div>
  );
};

export default HomePage;
