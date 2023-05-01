import { render, screen, cleanup } from "@testing-library/react";
import "@testing-library/jest-dom";
import QuestionGrid from "../questionGrid";

afterEach(() => {
  cleanup();
});

test("Render a QuestionGrid for Display", () => {
  const questions = ["Test Question 1?"];
  const answers = [0];
  const setAnswers = "test";
  const type = "display";

  render(
    <QuestionGrid
      questions={questions}
      answers={answers}
      setAnswers={setAnswers}
      type={type}
    />
  );
  const questionGridElement = screen.getByTestId("QuestionGrid-Test-display");
  expect(questionGridElement).toBeInTheDocument();
  expect(questionGridElement).toHaveTextContent("Test Question 1? : 0");
});

test("Render a QuestionGrid for Input", () => {
  const questions = ["Test Question 1?"];
  const answers = [0];
  const setAnswers = "test";
  const type = "input";

  render(
    <QuestionGrid
      questions={questions}
      answers={answers}
      setAnswers={setAnswers}
      type={type}
    />
  );
  const questionGridElement = screen.getByTestId("QuestionGrid-Test-input");
  expect(questionGridElement).toBeInTheDocument();
  expect(questionGridElement).toHaveTextContent("Test Question 1?");
});
