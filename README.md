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
            <pre><code>git clone https://github.com/yourusername/GoblinLogger.git
cd GoblinLogger</code></pre>
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

