# 🌍 Professional World Clock

A high-precision Python tool that retrieves the current date, time, and timezone format for any city in the world using GPS coordinates and geocoding.

## 📝 Description
This program allows users to input any city name (e.g., Beijing, Lu'an, Paris) and automatically determines its geographic coordinates. It then maps those coordinates to the official timezone database to provide the most accurate local time, accounting for Daylight Savings Time (DST).

## ✨ Features
* **Global Search:** Find any city, village, or landmark.
* **GPS Precision:** Uses `geopy` to find exact latitude and longitude.
* **Detailed Time Info:** Displays Day, Month, Year, 24-hour time, and UTC offset.
* **Error Handling:** Professional-grade handling for typos or unknown locations.

## 🚀 Benefits
* **Accuracy:** Unlike simple city-lists, this uses the most up-to-date Olson timezone database.
* **User Friendly:** No need to type complex formats like `Asia/Shanghai`; just type the city name.
* **Portable:** Works on any Linux/Unix system with Python 3.

---

## 🛠️ Installation & Setup

### 1. Update Packages & Install Dependencies
First, ensure your Linux system is up to date and has the necessary tools:

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install python3 python3-pip git python3-venv -y

2. Clone the Repository

Clone your project from GitHub (replace with your actual URL) and enter the directory:
Bash

git clone [https://github.com/hiddendestroyer/world-clock.git](https://github.com/hiddendestroyer/world-clock.git)
cd world-clock

3. Setup Virtual Environment (Best Practice)

In Linux administration, we use virtual environments to keep our system clean:
Bash

# Create the environment
python3 -m venv venv

# Activate the environment
source venv/bin/activate

4. Install Requirements

Install the required libraries listed in the requirements.txt:
Bash

pip install -r requirements.txt

💻 Usage

Run the program using the Python interpreter:
Bash

python3 world-clock.py

Example Input/Output:
Plaintext

Enter the place: Lu'an
----------------------------------------
Input Name:    Lu'an
Full Address:  Lu'an, Anhui, China
Timezone:      Asia/Shanghai
Current Date:  Sunday, December 28, 2025
Current Time:  04:05:12
Time Format:   CST (UTC +0800)
----------------------------------------

Exit the virtual environment: after executing the program, exit the virtual environment:
Bash

deactivate

📄 License

This project is licensed under the MIT License - see the LICENSE file for details.
👤 Author

hiddendestroyer

    Professional Python Programmer & Linux Admin (In-Training)