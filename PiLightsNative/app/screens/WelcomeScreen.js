import React from "react";
import { ImageBackground } from "react-native-web";

function WelcomeScreen(props) {
  return (
    <ImageBackground
      source={require("../assets/background.jpg")}
    ></ImageBackground>
  );
}

export default WelcomeScreen;
