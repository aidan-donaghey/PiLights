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
import { default as theme } from "./app/theme/green.json"; // <-- Import app theme
import { publishMQTT } from "./app/utilities/MQTT";
import { ListCustomItemShowcase } from "./app/components/ListCustomItems";
import { ListItemSingle, ListItems } from "./app/components/SimpleListItem";
// connect the client
const HomeScreen = () => (
  <Layout style={{ flex: 1, justifyContent: "center", alignItems: "center" }}>
    <Text category="h1">HOME LIGHT CONTROLS</Text>
    {/* <ListItemSingle color="White"></ListItemSingle> */}
    <ListItems colors={["Red", "Blue", "Green"]}></ListItems>
  </Layout>
);

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
