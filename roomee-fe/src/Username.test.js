import { render, fireEvent, screen } from '@testing-library/react';
import Username from './Username';

describe('Username component', () => {
  test('renders a username input field', () => {
    render(<Username />);
    const usernameInput = screen.getByPlaceholderText('username');
    expect(usernameInput).toBeInTheDocument();
  });

  test('renders a submit button', () => {
    render(<Username />);
    const submitButton = screen.getByRole('button', { name: 'Submit' });
    expect(submitButton).toBeInTheDocument();
  });

  test('calls getUserExists function on form submission', () => {
    const getUserExists = jest.fn();
    render(<Username onSubmit={getUserExists} />);
    const usernameInput = screen.getByPlaceholderText('username');
    const submitButton = screen.getByRole('button', { name: 'Submit' });
    fireEvent.change(usernameInput, { target: { value: 'test@test.com' } });
    fireEvent.click(submitButton);
    expect(getUserExists).toHaveBeenCalled();
  });

  test('displays username form on initial render', () => {
    render(<Username />);
    const usernameForm = screen.getByRole('form', { name: 'username' });
    expect(usernameForm).toBeInTheDocument();
  });

  test('navigates to next page when username is entered', async () => {
    global.fetch = jest.fn(() => Promise.resolve({ ok: true }));
    const historyMock = { push: jest.fn() };
    const usernameInput = screen.getByPlaceholderText('username');
    const submitButton = screen.getByRole('button', { name: 'Submit' });
    fireEvent.change(usernameInput, { target: { value: 'ausername' } });
    fireEvent.click(submitButton);
    await screen.findByText('Next page');
    expect(historyMock.push).toHaveBeenCalledWith('/next-page');
  });
});
