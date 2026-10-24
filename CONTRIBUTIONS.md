## CS456 - Mini Group Project 1: Resilient Security Systems
## Contributions:
**Victor Troncoso**: Implementation of the Critical Process with Simulated Failure. 
* sentinel.py - Simulated firewall, periodic heartbeat sender, and random crash simulation.

**Benjamin Mooneyham**:

**Matthew Leman**:

**Tyler Short**:


Task 1: Team
    Benjamin Mooneyham: "Moonshammy"
    Victor Troncoso: "troncosv"
    Matthew Leman: "Philojyw"
    Tyler Short: "Tsyber"

Task 2: Security Domain
    We chose Network Sentinel/Firewall Agent for this assignment

Task 3: Implement the Critical Process with Simulated Failure
    Need to create a process that has a built-in fault, and not just a scheduled crash. Like divide by zero

Task 4: Implement the Heartbeat Monitor
    Separate process that checks on the Critical Process and ensures that is alive. 
    Option A (Push/Periodic Heartbeat): The critical service sends a "HEARTBEAT" datagram to the
    monitor every 𝑇 milliseconds.
    Option B (Pull/Ping-Ack): The monitor pings the service every 𝑇 milliseconds, requiring a timely
    response.

Task 5: Adversarial Assessment
    Create an Adversarial program that replaces the Critical Process responses to spoof the Heartbeat monitor
    Attack 1 – Heartbeat Spoofing: Can an external script transmit fake heartbeat messages to the
    monitor so that the monitor reports the service is healthy even after the critical process has
    crashed?
    Attack 2 – Replay Attack/Tampering: If the heartbeat payload includes status data or a timestamp,
    can an attacker capture a valid packet and replay it indefinitely to mask downtime?

## Running the Project

The project just requires Python 3. No additional libraries are needed.

### 1. Normal Operation and Failure Detection

Open two separate terminals:

**Terminal 1 - Start the Monitor**
```powershell
python .\monitor.py
```

**Terminal 2 - Start the Sentinel**
```powershell
python .\sentinel.py
```

The Sentinel sends heartbeats every second and randomly crashes after 20 - 40 seconds. The monitor detects the failure after approximately 3 seconds without a heartbeat.

### 2. Attack 1 - Heartbeat Spoofing

Start the Monitor and Sentinel as described above.

**Terminal 3 - Start the Attacker**
```powershell
python .\attacker.py spoof
```

The attacker sends fake heartbeats to prevent the monitor from detecting the Sentinel's crash.

Stop the attacker using `Ctrl+C`. The monitor should then detect the failure.

### 3. Attack 2 - Heartbeat Replay

For this test, start the programs in the following order:

**Terminal 1 - Start Replay Capture**
```powershell
python .\attacker.py replay
```

**Terminal 2 - Start the Sentinel**
```powershell
python .\sentinel.py
```

Wait until the attacker captures a legitimate heartbeat.

**Terminal 3 - Start the Monitor**
```powershell
python .\monitor.py
```

Return to Terminal 1 and press `Enter` to begin replaying the captured heartbeat.

The monitor should continue accepting the replayed messages even after the Sentinel crashes.

Stop the attacker using `Ctrl+C` to verify that the monitor detects the missing heartbeats.

**Note:** Run each Python script in a separate terminal. For Attack 2, the attacker must capture and release UDP port 5001 before starting the monitor.
