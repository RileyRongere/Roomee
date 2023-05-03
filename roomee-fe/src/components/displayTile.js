import React from "react";
import { useState } from "react";
//import ReactSlider from 'react-slider'

export default function DisplayTile({ question, questionId, answers }) {
  return (
    <div className="slide" data-testid="displayTile-Test">
      <p>
        {question} : {answers[questionId]}
      </p>
    </div>
  );
}
