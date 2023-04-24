import React from 'react'
import { Link } from "react-router-dom";
import QuestionGrid from "../components/questionGrid";
//import ReactSlider from 'react-slider';
//slider code from https://www.w3schools.com/howto/howto_js_rangeslider.asp


function Quiz() {

    export const callApi = async (endpoint, method = 'GET', body) => {
      const url = `http://localhost:5000/${endpoint}`; // Replace with your Flask API URL
      const options = {
        method,
        headers: {
          'Content-Type': 'application/json',
        },
      };

      if (body) {
        options.body = JSON.stringify(body);
      }

      const response = await fetch(url, options);
      const data = await response.json();

      return data;
    };

    export const getQuestions = async () => {
      return await callApi('questions'); // Replace 'questions' with your GET endpoint
    };

    export const submitAnswers = async (questionIds, userId, answers) => {
      const payload = {
        user_id: userId,
        question_id: questionIds,
        answers: answers,
      };

      return await callApi('submit-answers', 'POST', payload); // Replace 'submit-answers' with your POST endpoint
    };

    export const isCompleted = async () => {
      return await callApi('is-completed'); // Replace 'is-completed' with your appropriate endpoint
    };

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
