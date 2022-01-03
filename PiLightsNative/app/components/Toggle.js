import { Avatar, Button, ListItem, Toggle } from "@ui-kitten/components";
import React, { useState } from "react";

export const ToggleButton = (props) => {
  const [checked, setChecked] = React.useState(false);
  const Turnoff = () => {
    setChecked(false);
  };
  const onCheckedChange = (isChecked) => {
    // isChecked is true when on and false when off
    setChecked(isChecked);
    props.toggleCallback(props.color, isChecked);
    console.log(props.turnOffToggle);
  };

  return <Toggle checked={checked} onChange={onCheckedChange}></Toggle>;
};
