import { Expose } from 'class-transformer';

export class ReviewResponse {
  @Expose()
  public teams: Array<string>;

  @Expose()
  public tonality: number;

  @Expose({ name: 'total_items'})
  public totalItems: number;

  constructor(model: Partial<ReviewResponse> = {}) {
    Object.assign(this, model);
  }
}
