## CS456 - Mini Group Project 1: Resilient Security Systems

### Security Domain: 
Network Sentinel/Firewall Agent

### Contributions:

**Victor Troncoso "troncosv"**: Implementation of the Critical Process with Simulated Failure and adversary attack 2. 
* sentinel.py - Simulated firewall, periodic heartbeat sender, and random crash simulation.
* adversary.py - External script that captures a legitimate heartbeat from the Sentinel and repeatedly replays it to trick the monitor into believing the Sentinel is still running, even after it crashes.
* Created and added content to README.md 
  
**Benjamin Mooneyham "Moonshammy"**:
* monitor.py - Opened a channel to receive input from Sentinel. Acknowledged when a message received, made a log when a message was not received in a delayed from normal Sentinel heartbeats.
  
**Matthew Leman "Philojyw"**:
* Created video demo
* monitor.py - updated logging logic, changed timeout and loss of service logic so the two aren't synonymous.
* Proof read and updated README.md
  
**Tyler Short "Tsyber"**: Implementation of adversary, attack 1.
* adversary.py - Outside system, configurable, sends either a fake 'heartbeat' or a captured one to mimic heartbeat of victim

