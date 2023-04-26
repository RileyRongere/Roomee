import React from 'react'
import QuestionTile from './questionTile'

export default function QuestionGrid({Questions, answers, setAnswers}){
    
    //Define an array to hold the question Tiles
    var questionArray = []

        //Iterate through the questions that we have been supplied with and create a tile for each
        //Once a tile has been created, append it to the questionArray
        let questionIdx = 0
        while(questionIdx < Questions.length){
            var questionInput = <QuestionTile  key = {questionIdx} questionId = {questionIdx} question = {Questions[questionIdx]} answers = {answers} setAnswers = {setAnswers}></QuestionTile>
            questionArray.push(questionInput)
            questionIdx ++
        }

    //Return the quiz in HTML form
    return(
        <div className='quiz'>
            {questionArray}
        </div>
    )
}