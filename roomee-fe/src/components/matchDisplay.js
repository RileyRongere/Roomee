import React from "react";
import QuestionGrid from "./questionGrid";

export default function MatchDisplay({
  questions,
  user,
  userAnswers,
  match,
  matchAnswers,
  score,
}) {
  const userAnswersGrid = (
    <QuestionGrid
      questions={questions}
      answers={userAnswers}
      type="display"
    ></QuestionGrid>
  );
  const matchAnswersGrid = (
    <QuestionGrid
      questions={questions}
      answers={matchAnswers}
      type="display"
    ></QuestionGrid>
  );

  return (
    <div className="matchContainer" data-testid="MatchDisplay-Test">
      <h2>
        You had a {score} match score with {match}!
      </h2>
      <p>Compare your answers below</p>
      <div className="matchDisplay">
        <div className="userAnswers">
          <h3>Your Answers</h3>
          {userAnswersGrid}
        </div>

        <div className="matchAnswers">
          <h3>{match}'s Answers</h3>
          {matchAnswersGrid}
        </div>
      </div>
    </div>
  );
}
