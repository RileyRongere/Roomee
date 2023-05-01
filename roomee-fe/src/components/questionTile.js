import React from 'react'
import { useState } from 'react'
//import ReactSlider from 'react-slider'

export default function QuestionTile({question, questionId, answers, setAnswers}) {
    const [valueState, setValuestate] = useState(answers[questionId])
    
    
    function handleChange(event) {
        //Set the value of the current slider to the target value of the 
        //update
        setValuestate(event.target.value)
        
        //Update the answers array in Quz.jsx to hold the updated value
        let answersCopy = answers
        answersCopy[questionId] = Number(event.target.value)
        setAnswers(answersCopy)
    }

    return(
        <div className = "slide" data-testid = 'QuestionTile-1'>
            <p>{question}</p>
            <input type = "range" min = "1" max = "5" value = {valueState} onChange = {handleChange} list = "markers"></input>
            <datalist id = "markers">
                <option value = "1"></option>
                <option value = "2"></option>
                <option value = "3"></option>
                <option value = "4"></option>
                <option value = "5"></option>
            </datalist>
        </div>
    )
}

