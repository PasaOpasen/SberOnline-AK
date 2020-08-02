import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import MenuTabs from "./src/components/MenuTabs/MenuTabs";
import { createStackNavigator } from "@react-navigation/stack";
import EStyleSheet from 'react-native-extended-stylesheet';
import { AppLoading } from 'expo'
import * as Font from 'expo-font';

export default function App() {
  let isFontsLoaded = false;
  const Stack = createStackNavigator();

  React.useLayoutEffect(() => {
    Font.loadAsync({
      'Roboto-Light': require('./assets/fonts/Roboto-Light.ttf'),
      'Roboto-Bold': require('./assets/fonts/Roboto-Bold.ttf')
    })
      .then(() => {
      isFontsLoaded = true;
    })
  }, []);


  return (
    <NavigationContainer>
      <Stack.Navigator>
        <Stack.Screen name="Main" component={MenuTabs} />
      </Stack.Navigator>
    </NavigationContainer>
  );
}

EStyleSheet.build({
    $textColor: '#0275d8'
});
