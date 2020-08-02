import React, { ReactElement } from 'react';
import { useSelector } from 'react-redux';
import { ReviewSelectors } from '../../redux/selectors/Review';
import { TeamsItem } from '../../components/TeamsItem/TeamsItem';
import './TeamItems.scss';
import { Loader } from '../../components/Loader/Loader';
import store from '../../redux/ConfigureStore';
import { ReviewActions } from '../../redux/actions/Review';

export function TeamItems(): ReactElement {
  let items = useSelector(ReviewSelectors.teams);
  let reviewTonality = useSelector(ReviewSelectors.tonality);
  const isFormSubmitting = useSelector(ReviewSelectors.isSubmitting);

  const removeItem = (item: string): void => {
    store.dispatch(ReviewActions.removeTeamSuccess(item));
  }

  const getTonalityEmoji = (): string => {
    if (!reviewTonality) {
      return '🙂';
    }

    if (reviewTonality > 0.6) {
      return '😜️️';
    } else if (reviewTonality > 0.3) {
      return '😊';
    } else if (reviewTonality > 0) {
      return '🙂';
    } else if (reviewTonality > -0.3) {
      return '😠';
    } else if (reviewTonality > -0.6) {
      return '😡';
    } else {
      return '🤬';
    }
  }

  return (
    <div>
      <div className="skill-items">
        <span className="skill-items-title">Тональность отзыва:</span>
        <div className="skill-items-data">
          <span className="skill-items-data-emoji">
            {getTonalityEmoji()}
          </span>
          <span className="skill-items-data-number">
            {reviewTonality}
          </span>
        </div>
      </div>
      <div className="skill-items">
        <span className="skill-items-title">Определенные команды:</span>
        {
          (isFormSubmitting)
            ? <Loader />
            : (items.length)
            ? (
              <div className="skill-items-data">
                {
                  items.map((item, key) => (
                    <TeamsItem
                      key={key}
                      item={item}
                      handleRemove={removeItem}
                    />
                  ))
                }
              </div>
            )
            : (
              <div className="skill-items-empty">
                Введи данные в поле, для того, чтоб мы определили команды которые могут помочь
              </div>
            )
        }
      </div>
    </div>
  );
}
