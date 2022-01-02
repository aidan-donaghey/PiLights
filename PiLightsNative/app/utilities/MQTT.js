import { Client, Message } from "react-native-paho-mqtt";
//Set up an in-memory alternative to global localStorage
const myStorage = {
  setItem: (key, item) => {
    myStorage[key] = item;
  },
  getItem: (key) => myStorage[key],
  removeItem: (key) => {
    delete myStorage[key];
  },
};

function publishMQTT(topic, payload) {
  const client = new Client({
    uri: "ws://localhost:9001/",
    clientId: "clientId",
    storage: myStorage,
  });

  // set event handlers
  client.on("connectionLost", (responseObject) => {
    if (responseObject.errorCode !== 0) {
      console.log(responseObject.errorMessage);
    }
  });
  client.on("messageReceived", (message) => {
    console.log(message.payloadString);
  });
  client
    .connect()
    .then(() => {
      const message = new Message(payload);
      message.destinationName = topic;
      client.send(message);
    })
    .catch((responseObject) => {
      if (responseObject.errorCode !== 0) {
        console.log("onConnectionLost:" + responseObject.errorMessage);
      }
    });
}

export { publishMQTT };
