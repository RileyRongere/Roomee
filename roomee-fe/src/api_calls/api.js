// callApi calls the api endpoint and allows the user to submit and receive data from the back end
function buildOptions(method, body) {
  var options = {
    headers: {
      "Content-Type": "application/json",
    },
  };
  if (arguments[1] === undefined) {
    options["method"] = method;
  } else if (arguments[1] !== undefined) {
    options["method"] = method;
    options["body"] = JSON.stringify(body);
  }
  return options;
}

export const callApi = async (endpoint, method, body) => {
  console.log("call api");

  const url = `http://localhost:3050/api/${endpoint}`;
  const options = buildOptions(method, body);

  const response = await fetch(url, options);
  // const data = await response.json();
  // const data = response;
  return response;
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
  return await callApi("submitAnswers", "POST", payload);
};

// Gets a list of matches when the api is given a user_id
export const getMatches = async (payload) => {
  return await callApi("match", payload);
};

// Boolean Value that checks to see if the user exists
export const getUserExists = async (user_id) => {
  const userBase = "user/";
  const userEndpoint = userBase.concat(user_id);
  let getUserResponse = await callApi(userEndpoint, "PUT", undefined).then(
    (response) => response
  );
  const userStatus = getUserResponse["status"];
  return userStatus;
};

// Submits password and username to the api team to be written in the database
export const submitPassword = async (username, password) => {
  const payload = {
    username: username,
    password: password,
  };
  console.log("Password Submitted!");
  return await callApi("login", "POST", payload);
};

// Submits a username and password pair to login endpoint
export const userLogin = async (username, password) => {
  const payload = {
    username: username,
    password: password,
  };
  console.log("User login!");
  let loginResponse = await callApi("login", "POST", payload).then((response) =>
    response.json()
  );
  // console.log("RESPONSE")
  // console.log(loginResponse)
  return loginResponse;
};

// Submits a username and password pair to the register endpiont
export const userRegister = async (username, password) => {
  const payload = {
    username: username,
    password: password,
  };
  console.log("User register!");
  return await callApi("register", "POST", payload);
};
