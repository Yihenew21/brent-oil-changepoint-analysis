import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Line } from 'react-chartjs-2';
import { Chart as ChartJS, Title, Tooltip, LineElement, Legend, CategoryScale, LinearScale, PointElement, Filler } from 'chart.js';
import { format } from 'date-fns';

// Register Chart.js components for line chart functionality
ChartJS.register(Title, Tooltip, LineElement, Legend, CategoryScale, LinearScale, PointElement, Filler);

function App() {
  // State to store price data array from API
  const [prices, setPrices] = useState([]);
  
  // State to store change point analysis results
  const [changePoint, setChangePoint] = useState({});
  
  // State to store user-selected date filter for data visualization
  const [filterDate, setFilterDate] = useState('');

  // Effect hook to fetch data from backend API on component mount
  useEffect(() => {
    // Fetch price data from backend
    axios.get('http://localhost:5000/api/prices')
      .then(response => {
        console.log('Raw prices response:', response.data);
        // Handle potential data structure variations - ensure we get an array
        const priceData = Array.isArray(response.data) ? response.data : response.data.prices || [];
        console.log('Processed prices data:', priceData);
        setPrices(priceData);
      })
      .catch(error => console.error('Error fetching prices:', error));
    
    // Fetch change point analysis data from backend
    axios.get('http://localhost:5000/api/change-point')
      .then(response => {
        console.log('Change point data:', response.data);
        setChangePoint(response.data);
      })
      .catch(error => console.error('Error fetching change point:', error));
  }, []);

  // Filter price data based on user-selected date or exclude invalid log returns
  const filteredPrices = filterDate
    ? prices.filter(p => {
        // Extract date portion from datetime string for comparison
        const dateStr = p.Date.split(' ')[0];
        console.log(`Filtering: ${dateStr} vs ${filterDate}`);
        return dateStr === filterDate;
      })
    : // If no date filter, exclude entries with invalid (NaN) log returns
      prices.filter(p => !isNaN(p.Log_Returns));

  console.log('Filtered prices length:', filteredPrices.length);

  // Configure chart data structure for Chart.js Line component
  const chartData = {
    // X-axis labels: extract date portion from datetime strings
    labels: filteredPrices.map(p => p.Date.split(' ')[0]),
    datasets: [
      {
        label: 'Log Returns',
        // Y-axis data: log return values
        data: filteredPrices.map(p => p.Log_Returns),
        borderColor: 'rgba(75,192,192,1)',
        backgroundColor: 'rgba(75,192,192,0.2)',
        fill: true, // Fill area under the line
        // Highlight change point date with larger point radius
        pointRadius: filteredPrices.map((_, i) => {
          const changeDate = changePoint.change_point_date;
          return changeDate && filteredPrices[i]?.Date.split(' ')[0] === changeDate ? 5 : 0;
        }),
        pointHoverRadius: 5,
      },
    ],
  };

  // Configure chart display options and styling
  const options = {
    responsive: true, // Make chart responsive to container size
    scales: {
      x: { title: { display: true, text: 'Date' } },
      y: { title: { display: true, text: 'Log Returns' } },
    },
    plugins: {
      legend: { position: 'top' },
      tooltip: {
        callbacks: {
          // Custom tooltip formatting for better readability
          label: context => `Log Return: ${context.raw}`,
        },
      },
    },
  };

  return (
    <div style={{ padding: '20px', maxWidth: '1200px', margin: '0 auto' }}>
      <h1>Brent Oil Price Analysis Dashboard</h1>
      
      {/* Date filter input for interactive data exploration */}
      <div>
        <label>
          Filter by Date:
          <input
            type="date"
            value={filterDate}
            onChange={e => {
              console.log('New filter date:', e.target.value);
              setFilterDate(e.target.value);
            }}
          />
        </label>
      </div>
      
      {/* Main chart component displaying log returns over time */}
      <Line data={chartData} options={options} />
      
      {/* Conditional rendering of change point analysis results */}
      {changePoint.change_point_date && (
        <div style={{ marginTop: '20px' }}>
          <h2>Change Point Analysis</h2>
          <p><strong>Date:</strong> {changePoint.change_point_date}</p>
          <p><strong>Event:</strong> {changePoint.associated_event}</p>
          <p><strong>Log Return Change:</strong> {changePoint.log_return_change}</p>
          <p><strong>Event Date:</strong> {changePoint.event_date}</p>
          <p><strong>Description:</strong> {changePoint.event_description}</p>
        </div>
      )}
    </div>
  );
}

export default App;