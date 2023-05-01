import {render, screen, cleanup} from '@testing-library/react';
import MatchDisplay from '../matchDisplay';

afterEach(() => {
    cleanup();
});

//Test that the text that is unique to MatchDisplay is outputted correctly
//The Question Grids have already been tested
test('Render MatchDisplay component', () => {
    const questions = ["Test QUestion 1?"]
    const user = "Evan"
    const userAnswers = [1]
    const match = "Ethan"
    const matchAnswers = [2]
    const score = 100

    render(<MatchDisplay questions = {questions} user = {user} userAnswers={userAnswers} match = {match} matchAnswers={matchAnswers} score={score}/>)
    const matchDisplayElement = screen.getByTestId('MatchDisplay-Test')
    expect(matchDisplayElement).toBeInTheDocument()
    expect(matchDisplayElement).toHaveTextContent("You had a 100 match score with Ethan!")
    expect(matchDisplayElement).toHaveTextContent("Compare your answers below")
    expect(matchDisplayElement).toHaveTextContent("Your Answers")
    expect(matchDisplayElement).toHaveTextContent("Ethan's Answers") 
});  