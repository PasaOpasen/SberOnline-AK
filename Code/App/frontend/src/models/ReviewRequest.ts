import { Expose } from 'class-transformer';

export class ReviewRequest {
  @Expose()
  public review: string;

  constructor(model: Partial<ReviewRequest> = {}) {
    Object.assign(this, model);
  }
}
