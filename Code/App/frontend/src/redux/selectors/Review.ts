import { createSelector } from 'reselect';
import { AppState } from '../ConfigureStore';
import { ReviewState } from '../state/Review';

const selectFeature = (state: AppState): ReviewState => state.reviewsReducer;

export class ReviewSelectors {
  public static isLoading = createSelector(
    selectFeature,
    (state: ReviewState) => state.isLoading
  );

  public static teams = createSelector(
    selectFeature,
    (state: ReviewState) => state.teams
  );

  public static tonality = createSelector(
    selectFeature,
    (state: ReviewState) => state.tonality
  );

  public static totalItems = createSelector(
    selectFeature,
    (state: ReviewState) => state.totalItems
  );

  public static errorResponse = createSelector(
    selectFeature,
    (state: ReviewState) => state.errorResponse
  );

  public static isSubmitting = createSelector(
    selectFeature,
    (state: ReviewState) => state.isSubmitting
  );
}
