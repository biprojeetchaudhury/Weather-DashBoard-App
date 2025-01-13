# Weather-DashBoard-App

## **Project Overview**

The Weather Search App allows users to search for the current weather conditions of any city worldwide. The app displays information such as temperature, weather conditions, humidity, and wind speed. The application also stores a history of searched cities using browser-side storage, making it easy for users to revisit previous searches.

---

## **Setup Instructions**

### **Prerequisites**
- Python 3.11 or higher
- Flask framework
- Internet connection for API requests

### **1. Clone the Repository**
```bash
git clone <repository_url>
cd weather-search-app
```

### **2. Install Dependencies**
Install required Python packages:
```bash
pip install -r requirements.txt
```

### **3. Set Up Environment Variables**
Create a `.env` file in the project root and add your OpenWeatherMap API key:
```plaintext
API_KEY=your_openweather_api_key_here
```

### **4. Run the Application**
Start the Flask server by executing:
```bash
python app.py
```

The app will be available at `http://localhost:5000`.

---

## **API Documentation**

### **Endpoint: Get Weather Data**
- **URL:** `/api/weather`
- **Method:** `GET`
- **Query Parameters:**
  - `city`: Name of the city (required)

#### **Example Request**
```http
GET /api/weather?city=London
```

#### **Response**
```json
{
  "city": "London",
  "temperature": 18.5,
  "condition": "clear sky",
  "humidity": 55,
  "wind_speed": 3.5
}
```

#### **Error Responses**
- **404:** City not found
- **500:** Internal server error

---

## **Design Decisions**

- **Frontend:** Simple single-page design with a responsive layout.
- **Backend:** Flask was chosen for its simplicity and lightweight nature.
- **Weather API:** OpenWeatherMap API was selected due to its comprehensive data and free tier availability.
- **Data Storage:** Browser-side `localStorage` was used to maintain the search history without requiring server-side storage.

---

## **Future Improvements**

1. **Enhanced Error Handling:** Provide more descriptive error messages for different API issues.
2. **Autocomplete Suggestions:** Implement city name suggestions as the user types.
3. **User Preferences:** Allow users to save temperature units (Celsius/Fahrenheit) and theme preferences.
4. **Mobile Optimization:** Improve the UI for better mobile device usability.
5. **Localization:** Support multiple languages for a broader audience.
6. **Weather Forecast:** Add a 7-day weather forecast feature.

---

## **Notes About Platform Limitations**

- **API Rate Limits:** The OpenWeatherMap free tier has request limits that may impact frequent searches.
- **Browser Storage:** `localStorage` has size limitations and may not scale for larger datasets.
- **Deployment Restrictions:** Free platforms like Replit may impose resource or storage constraints.

---

## **Conclusion**
The Weather Search App is a lightweight, functional application providing a user-friendly way to check current weather conditions and maintain a history of searches. With planned improvements, the app aims to deliver even more value and convenience for its users.

