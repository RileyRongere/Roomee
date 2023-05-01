// api.js
export const callApi = async (endpoint, method = 'GET', body) => {
  const url = `http://localhost:5000/${endpoint}`;
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
  return await callApi('questions');
};

export const submitAnswers = async (questionIds, userId, answers) => {
  const payload = {
    question_id: questionIds,
    user_id: userId,
    answers: answers,
  };

  return await callApi('submit-answers', 'POST', payload);
};

export const isCompleted = async () => {
  return await callApi('is-completed');
};

export const getProfile = async () => {
  return await callApi('profile');
};
