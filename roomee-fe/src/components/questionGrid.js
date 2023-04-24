import React from 'react'
import QuestionTile from './questionTile'

export default function QuestionGrid({Questions}){
    var questionArray = []
        let questionIdx = 0
        while(questionIdx < Questions.length){
            var questionInput = <QuestionTile question = {Questions[questionIdx]}></QuestionTile>             
            questionArray.push(questionInput)
            questionIdx ++
        }
    
    return(
        <div className='quiz'>
            {questionArray}
        </div>
    )
}