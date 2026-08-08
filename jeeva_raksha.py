import tkinter as tk
from tkinter import messagebox
import pyttsx3
import threading
import time
from datetime import datetime
# VOICE ENGINE
engine = pyttsx3.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()

# MAIN WINDOW

root = tk.Tk()
root.title("JeevaRaksha Safety App")
root.geometry("900x700")
root.config(bg="#101820")
heading = tk.Label(
    root,
    text="JeevaRaksha - Personal Safety & Health Companion",
    font=("Arial", 20, "bold"),
    bg="#101820",
    fg="white"
)
heading.pack(pady=20)
main_frame = tk.Frame(root, bg="#101820")
main_frame.pack(pady=10)

# EMERGENCY CONTACTS

contacts = [
    "Mother : XXXXXXXX",
    "Father : XXXXXXXX",
    "Brother : XXXXXXXX"
]

# SOS FUNCTION

def send_sos():
    location = "Demo Location (replace with your own location service)"

    emergency_message = (
        "EMERGENCY ALERT!\n\n"
        f"Live Location: {location}\n"
        "Emergency contacts notified successfully."
    )

    messagebox.showwarning("SOS ALERT", emergency_message)

    speak("Emergency detected. Live location sent successfully")

# WOMEN SAFETY MODE

def women_safety_mode():
    messagebox.showinfo(
        "Women Safety Mode",
        "Women safety mode activated.\n"
        "Audio recording started.\n"
        "Live location shared."
    )

    speak("Women safety mode activated")


# ACCIDENT DETECTION

def accident_detected():
    messagebox.showerror(
        "Accident Alert",
        "Possible accident detected!\n"
        "Emergency contacts informed."
    )

    speak("Accident detected. Emergency contacts informed")


# -----------------------------
# HEART EMERGENCY
# -----------------------------
def heart_emergency():
    messagebox.showwarning(
        "Health Emergency",
        "Abnormal heartbeat detected!\n"
        "Medical emergency alert sent."
    )

    speak("Health emergency detected")


# -----------------------------
# AUDIO RECORDING SIMULATION
# -----------------------------
def record_audio():
    messagebox.showinfo(
        "Audio Recording",
        "Emergency audio recording started successfully."
    )

    speak("Audio recording started")


# -----------------------------
# PHOTO CAPTURE SIMULATION
# -----------------------------
def capture_photo():
    messagebox.showinfo(
        "Photo Capture",
        "Surrounding photo captured successfully."
    )

    speak("Photo captured successfully")


# -----------------------------
# LIVE LOCATION
# -----------------------------
def share_location():
    location = "Demo Location (replace with your own location service)"

    messagebox.showinfo(
        "Live Location",
        f"Live location shared successfully!\n\n{location}"
    )

    speak("Live location shared")


# -----------------------------
# MEDICINE REMINDER SYSTEM
# -----------------------------
def medicine_alarm(medicine_name, alarm_time):
    while True:
        current_time = datetime.now().strftime("%H:%M")

        if current_time == alarm_time:
            messagebox.showinfo(
                "Medicine Reminder",
                f"Time to take your medicine:\n{medicine_name}"
            )

            speak(f"Please take your medicine {medicine_name}")
            time.sleep(60)

        time.sleep(1)


# -----------------------------
# SET REMINDER
# -----------------------------
def set_reminder():
    medicine = medicine_entry.get()
    reminder_time = time_entry.get()

    if medicine == "" or reminder_time == "":
        messagebox.showerror("Error", "Please fill all fields")
        return

    thread = threading.Thread(
        target=medicine_alarm,
        args=(medicine, reminder_time),
        daemon=True
    )

    thread.start()

    messagebox.showinfo(
        "Reminder Set",
        f"Medicine reminder set for {reminder_time}"
    )


# -----------------------------
# BUTTONS SECTION
# -----------------------------
button_frame = tk.Frame(main_frame, bg="#101820")
button_frame.grid(row=0, column=0, padx=20)


btn_style = {
    "font": ("Arial", 12, "bold"),
    "width": 25,
    "height": 2,
    "bd": 0
}


sos_btn = tk.Button(
    button_frame,
    text="SOS EMERGENCY",
    bg="red",
    fg="white",
    command=send_sos,
    **btn_style
)
sos_btn.pack(pady=10)


women_btn = tk.Button(
    button_frame,
    text="Women Safety Mode",
    bg="#ff1493",
    fg="white",
    command=women_safety_mode,
    **btn_style
)
women_btn.pack(pady=10)


accident_btn = tk.Button(
    button_frame,
    text="Accident Detection",
    bg="#ff6600",
    fg="white",
    command=accident_detected,
    **btn_style
)
accident_btn.pack(pady=10)


heart_btn = tk.Button(
    button_frame,
    text="Health Emergency",
    bg="#990000",
    fg="white",
    command=heart_emergency,
    **btn_style
)
heart_btn.pack(pady=10)


location_btn = tk.Button(
    button_frame,
    text="Share Live Location",
    bg="#0066cc",
    fg="white",
    command=share_location,
    **btn_style
)
location_btn.pack(pady=10)


record_btn = tk.Button(
    button_frame,
    text="Record Emergency Audio",
    bg="#663399",
    fg="white",
    command=record_audio,
    **btn_style
)
record_btn.pack(pady=10)


photo_btn = tk.Button(
    button_frame,
    text="Capture Emergency Photo",
    bg="#009966",
    fg="white",
    command=capture_photo,
    **btn_style
)
photo_btn.pack(pady=10)


# -----------------------------
# MEDICINE REMINDER SECTION
# -----------------------------
medicine_frame = tk.Frame(main_frame, bg="#1c1c1c", padx=20, pady=20)
medicine_frame.grid(row=0, column=1, padx=20)


medicine_title = tk.Label(
    medicine_frame,
    text="Medicine Reminder System",
    font=("Arial", 16, "bold"),
    bg="#1c1c1c",
    fg="white"
)
medicine_title.pack(pady=10)


medicine_label = tk.Label(
    medicine_frame,
    text="Medicine Name",
    font=("Arial", 12),
    bg="#1c1c1c",
    fg="white"
)
medicine_label.pack()

medicine_entry = tk.Entry(medicine_frame, width=30)
medicine_entry.pack(pady=5)


# TIME
ntime_label = tk.Label(
    medicine_frame,
    text="Reminder Time (24hr format HH:MM)",
    font=("Arial", 12),
    bg="#1c1c1c",
    fg="white"
)
ntime_label.pack()


time_entry = tk.Entry(medicine_frame, width=30)
time_entry.pack(pady=5)


# REMINDER BUTTON
reminder_btn = tk.Button(
    medicine_frame,
    text="Set Reminder",
    bg="#00aa00",
    fg="white",
    font=("Arial", 12, "bold"),
    width=20,
    command=set_reminder
)
reminder_btn.pack(pady=20)


# -----------------------------
# CONTACTS SECTION
# -----------------------------
contact_title = tk.Label(
    medicine_frame,
    text="Emergency Contacts",
    font=("Arial", 15, "bold"),
    bg="#1c1c1c",
    fg="white"
)
contact_title.pack(pady=10)


for contact in contacts:
    lbl = tk.Label(
        medicine_frame,
        text=contact,
        font=("Arial", 11),
        bg="#1c1c1c",
        fg="#00ffcc"
    )
    lbl.pack()

footer = tk.Label(
    root,
    text="Built using Python + Tkinter",
    font=("Arial", 11),
    bg="#101820",
    fg="gray"
)
footer.pack(side="bottom", pady=10)

root.mainloop()
