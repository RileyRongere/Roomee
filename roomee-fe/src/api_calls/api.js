// callApi calls the api endpoint and allows the user to submit and receive data from the back end
export const callApi = async (endpoint, method = "GET", body) => {
  const url = `http://localhost:5000/${endpoint}`;
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

// Function to get questions for the Quiz.jsx page
export const getQuestions = async () => {
  return await callApi("questions");
};

// Submits the answers of the questions to the api so they can be written to DB
export const submitAnswers = async (questionIds, userId, answers) => {
  const payload = {
    question_id: questionIds,
    user_id: userId,
    answers: answers,
  };

  //console.log(payload)
  console.log("Answers Submitted!");
  return await callApi('submitAnswers', 'POST', payload);
};

// Gets a list of matches when the api is given a user_id
export const getMatches = async (payload) => {
  return await callApi('match', payload);
};


export const getUserExists = async (user_id) => {
   return await callApi(user_id, 'PUT')
};
