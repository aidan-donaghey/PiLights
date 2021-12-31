import paho.mqtt.client as paho
import time
import lightsAPI
# Broker and User information
broker="192.168.1.127"
# This is the topic that we are subscribing to
#  It should be subbed to all topics inside of rasplights with the #
topic = "/rasplights/#"
lights = lightsAPI.lights()

def connect_mqtt() -> paho:
    """This connects to the Broker

    Returns:
        paho: This is the cleint Object
    """
    def on_connect(client, userdata, flags, rc):
        """Callback function for connection to the broker

        Args:
            client (paho): Client Object
            userdata (dict): Optional
            flags ([type]): [description]
            rc ([type]): [description]

        Returns:
            [paho]: Returns the client after it has been connected or not.
        """
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)
    client = paho.Client("client-001")
    # Binds the on_connect function above to the client.
    client.on_connect = on_connect
    # Actually connects and calls on_connect
    client.connect(broker)
    return client


def subscribe(client: paho):
    def on_message(client, userdata, msg):
        if msg.topic in lights.actions:
            print("It is in actions")
            lights.actions[msg.topic](msg)
        else:
            print("Not a Valid command")
    client.subscribe(topic)
    client.on_message = on_message


def run():
    """Main Running Loop
    """
    client = connect_mqtt()
    client.loop_start()
    while True:
        subscribe(client)
        


if __name__ == '__main__':
    run()