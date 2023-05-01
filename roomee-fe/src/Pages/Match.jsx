import React from "react";
import QuestionGrid from "../components/questionGrid";
import MatchDisplay from "../components/matchDisplay";
import { useState } from "react";

function Match() {

    const [matchNo, setMatchNo] = useState(0)

    const questions = ["question1", "question2", "question3"]
    const matchNames = ["Ethan", "Josh"]
    const userName = "Evan"
    const userAnswers = [1,2,3]
    const matchAnswers = [[4,5,6], [7,8,9]]
    const matchScores = [100, 200]

    
    function nextMatch() {
        if (matchNo < matchAnswers.length - 1){
            setMatchNo(matchNo + 1)
        }
        
    }

    function previousMatch() {
        if(matchNo > 0){
            setMatchNo (matchNo - 1)
        }
    }

    
    var matches = []
    let matchIdx = 0
    while(matchIdx < matchNames.length){
        const display = <MatchDisplay questions = {questions} 
        user = {userName} userAnswers= {userAnswers} match = {matchNames[matchIdx]} 
        matchAnswers= {matchAnswers[matchIdx]}
        score = {matchScores[matchIdx]}></MatchDisplay>
        matches.push(display)
        matchIdx ++
    }


    return(
        <div className = "page">
            <h1> Match Page </h1>
                {matches[matchNo]}
                <button onClick = {previousMatch} >Previous</button>
                    <a href="/quiz">
                        <button>Edit Profile</button>
                    </a>
                <button onClick = {nextMatch}>Next</button>
        </div>
    );
}
export default Match;