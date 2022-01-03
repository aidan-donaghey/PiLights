import { Layout, Text } from "@ui-kitten/components";
import { ListItems } from "../components/SimpleListItem";

export const HomeScreen = () => (
  <Layout style={{ flex: 1, justifyContent: "center", alignItems: "center" }}>
    <Text category="h1">HOME LIGHT CONTROLS</Text>
    <ListItems colors={["Red", "Blue", "Green"]}></ListItems>
  </Layout>
);
