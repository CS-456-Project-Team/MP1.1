# MP1.1

Using Python version 3.14

Criteria:
Task 1: Team
    Benjamin Mooneyham: "Moonshammy"
    Victor Troncoso: "troncosv"
    Matthew Leman: ""
    Tyler Short: ""

Task 2: Security Domain
    Network Sentinel/Firewall Agent

Task 3: Implement the Critical Process with Simulated Failure
    Must have a running process must completely close out due to a critical failure. Failure cannot be scheduled,
    should have it on some sort of error (it could divide by zero and break).

Task 4: Implement the Heartbeat Monitor
    Option A (Push/Periodic Heartbeat): The critical service sends a "HEARTBEAT" datagram to the
    monitor every 𝑇 milliseconds.
    Option B (Pull/Ping-Ack): The monitor pings the service every 𝑇 milliseconds, requiring a timely
    response.
    
Task 5: Adversarial Assessment
    Attack 1 – Heartbeat Spoofing: Can an external script transmit fake heartbeat messages to the
    monitor so that the monitor reports the service is healthy even after the critical process has
    crashed?
    Attack 2 – Replay Attack/Tampering: If the heartbeat payload includes status data or a timestamp,
    can an attacker capture a valid packet and replay it indefinitely to mask downtime?
