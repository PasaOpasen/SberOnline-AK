import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import { MaterialCommunityIcons } from '@expo/vector-icons';
import Tasks from '../../screens/Tasks/Tasks';
import React from 'react';
import Updates from '../../screens/Updates/Updates';
import Profile from '../../screens/Profile/Profile';
import { getFocusedRouteNameFromRoute } from '@react-navigation/native';

export default function MenuTabs({ navigation, route }) {
  const Tab = createBottomTabNavigator();

  const getHeaderTitle = (route) => {
    const routeName = getFocusedRouteNameFromRoute(route) ?? 'Tasks';

    switch (routeName) {
      case 'Tasks':
        return 'Задачи команды';
      case 'Profile':
        return 'Мой профиль';
      case 'Reviews':
        return 'Отзывы';
      case 'Updates':
        return 'Обновления';
    }
  }

  React.useLayoutEffect(() => {
    navigation.setOptions({ headerTitle: getHeaderTitle(route) });
  }, [navigation, route]);

  return (
    <Tab.Navigator
      initialRouteName="Feed"
      tabBarOptions={{
        activeTintColor: '#e91e63',
        style: {
          height: 60,
          borderTopWidth: 0
        }
      }}
    >
      <Tab.Screen
        name="Updates"
        component={Updates}
        options={{
          tabBarLabel: 'Обновления',
          tabBarIcon: ({ color, size }) => (
            <MaterialCommunityIcons name="bell" color={color} size={size} />
          )
        }}
      />
      <Tab.Screen
        name="Tasks"
        component={Tasks}
        options={{
          tabBarLabel: 'Задачи',
          tabBarIcon: ({ color, size }) => (
            <MaterialCommunityIcons name="book-open-variant" color={color} size={size} />
          ),
        }}
      />
      <Tab.Screen
        name="Reviews"
        component={Tasks}
        options={{
          tabBarLabel: 'Отзывы',
          tabBarIcon: ({ color, size }) => (
            <MaterialCommunityIcons name="ballot" color={color} size={size} />
          ),
        }}
      />
      <Tab.Screen
        name="Profile"
        component={Profile}
        options={{
          tabBarLabel: 'Профиль',
          tabBarIcon: ({ color, size }) => (
            <MaterialCommunityIcons name="account" color={color} size={size} />
          ),
        }}
      />
    </Tab.Navigator>
  );
}
