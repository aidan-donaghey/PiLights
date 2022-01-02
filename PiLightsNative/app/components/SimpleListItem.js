import { StyleSheet, View, SafeAreaView, Platform } from "react-native";
import { Avatar, Button, ListItem, Toggle } from "@ui-kitten/components";
import React from "react";

const ToggleButton = () => {
  const [checked, setChecked] = React.useState(false);

  const onCheckedChange = (isChecked) => {
    setChecked(isChecked);
  };

  return <Toggle checked={checked} onChange={onCheckedChange}></Toggle>;
};
// const ItemImage = (props) => <View style={styles.container}></View>;

export const ListItemSingle = (props) => (
  <ListItem
    title={props.color}
    description="Turn on the the lights"
    // accessoryLeft={ItemImage}
    accessoryRight={ToggleButton}
  />
);

export const ListItems = (props) => {
  var items = [];
  props.colors.forEach((element) => {
    console.log(element);
    items.push(
      <ListItemSingle color={element} key={element.toString()}></ListItemSingle>
    );
  });
  return items;
};

const styles = StyleSheet.create({
  container: {
    maxHeight: 320,
  },
  contentContainer: {
    paddingHorizontal: 8,
    paddingVertical: 4,
  },
  item: {
    marginVertical: 4,
  },
});
