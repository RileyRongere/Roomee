import React from 'react'
import { useState } from 'react'
//import ReactSlider from 'react-slider'

export default function QuestionTile({question}) {
    const [sliderValue, setSliderValue] = useState(3)

    function handleChange(event) {
        setSliderValue(event.target.value)
        console.log(event.target.value)
    }

    return(
        <div className = "slide">
            <p>{question}</p>
            <input type = "range" min = "1" max = "5" value = {sliderValue} onChange={handleChange}></input>
        </div>
    )
}

