import * as React from 'react';
import { FlatList, Text, TouchableOpacity, View } from 'react-native';
import EStyleSheet from 'react-native-extended-stylesheet';
import { Col, Row, Grid } from "react-native-easy-grid";

export default function Tasks() {
  const data = [
    {id: 10, task: 'Ошибка из отзыва AppStore #7', desc: 'Приложение долго запускается', due_date: '22.04.2020'},
    {id: 9, task: 'Ошибка из отзыва Google Play #3', desc: 'Не могу оформить самозанятость', due_date: '12.03.2020'},
    {id: 8, task: 'Ошибка из отзыва AppStore #6', desc: 'Не могу оплатить кредит', due_date: '08.03.2020'},
    {id: 7, task: 'Ошибка из отзыва AppStore #5', desc: 'Вообщем все в порядке, но подтормаживает', due_date: '08.03.2020'},
    {id: 6, task: 'Ошибка из отзыва AppStore #4', desc: 'Отличное приложение, но часто виснет на оплате', due_date: '03.03.2020'},
    {id: 5, task: 'Ошибка из отзыва Google Play #2', desc: 'Не могу офрмить кредитную карту', due_date: '02.02.2020'},
    {id: 4, task: 'Ошибка из отзыва AppStore #3', desc: 'Все вроде работает, но у банка нет опции процента на остаток', due_date: '02.02.2020'},
    {id: 3, task: 'Ошибка из отзыва AppStore #2', desc: 'Зависает при запуске', due_date: '31.12.2019'},
    {id: 2, task: 'Ошибка из отзыва Google Play #1', desc: 'Не проходит оплата', due_date: '22.12.2019'},
    {id: 1, task: 'Ошибка из отзыва AppStore #1', desc: 'Не верное отображение баланса', due_date: '12.11.2019'},
  ];

  const styles = EStyleSheet.create({
    mainContainer: {
      fontFamily: "Roboto-Light"
    },
    taskCard: {
      padding: 20,
      margin: 20,
      marginTop: 3,
      backgroundColor: '#fff',
      borderRadius: 10,
      shadowColor: '#000',
      shadowOpacity: 0.1,
      shadowOffset: {width: 0, height: 3}
    },
    taskCard_label: {
      position: 'absolute',
      right: 0,
      marginTop: 10,
      marginRight: 10,
      backgroundColor: '#f1be1d',
      borderRadius: 10,
      padding: 3
    },
    taskCard_title: {
      fontFamily: "Roboto-Bold",
      fontSize: 16
    },
    taskCard_item_title: {
      color: '#6F8094',
      marginTop: 10
    },
    taskCard_item_info: {
      marginTop: 10,
      marginRight: 10
    },
  });

  const openTask = (taskId: number): void => {
    console.log(taskId);
  }

  return (
    <View style={styles.mainContainer}>
      <FlatList
        data={data}
        renderItem={({item, index}) => (
          <TouchableOpacity
            key={index.toString()}
            onPress = {() => openTask(item.id)}
            style={EStyleSheet.child(styles, 'taskCard', index, data.length)}
          >
            <Text style={styles.taskCard_title}>
              {item.task}
            </Text>
            <Grid>
              <Row>
                <Col size={30}>
                  <Text style={styles.taskCard_item_title}>
                    Описание:
                  </Text>
                </Col>
                <Col size={70}>
                  <Text style={styles.taskCard_item_info}>
                    {item.desc}
                  </Text>
                </Col>
              </Row>
              <Row>
                <Col size={30}>
                  <Text style={styles.taskCard_item_title}>
                    Дата:
                  </Text>
                </Col>
                <Col size={70}>
                  <Text style={styles.taskCard_item_info}>
                    {item.due_date}
                  </Text>
                </Col>
              </Row>
            </Grid>

            <View style={styles.taskCard_label}>
              <Text>To do</Text>
            </View>
          </TouchableOpacity>
        )}
      />
    </View>
  );
}
