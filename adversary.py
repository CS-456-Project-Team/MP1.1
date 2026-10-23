import socket
import threading
import time

# Attack 1
# Function to send a heartbeat message over UDP
def send_heartbeat():
    # Creates a UDP socket for sending the heartbeat message
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as heartbeat_socket:
        while True:
            # Sends a heartbeat message to the specified IP address and port
            # to indicate that the sender is alive
            heartbeat_socket.sendto(b"HEARTBEAT", ("127.0.0.1", 5001))

            #print("Heartbeat sent")

            time.sleep(1)  # Wait for 1 seconds before sending the next heartbeat

# Attack 2


if __name__ == "__main__":
    send_heartbeat()

    