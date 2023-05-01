import {render, screen, cleanup} from '@testing-library/react';
import DisplayTile from '../displayTile';

afterEach(() => {
    cleanup();
});

//Test that the DisplayTile component displays what we expect
test('render displayile component', () => {
    const question = "Test Question ?" 
    const questionId = 0
    const answers = [0]
    render(<DisplayTile question = {question} questionId = {questionId} answers = {answers}/>);
    const displayElement = screen.getByTestId('displayTile-Test');
    expect(displayElement).toBeInTheDocument();
    expect(displayElement).toHaveTextContent('Test Question ? : 0')
});