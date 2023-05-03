// api.js
export const callApi = async (endpoint, method = "GET", body) => {
  const url = `http://localhost:5000/${endpoint}`; // Replace with your Flask API URL
  const options = {
    method,
    headers: {
      "Content-Type": "application/json",
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
  return await callApi("questions"); // Replace 'questions' with your GET endpoint
};

export const submitAnswers = async (questionIds, userId, answers) => {
  const payload = {
    question_id: questionIds,
    user_id: userId,
    answers: answers,
  };

  //console.log(payload)
  console.log("Answers Submitted!");
  //return await callApi('submit-answers', 'POST', payload); // Replace 'submit-answers' with your POST endpoint
};

export const isCompleted = async () => {
  return await callApi("is-completed"); // Replace 'is-completed' with your appropriate endpoint
};
