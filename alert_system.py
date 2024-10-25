import time
from config import THRESHOLD, ALERT_THRESHOLD_CONSECUTIVE
from database import get_latest_weather_data

# Function to check alert conditions based on the temperature threshold
def check_alert_conditions(city, threshold=THRESHOLD, consecutive_count=ALERT_THRESHOLD_CONSECUTIVE):
    alert_counter = 0

    # Continuously check for updates
    while True:
        latest_weather_data = get_latest_weather_data(city)

        # Check if the temperature exceeds the threshold
        if latest_weather_data['temperature'] > threshold:
            alert_counter += 1
            if alert_counter >= consecutive_count:
                # Trigger alert when threshold is breached consecutively
                trigger_alert(city, latest_weather_data)
                alert_counter = 0  # Reset after alert
        else:
            alert_counter = 0  # Reset the counter if the condition is not met

        # Wait before checking again (simulating real-time updates)
        time.sleep(300)  # Adjust the interval as necessary (in seconds)

# Function to trigger an alert (can be console, email, etc.)
def trigger_alert(city, weather_data):
    alert_message = f"ALERT: High temperature in {city}! \n" \
                    f"Temperature: {weather_data['temperature']}°C\n" \
                    f"Weather Condition: {weather_data['weather_condition']}\n" \
                    f"Timestamp: {weather_data['timestamp']}"
    # For simplicity, print the alert to the console. This can be extended to send email or notifications.
    print(alert_message)
    # You can add code here to send the alert via email or any other preferred method.

if __name__ == "__main__":
    # Example usage: Check alert conditions for a specific city
    check_alert_conditions(city="Delhi")
