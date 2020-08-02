import { call, put, takeLatest } from 'redux-saga/effects';
import { SagaIterator } from 'redux-saga';
import { Action } from 'deox';
import { ReviewService } from '../../services/api/Review';
import { ReviewRequest } from '../../models/ReviewRequest';
import { ReviewActions } from '../actions/Review';

function * getTeamsList(action: Action<string, ReviewRequest>): SagaIterator {
  try {
    const createdNews = yield call(ReviewService.getSkills, action.payload);

    yield put(ReviewActions.getTeamsSuccess(createdNews));
  } catch (e) {
    yield put(ReviewActions.getTeamsFailure(e));
  }
}

function * review(): SagaIterator {
  yield takeLatest(ReviewActions.getTeams, getTeamsList);
}

export default review;
