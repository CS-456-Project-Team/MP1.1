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
