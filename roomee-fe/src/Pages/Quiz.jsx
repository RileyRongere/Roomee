import React, { useEffect } from 'react'
import { Link } from "react-router-dom";
import QuestionGrid from "../components/questionGrid";
import { useState } from 'react';
import '../api_calls/api'
import { getQuestions, isCompleted, submitAnswers} from '../api_calls/api';
//import { prompt } from 'react-router';
//import ReactSlider from 'react-slider';
//slider code from https://www.w3schools.com/howto/howto_js_rangeslider.asp


function Quiz() {

    // const apiQuestionJson = getQuestions()
    // const questionList = apiQuestionJson["questions"]
    // const questionIds = apiQuestionJson["question_id"]
    // const userId = apiQuestionJson["user_id"]
    
    


    const mockapi = ["question1", "question2", "question3"];
    const questionIds = [1,2,3];
    const userId = 'Evan';
    const ExistingQuiz = "false"
    const previousQuiz = [5,5,5]


    //logic required to handle the case where the page is exited and we have a partially complete quiz
    var answerState = []
    if (ExistingQuiz == "true") {
      answerState = previousQuiz
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
    
    

    //const grid = <QuestionGrid Questions = {apiQuestionList} answers = {answers} setAnswers = {setAnswers}></QuestionGrid>
    const grid = <QuestionGrid questions = {mockapi} answers = {answers} setAnswers = {setAnswers} type = "input"></QuestionGrid>
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
//jest
export default Quiz;