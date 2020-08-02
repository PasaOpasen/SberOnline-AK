import { AxiosResponse } from 'axios';

export class ReviewState {
  public teams: Array<string>;
  public tonality: number;
  public totalItems: number;
  public errorResponse: AxiosResponse;
  public isLoading: boolean;
  public isSubmitting: boolean;

  constructor() {
    this.teams = [];
    this.totalItems = 0;
    this.errorResponse = null;
    this.isSubmitting = false;
    this.isLoading = false;
  }
}
