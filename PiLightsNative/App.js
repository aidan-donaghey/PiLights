import { StatusBar } from "expo-status-bar";
import { StyleSheet, View, SafeAreaView, Platform } from "react-native";
import * as eva from "@eva-design/eva";
import {
  ApplicationProvider,
  Layout,
  Text,
  Card,
  List,
} from "@ui-kitten/components";
import { default as theme } from "./app/theme/green.json";
import { publishMQTT } from "./app/utilities/MQTT";
import { ListItemSingle, ListItems } from "./app/components/SimpleListItem";
import { HomeScreen } from "./app/screens/HomeScreen";
// connect the client

export default function App() {
  const handlePress = () => publishMQTT("/rasplights/red", "10");
  return (
    <ApplicationProvider {...eva} theme={{ ...eva.dark, ...theme }}>
      <HomeScreen />
    </ApplicationProvider>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "dodgerblue",
    alignItems: "center",
    justifyContent: "center",
  },
});
