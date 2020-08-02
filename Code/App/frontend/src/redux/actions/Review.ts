import { AxiosError } from 'axios';
import { createActionCreator } from 'deox';
import { ReviewResponse } from '../../models/ReviewResponse';
import { ReviewRequest } from '../../models/ReviewRequest';

export class ReviewActions {
  public static refreshState = createActionCreator(
    '[Main Page] Refresh State'
  );

  public static getTeams = createActionCreator(
    '[Main Page] Get Teams By Review',
    (resolve) => (data: ReviewRequest) => resolve(data)
  );

  public static getTeamsSuccess = createActionCreator(
    '[Main Page] Get Teams By Review Success',
    (resolve) => (data: ReviewResponse) => resolve(data)
  );

  public static getTeamsFailure = createActionCreator(
    '[Main Page] Get Teams By Review Failure',
    (resolve) => (response: AxiosError) => resolve(response)
  );

  public static removeTeam = createActionCreator(
    '[News Page] Remove Team',
    (resolve) => (data: string) => resolve(data)
  );

  public static removeTeamSuccess = createActionCreator(
    '[News Page] Remove Team Success',
    (resolve) => (data: string) => resolve(data)
  );
}
