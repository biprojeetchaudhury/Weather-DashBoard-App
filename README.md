# Weather App API

## **Project Overview**
The Weather App API is a Flask-based web application that provides weather data for a given city. It fetches real-time weather information using the OpenWeather API and exposes an API endpoint that can be integrated with various frontends. The app is designed to be easily deployed on platforms like Render, ensuring scalability and ease of use.

### **Features:**
- Fetch current weather details (temperature, condition, humidity, wind speed).
- Lightweight and modular architecture.
- CORS-enabled to allow access from any frontend.

---

## **Setup Instructions**

### **Prerequisites:**
- Python 3.9+
- OpenWeather API Key (Sign up at https://openweathermap.org/ to get your API key).

### **Steps to Run Locally:**

1. **Clone the repository:**
   ```bash
   git clone https://github.com/biprojeetchaudhury/Weather-DashBoard-App.git
   cd Weather-DashBoard-app
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Create a `.env` file in the root directory:**
   ```plaintext
   WEATHER_API_KEY=openweather_api_key
   ```

4. **Run the application:**
   ```bash
   python3 app.py
   ```
   The app will start at `http://127.0.0.1:5000/`.

### **Deploy on Render:**
1. Push the repository to a GitHub/GitLab repository.
2. Log in to your [Render](https://render.com/) account and create a new Web Service.
3. Configure the service:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app --bind 0.0.0.0:$PORT`
4. Add the `WEATHER_API_KEY` as an environment variable in Render.
5. Deploy and access your application via the generated URL(`https://biprojeetchaudhury.github.io/Weather-DashBoard-App/`).
6. Wake-Up Time expectations - about 30 seconds

---

## **Design Decisions**
1. Frontend - HTML,CSS,Javascript
2. Backend - Flask

---

## **Future Improvements**

- Provide a 7-day weather forecast using additional OpenWeather API endpoints.
- Clear previous search history
- Shortcut to search previously searched city by clicking it

---

## **Notes About Platform Limitations**
1. **Cold Starts:**
   - On serverless platforms like Render, there might be a slight delay during the first request after a period of inactivity.

2. **Rate Limiting:**
   - OpenWeather API has rate limits based on your subscription tier. Ensure the application handles rate-limit errors gracefully.

3. **Static IP Restrictions:**
   - Some OpenWeather accounts may require whitelisting IPs. Ensure Render's dynamic IPs are compatible with your setup.

---

With these guidelines, you can easily set up, deploy, and extend the Weather App API for various use cases.

### **User Interface**
![Weather App - Google Chrome 16-01-2025 09_08_00 PM](https://github.com/user-attachments/assets/192d485a-d382-4378-92c0-b5c5eb6ac302)
![Weather App - Google Chrome 16-01-2025 09_09_34 PM](https://github.com/user-attachments/assets/faa145a9-1878-4a8f-9040-2095d447c9df)
![Weather App - Google Chrome 16-01-2025 09_09_50 PM](https://github.com/user-attachments/assets/c47c7d99-2a73-4a68-b84e-1c6f5ba1c5af)


