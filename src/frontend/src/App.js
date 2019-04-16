import React, { Component } from 'react';
import './App.css';
import Navbar from './components/navbar';
import Footer from './components/footer';

class App extends Component {
  render() {
    return (
      <div className="App">
        <Navbar />
        <Footer />
      </div>
    );
  }
}

export default App;
