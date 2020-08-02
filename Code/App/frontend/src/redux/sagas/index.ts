import { all } from 'redux-saga/effects';
import review from './Review';

export default function * sagas () {
  yield all([
    review()
  ]);
}
