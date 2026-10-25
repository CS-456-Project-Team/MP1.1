## CS456 - Mini Group Project 1: Resilient Security Systems

### Security Domain: 
Network Sentinel/Firewall Agent

### Contributions:

**Victor Troncoso "troncosv"**: Implementation of the Critical Process with Simulated Failure and adversary attack 2. 
* sentinel.py - Simulated firewall, periodic heartbeat sender, and random crash simulation.
* adversary.py - External script that captures a legitimate heartbeat from the Sentinel and repeatedly replays it to trick the monitor into believing the Sentinel is still running, even after it crashes.
  
**Benjamin Mooneyham "Moonshammy"**:

**Matthew Leman "Philojyw"**:

**Tyler Short "Tsyber"**: Implementation of adversary, attack 1.
* adversary.py - Outside system, configurable, sends either a fake 'heartbeat' or a captured one to mimic heartbeat of victim

