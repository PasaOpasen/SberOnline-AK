import { classToPlain, plainToClass } from 'class-transformer';
import { isUndefined, omitBy } from 'lodash';
import ApiClient from './ApiClient';
import { ReviewRequest } from '../../models/ReviewRequest';
import { ReviewResponse } from '../../models/ReviewResponse';

const apiClient = new ApiClient();

export class ReviewService {
  public static getSkills(credentials: ReviewRequest): Promise<ReviewResponse> {
    const data = omitBy(classToPlain<ReviewRequest>(credentials), isUndefined);

    return apiClient
      .post({ endpoint: '/api/review', data })
      .then((resp) => plainToClass(ReviewResponse, resp.data));
  }
}
