import logging
import socket
import threading
from datetime import datetime

HOST = '127.0.0.1'
PORT = 5001

def receive_heartbeat():
    monitor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    monitor.settimeout(3) #extended wait time for network latency
    
    monitor.bind((HOST, PORT))
    
    try:
        print("Heartbeat online")
        
        while True:
            try:
                message = monitor.recv(1024)
                
                if not message:
                    logging.info(f"Received heartbeat on {datetime.now()}")
                    break
                
                logging.info(f"Received heartbeat: {message}")
                
            except socket.timeout:
                logging.error(f"Heartbeat not received at {datetime.now()}")
    
    except socket.error as e:
        print("Server unexpectedly closed")
        
    except KeyboardInterrupt:
        print("Server stopped by user")
    
    finally:
        monitor.close()
        
        
if __name__ == "__main__":
    monitor_t = threading.Thread(target=receive_heartbeat)
    monitor_t.start()
    
