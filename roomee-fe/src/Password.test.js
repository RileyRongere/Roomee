import { render, fireEvent, screen } from '@testing-library/react';
import Password from './Password';

describe('Password component', () => {
  test('renders a password input field', () => {
    render(<Password />);
    const passwordInput = screen.getByPlaceholderText('password');
    expect(passwordInput).toBeInTheDocument();
  });

  test('renders a submit button', () => {
    render(<Password />);
    const submitButton = screen.getByRole('button', { name: 'Submit' });
    expect(submitButton).toBeInTheDocument();
  });

  test('calls searchPassword function on form submission', () => {
    const searchPassword = jest.fn();
    render(<Password onSubmit={searchPassword} />);
    const passwordInput = screen.getByPlaceholderText('password');
    const submitButton = screen.getByRole('button', { name: 'Submit' });
    fireEvent.change(passwordInput, { target: { value: 'password123' } });
    fireEvent.click(submitButton);
    expect(searchPassword).toHaveBeenCalled();
  });

  test('displays password form on initial render', () => {
    render(<Password />);
    const passwordForm = screen.getByRole('form', { name: 'password' });
    expect(passwordForm).toBeInTheDocument();
  });

  test('displays a heading based on username state', () => {
    render(<Password location={{ state: { username: 'JohnDoe' } }} />);
    const heading = screen.getByRole('heading', { level: 2 });
    expect(heading).toHaveTextContent('Enter Password Here for JohnDoe');
  });

  test('displays error message when password is incorrect', async () => {
    global.fetch = jest.fn(() => Promise.resolve({ ok: false }));
    render(<Password location={{ state: { username: 'JohnDoe' } }} />);
    const passwordInput = screen.getByPlaceholderText('password');
    const submitButton = screen.getByRole('button', { name: 'Submit' });
    fireEvent.change(passwordInput, { target: { value: 'wrongpassword' } });
    fireEvent.click(submitButton);
    const errorMessage = await screen.findByText('Incorrect password');
    expect(errorMessage).toBeInTheDocument();
  });

  test('navigates to next page when password is correct', async () => {
    global.fetch = jest.fn(() => Promise.resolve({ ok: true }));
    const historyMock = { push: jest.fn() };
    render(<Password location={{ state: { username: 'JohnDoe' } }} history={historyMock} />);
    const passwordInput = screen.getByPlaceholderText('password');
    const submitButton = screen.getByRole('button', { name: 'Submit' });
    fireEvent.change(passwordInput, { target: { value: 'correctpassword' } });
    fireEvent.click(submitButton);
    await screen.findByText('Next page');
    expect(historyMock.push).toHaveBeenCalledWith('/next-page');
  });
});
