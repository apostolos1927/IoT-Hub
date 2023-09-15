from azure.iot.device import IoTHubDeviceClient, Message
import time
import json
import random

connection = "...."


def main():
    try:
        client = IoTHubDeviceClient.create_from_connection_string(connection)
        while True:
            data = {
                "DeviceID": random.randint(1, 100),
                "DeviceNumber": random.randint(1, 100),
            }
            message = Message(json.dumps(data))
            client.send_message(message)
            print(f"Message {message} was sent successfully")
            time.sleep(2)
    except KeyboardInterrupt:
        print("program was interruped")


if __name__ == "__main__":
    main()
