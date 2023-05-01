import React from 'react'
import QuestionTile from './questionTile'
import DisplayTile from './displayTile'

export default function QuestionGrid({questions, answers, setAnswers, type}){
    

    //Define an array to hold the question Tiles
    var questionArray = []

        //Iterate through the questions that we have been supplied with and create a tile for each
        //Once a tile has been created, append it to the questionArray
        let questionIdx = 0

        if (type === "input") {
            while(questionIdx < questions.length){
                var questionInput = <QuestionTile  key = {questionIdx} questionId = {questionIdx} question = {questions[questionIdx]} answers = {answers} setAnswers = {setAnswers}></QuestionTile>
                questionArray.push(questionInput)
                questionIdx ++
            }
        }
        else if (type === "display") {
            while(questionIdx < questions.length){
                var questionDisplay = <DisplayTile key = {questionIdx} questionId = {questionIdx} question = {questions[questionIdx]} answers = {answers}></DisplayTile>
                questionArray.push(questionDisplay)
                questionIdx ++ 
            }
        }

    //Return the quiz in HTML form
    return(
        <div className='questionGrid' data-testid = {`QuestionGrid-Test-${type}`}>
            {questionArray}
        </div>
    )
}