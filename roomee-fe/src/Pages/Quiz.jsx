import React from 'react'
import { Link } from "react-router-dom";
import QuestionGrid from "../components/questionGrid";
//import ReactSlider from 'react-slider';
//slider code from https://www.w3schools.com/howto/howto_js_rangeslider.asp


function Quiz() {

    const mockapi = ["question1", "question2", "question3"];
 
    function getAnswers(grid){
        console.log("test")
        console.log(grid)
    }


    
    const grid = <QuestionGrid Questions = {mockapi}></QuestionGrid>
    return (
        <div className='page'>
            <h1>Quiz Page</h1>
            {grid}
            <button onClick = {getAnswers(grid)}>Submit Answers</button>
            <br></br>
            <Link to={"/"}>Go home</Link>
        </div>
    );
}
export default Quiz;
