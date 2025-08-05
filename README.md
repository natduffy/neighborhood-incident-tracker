# Seattle Fire Incident Tracker

A real-time web application that tracks and displays fire incidents within one mile of specified coordinates in Seattle, Washington.

## 🚒 Features

- **Real-time Data**: Fetches live fire incident data from Seattle's Open Data API
- **Distance Filtering**: Shows only incidents within one mile of your location
- **Interactive Map**: Visual display using Leaflet.js with clickable markers
- **Auto-refresh**: Automatically loads latest data when page opens
- **Manual Refresh**: Button to fetch updated data anytime
- **Responsive Design**: Works on desktop and mobile devices

## 📁 Project Structure

```
seattle-fire/
├── data.txt                    # Configuration file with coordinates and API URL
├── filter_incidents.py         # Python script to fetch and filter incidents
├── map_viewer.html            # Static HTML viewer with embedded data
├── map_viewer_dynamic.html    # Dynamic HTML viewer with live API integration
├── filtered_incidents.json    # Sample filtered incident data
├── requirements.txt           # Python dependencies
├── seattle.gov.txt           # Additional Seattle data reference
└── README.md                 # This file
```

## 🚀 Quick Start

### Option 1: Dynamic Viewer (Recommended)
1. Open `map_viewer_dynamic.html` in your web browser
2. Data loads automatically from Seattle's API
3. Use the "Refresh Data" button to get latest incidents

### Option 2: Static Viewer
1. Run the Python script to fetch data:
   ```bash
   python3 filter_incidents.py
   ```
2. Open `map_viewer.html` in your web browser
3. View the filtered incidents

### Option 3: Command Line
1. Install dependencies:
   ```bash
   pip3 install requests
   ```
2. Run the filtering script:
   ```bash
   python3 filter_incidents.py
   ```
3. View results in terminal and `filtered_incidents.json`

## 🔧 Configuration

Edit `data.txt` to change your location:
```
API Access: https://data.seattle.gov/resource/kzjm-xkqj.json
My latitude: 47.578393
My longitude: -122.398786
```

## 📊 Data Sources

- **API Endpoint**: Seattle Fire Department 911 Incident Response
- **Data Format**: JSON with latitude, longitude, incident type, address, and timestamp
- **Update Frequency**: Real-time as incidents are reported
- **Coverage**: All of Seattle, Washington

## 🗺️ Map Features

- **Your Location**: Blue marker showing your coordinates
- **1-Mile Radius**: Red dashed circle showing search area
- **Incident Markers**: Red dots for each fire incident
- **Interactive Popups**: Click markers for detailed incident information
- **Clickable Cards**: Click sidebar cards to zoom to incident location

## 🎯 Incident Types Tracked

- Automatic Fire Alarms
- Motor Vehicle Incidents (MVI)
- Rescue Operations
- Medical Responses
- Brush Fires
- And more...

## 🔄 Refresh Options

### Dynamic Viewer
- **Auto-load**: Data loads automatically when page opens
- **Manual Refresh**: Click "🔄 Refresh Data" button
- **Keyboard Shortcut**: Ctrl+R (Windows/Linux) or Cmd+R (Mac)

### Static Viewer
- **Manual Update**: Run `python3 filter_incidents.py` to refresh data
- **File-based**: Updates `filtered_incidents.json` with new data

## 🛠️ Technical Details

### Distance Calculation
Uses the Haversine formula to calculate accurate distances between geographic coordinates:
- Earth radius: 3,956 miles
- Precision: 3 decimal places
- Filter: Incidents within 1.0 mile radius

### API Integration
- **Endpoint**: `https://data.seattle.gov/resource/kzjm-xkqj.json`
- **Method**: GET request
- **Format**: JSON response
- **Rate Limiting**: None specified by Seattle Open Data

### Browser Compatibility
- Modern browsers with ES6+ support
- Leaflet.js for map functionality
- No server required - runs entirely in browser

## 📱 Mobile Support

The application is fully responsive and works on:
- Desktop browsers (Chrome, Firefox, Safari, Edge)
- Mobile browsers (iOS Safari, Chrome Mobile)
- Tablet browsers

## 🔍 Troubleshooting

### Common Issues

1. **No incidents showing**: Check your coordinates in `data.txt`
2. **API errors**: Verify internet connection and API availability
3. **Map not loading**: Ensure JavaScript is enabled
4. **Distance calculations**: Verify latitude/longitude format

### Error Messages

- **"Error loading incidents data"**: API connection issue
- **"No incidents found within one mile"**: No recent incidents in your area
- **"Failed to fetch data"**: Network or API server issue

## 📈 Future Enhancements

- [ ] Time-based filtering (last 24 hours, week, month)
- [ ] Incident type filtering
- [ ] Multiple location support
- [ ] Historical data analysis
- [ ] Email/SMS alerts for nearby incidents
- [ ] Mobile app version

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- Seattle Open Data for providing the fire incident API
- Leaflet.js for the interactive mapping functionality
- OpenStreetMap for map tiles and data

---

**Note**: This application is for informational purposes only. For emergency situations, always call 911. 