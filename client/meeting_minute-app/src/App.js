import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';

import HomePage from './Components/HomePage';
import AudioUploaderEnglish from './Components/AudioUploaderEnglish';
import AudioUploaderBangla from './Components/AudioUploaderBangla';
import AudioUploaderHindi from './Components/AudioUploaderHindi';

const App = () => {
  return (
    <Router>
      <div>
        <Routes>
          <Route exact path="/" element={<HomePage />} />
          <Route path="/bangla" element={<AudioUploaderBangla />} />
          <Route path="/hindi" element={<AudioUploaderHindi />} />
          <Route path="/english" element={<AudioUploaderEnglish />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
