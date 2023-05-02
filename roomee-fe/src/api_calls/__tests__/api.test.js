import { callApi, getQuestions, submitAnswers, isCompleted, getProfile } from './api';

beforeEach(() => {
  global.fetch = jest.fn();
});

afterEach(() => {
  jest.restoreAllMocks();
});

it('successfully gets questions', async () => {
  const responseData = [{ id: 1, question: 'Test question' }];

  global.fetch.mockResolvedValueOnce({
    ok: true,
    json: async () => responseData,
  });

  const result = await getQuestions();
  expect(global.fetch).toHaveBeenCalledTimes(1);
  expect(global.fetch).toHaveBeenCalledWith('http://localhost:5000/questions', {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json',
    },
  });
  expect(result).toEqual(responseData);
});

it('successfully submits answers', async () => {
  const questionIds = [1];
  const userId = 'testUser';
  const answers = [1];
  const responseData = { message: 'Success' };

  global.fetch.mockResolvedValueOnce({
    ok: true,
    json: async () => responseData,
  });

  const result = await submitAnswers(questionIds, userId, answers);
  expect(global.fetch).toHaveBeenCalledTimes(1);
  expect(global.fetch).toHaveBeenCalledWith('http://localhost:5000/submit-answers', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ question_id: questionIds, user_id: userId, answers: answers }),
  });
  expect(result).toEqual(responseData);
});

it('checks if quiz is completed', async () => {
  const responseData = { completed: true };

  global.fetch.mockResolvedValueOnce({
    ok: true,
    json: async () => responseData,
  });

  const result = await isCompleted();
  expect(global.fetch).toHaveBeenCalledTimes(1);
  expect(global.fetch).toHaveBeenCalledWith('http://localhost:5000/is-completed', {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json',
    },
  });
  expect(result).toEqual(responseData);
});

it('successfully gets profile information', async () => {
  const responseData = { id: 'testUser', name: 'Test User' };

  global.fetch.mockResolvedValueOnce({
    ok: true,
    json: async () => responseData,
  });

  const result = await getProfile();
  expect(global.fetch).toHaveBeenCalledTimes(1);
  expect(global.fetch).toHaveBeenCalledWith('http://localhost:5000/profile', {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json',
    },
  });
  expect(result).toEqual(responseData);
});
