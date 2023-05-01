import React from 'react';
import renderer from 'react-test-renderer';
import { BrowserRouter } from 'react-router-dom';
import Quiz from './Pages/Quiz';

describe('Quiz', () => {
  it('renders correctly', () => {
    const tree = renderer
      .create(
        <BrowserRouter>
          <Quiz />
        </BrowserRouter>
      )
      .toJSON();
    expect(tree).toMatchSnapshot();
  });
});
