import { StyleSheet, View, SafeAreaView, Platform } from "react-native";
import { Avatar, Button, ListItem, Toggle } from "@ui-kitten/components";
import React, { useState } from "react";
import { ToggleButton } from "./Toggle";
const lightState = React.createContext("off");

export const ListItemSingle = (props) => (
  <ListItem
    title={props.color}
    description="Turn on the the lights"
    accessoryRight={
      <ToggleButton
        color={props.color}
        toggleCallback={props.toggleCallback}
        turnOffToggle={props.turnOffToggle}
      />
    }
  />
);

export const ListItems = (props) => {
  var items = [];
  const toggleCallback = (color, state) => {
    items.forEach((element) => {
      if (element.key === color) {
        // console.log("Called From the list " + color, state);
      } else {
        console.log("Called From the list " + element.key, false);
        // console.log(element.props);
        turnOffToggle(element.key);
      }
    });
    console.log("\n");
    // turnOffToggle();
  };

  // It takes in a key/color and sets the child with that color to false
  const turnOffToggle = (key) => {
    return key;
  };
  props.colors.forEach((element) => {
    items.push(
      <ListItemSingle
        color={element}
        key={element.toString()}
        toggleCallback={toggleCallback}
        turnOffToggle={turnOffToggle}
      ></ListItemSingle>
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
