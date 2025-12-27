import datetime
import pytz
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder

def get_world_time():
    print("--- Professional GPS-Based World Clock ---")
    
    # 1. Initialize the tools
    # 'user_agent' is required by the geocoding service to identify your app
    geolocator = Nominatim(user_agent="world_clock_app")
    tf = TimezoneFinder()

    place_name = input("Enter the place (e.g., Lu'an, Beijing, Paris): ").strip()

    try:
        # 2. Convert city name to Latitude/Longitude (Geocoding)
        location = geolocator.geocode(place_name)
        
        if not location:
            print(f"Error: Could not find '{place_name}'. Check the spelling.")
            return

        # 3. Find the timezone name using coordinates
        timezone_str = tf.timezone_at(lng=location.longitude, lat=location.latitude)

        if not timezone_str:
            print(f"Error: Could not determine timezone for {place_name}.")
            return

        # 4. Get the current time for that timezone
        timezone = pytz.timezone(timezone_str)
        now = datetime.datetime.now(timezone)

        # Formatting
        date_str = now.strftime("%A, %B %d, %Y")
        time_str = now.strftime("%H:%M:%S")
        tz_format = now.strftime("%Z (UTC %z)")

        print("-" * 40)
        print(f"Input Name:    {place_name}")
        print(f"Full Address:  {location.address}")
        print(f"Timezone:      {timezone_str}")
        print(f"Current Date:  {date_str}")
        print(f"Current Time:  {time_str}")
        print(f"Time Format:   {tz_format}")
        print("-" * 40)

    except Exception as e:
        print(f"A connection error occurred. Please check your internet.")

if __name__ == "__main__":
    get_world_time()