import React from 'react'; // Import React library
import ReactDOM from 'react-dom/client'; // Import ReactDOM for rendering
import App from './App'; // Import the main App component
import './index.css'; // Import global styles

ReactDOM.createRoot(document.getElementById('root')).render( // Create and render the React root
  <React.StrictMode>
    <App />
  </React.StrictMode>
);