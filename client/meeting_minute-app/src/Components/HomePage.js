import React from 'react';
import { Link } from 'react-router-dom';
import Navbar from './Navbar';
import './HomePage.css'; // Import CSS file for HomePage styling

const HomePage = () => {
  return (
    <div>
      <Navbar />
      <div className="home-page-container">
        <h1>Welcome to Frisbee: Your Helpful Meeting Summarizer</h1> {/* Animated intro */}
        <h3>Select Language To Summarize</h3>
        <div className="button-container">
          <Link to="/bangla" className="language-button">
            Bangla
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
