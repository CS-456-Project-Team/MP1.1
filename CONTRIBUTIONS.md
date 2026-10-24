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


Stop the attacker using `Ctrl+C` to verify that the monitor detects the missing heartbeats.

**Note:** Run each Python script in a separate terminal. For Attack 2, the attacker must capture and release UDP port 5001 before starting the monitor.
