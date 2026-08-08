# Jeeva Raksha – Emergency Assistance Application

Jeeva Raksha is a Python-based desktop application developed using Tkinter. It provides a simple graphical interface for accessing emergency-assistance features such as SOS alerts, women safety mode, emergency location sharing, voice assistance, and medicine reminders.

## Features

- SOS emergency alert interface
- Women Safety Mode
- Accident Alert simulation
- Health Emergency alert simulation
- Emergency audio recording simulation
- Emergency photo capture simulation
- Demo live-location sharing
- Medicine reminder with time-based alerts
- Voice assistance using `pyttsx3`
- User-friendly Tkinter GUI
- Emergency contact section

## Technologies Used

- Python
- Tkinter
- pyttsx3
- Threading
- DateTime

## Project Structure

```text
Jeeva-Raksha-Emergency-App/
├── jeeva_raksha.py
└── README.md
```

## Installation

1. Install Python 3.
2. Install the required external package:

```bash
pip install pyttsx3
```

`tkinter`, `threading`, `time`, and `datetime` are used by the application; Tkinter is included with many standard Python installations.

## Run the Application

```bash
python jeeva_raksha.py
```

## Important Note

This project is a student software prototype. Some functions, including accident detection, health monitoring, audio recording, photo capture, and live-location sharing, are implemented as simulations/demo interfaces in the current version rather than as connected real-world services or sensors.

Emergency contact information and location values in this public repository have been replaced with placeholders for privacy.

## Future Improvements

- Integrate real GPS/location services
- Add actual emergency SMS/calling functionality
- Connect real audio recording and camera modules
- Integrate health sensors for real-time monitoring
- Store and manage emergency contacts securely
- Improve validation and error handling

## Author

**Shivani Ponaganti**

Electronics & Communication Engineering Student
