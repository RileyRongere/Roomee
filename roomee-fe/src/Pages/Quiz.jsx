import React, { useEffect } from 'react'
import { Link } from "react-router-dom";
import QuestionGrid from "../components/questionGrid";
import { useState } from 'react';
//import { prompt } from 'react-router';
//import ReactSlider from 'react-slider';
//slider code from https://www.w3schools.com/howto/howto_js_rangeslider.asp


function Quiz() {

    const callApi = async (endpoint, method = 'GET', body) => {
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

    const getQuestions = async () => {
      return await callApi('questions'); // Replace 'questions' with your GET endpoint
    };

    const submitAnswers = async (questionIds, userId, answers) => {
      const payload = {
        user_id: userId,
        question_id: questionIds,
        answers: answers,
      };

      console.log(payload)
      //return await callApi('submit-answers', 'POST', payload); // Replace 'submit-answers' with your POST endpoint
    };

    const isCompleted = async () => {
      return await callApi('is-completed'); // Replace 'is-completed' with your appropriate endpoint
    };

    const mockapi = ["question1", "question2", "question3"];
    const questionIds = [1,2,3];
    const userId = 'Evan';
    const ExistingQuiz = "false"
    const Previousquiz = [5,5,5]
    //logic required to handle the case where the page is exited and we have a partially complete quiz
    var answerState = []
    if (ExistingQuiz == "true") {
      answerState = Previousquiz
    }
    else{
      answerState = Array(mockapi.length).fill(3)
    }
    
    const  [answers, setAnswers] = useState(answerState)

    //Prevent the user from leaving the page if they haven't submitted
    //Code from https://morioh.com/p/e75e83f36c8e
    useEffect(() => {
      window.addEventListener('beforeunload', alertUser)
      //window.addEventListener('unload', submitAnswers(questionIds, userId, answers))
      return () => {
        window.removeEventListener('beforeunload', alertUser)
        //window.removeEventListener('unload', submitAnswers(questionIds, userId, answers))
      }
    }, [])

    const alertUser = e => {
      e.preventDefault()
      e.returnValue = ''
    }

    const grid = <QuestionGrid Questions = {mockapi} answers = {answers} setAnswers = {setAnswers}></QuestionGrid>
    return (
        <div className='page'>
            <h1>Quiz Page</h1>
            {grid}
            <button onClick = {() => submitAnswers(questionIds, userId, answers)}>Submit Answers</button>
            <br></br>
            <Link to={"/"}>Go home</Link>
        </div>
    );
}
export default Quiz;