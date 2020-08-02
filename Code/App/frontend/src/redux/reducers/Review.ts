import { Action, createReducer } from 'deox';
import { ReviewState } from '../state/Review';
import { ReviewActions } from '../actions/Review';
import { filter } from 'lodash';

const initialState = new ReviewState();

const reducer = createReducer(initialState, (handleAction) => [
  handleAction(ReviewActions.refreshState, (state) => ({
    ...state,
    ...initialState
  })),
  handleAction(ReviewActions.getTeams, (state) => ({
    ...state,
    isSubmitting: true,
    errorResponse: null
  })),
  handleAction(ReviewActions.getTeamsSuccess, (state, action) => ({
    ...state,
    isSubmitting: false,
    tonality: action.payload.tonality,
    teams: action.payload.teams,
    totalItems: action.payload.totalItems,
  })),
  handleAction(ReviewActions.getTeamsFailure, (state, action) => ({
    ...state,
    isSubmitting: false,
    errorResponse: action.payload.response
  })),
  handleAction(ReviewActions.removeTeam, (state) => ({
    ...state
  })),
  handleAction(ReviewActions.removeTeamSuccess, (state, action) => ({
    ...state,
    isSubmitting: false,
    teams: filter(state.teams, (item) => item !== action.payload)
  }))
]);

export function reviewsReducer(state: ReviewState | undefined, action: Action<any>): ReviewState {
  return reducer(state, action);
}
