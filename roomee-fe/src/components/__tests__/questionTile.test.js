import { render, screen, cleanup } from "@testing-library/react";
import QuestionTile from "../questionTile";

afterEach(() => {
  cleanup();
});

test("Render QuestionTile Component", () => {
  const question = "Test Question 1?";
  const questionId = 0;
  var answers = [0];
  const setAnswers = "Ask about this";
  render(
    <QuestionTile
      question={question}
      questionId={questionId}
      answers={answers}
      setAnswers={setAnswers}
    />
  );
  const questionTileElement = screen.getByTestId("QuestionTile-1");
  expect(questionTileElement).toHaveTextContent("Test Question 1?");
});
