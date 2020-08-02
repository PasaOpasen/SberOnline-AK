import React, { ReactElement } from 'react';
import * as Yup from 'yup';
import './ReviewForm.scss';
import { ServerValidationErrors } from '../../components/ServerValidationError/ServerValidationError';
import { FormikProps, FormikValues, Form, Field, Formik } from 'formik';
import { TextareaField } from '../../components/TextareaField/TextareaField';
import { SubmitButton } from '../../components/SubmitButton/SubmitButton';
import { ReviewRequest } from '../../models/ReviewRequest';
import { ReviewSelectors } from '../../redux/selectors/Review';
import { useSelector } from 'react-redux';
import { ReviewActions } from '../../redux/actions/Review';
import store from '../../redux/ConfigureStore';

export function ReviewForm(): ReactElement {
  const errorResponse = useSelector(ReviewSelectors.errorResponse);
  const isSubmitting = useSelector(ReviewSelectors.isSubmitting);

  const initialValues: ReviewRequest = {
    review: '',
  };

  const validationSchema = Yup.object().shape({
    review: Yup.string().required('Ошибка')
  });

  const sendResumeText = (values: FormikValues): void => {
    const credentials = new ReviewRequest({
      review: values.review
    });

    store.dispatch(ReviewActions.getTeams(credentials));
  }

  return (
    <div>
      <span className="skill-items-title">Твой отзыв:</span>

      <Formik
        initialValues={initialValues}
        onSubmit={sendResumeText}
        validationSchema={validationSchema}
      >
        {
          (props: FormikProps<FormikValues>): ReactElement => (
            <Form className="form resume-form">
              <Field
                name="review"
                component={TextareaField}
                onChange={props.handleChange}
                error={props.errors.review}
                touched={props.touched.review}
                value={props.values.review}
              />

              <ServerValidationErrors errorResponse={errorResponse}/>

              <SubmitButton
                text="Определить команды и тональность"
                isSubmitting={isSubmitting}
              />
            </Form>
          )
        }
      </Formik>
    </div>
  );
}
