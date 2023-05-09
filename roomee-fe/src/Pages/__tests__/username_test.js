import React from 'react';
import { render, fireEvent, waitFor, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import Username from './Username';

describe('Username Component', () => {
  test('renders username input field', () => {
    render(<Username />);
    const usernameInput = screen.getByLabelText('Username');
    expect(usernameInput).toBeInTheDocument();
  });

  test('updates state when input field is changed', async () => {
    render(<Username />);
    const usernameInput = screen.getByLabelText('Username');
    await userEvent.type(usernameInput, 'testuser');
    expect(usernameInput).toHaveValue('testuser');
  });

  test('calls navigate function with correct arguments when submit button is clicked', async () => {
    render(<Username />);
    const usernameInput = screen.getByLabelText('Username');
    await userEvent.type(usernameInput, 'testuser');
    const submitButton = screen.getByRole('button', { name: /submit/i });
    fireEvent.click(submitButton);
    await waitFor(() => expect(screen.getByText(/password/i)).toBeInTheDocument());
    expect(screen.getByText(/testuser/i)).toBeInTheDocument();
  });

  test('logs the username to the console', async () => {
    console.log = jest.fn();
    render(<Username />);
    const usernameInput = screen.getByLabelText('Username');
    await userEvent.type(usernameInput, 'testuser');
    const submitButton = screen.getByRole('button', { name: /submit/i });
    fireEvent.click(submitButton);
    await waitFor(() => expect(console.log).toHaveBeenCalledWith('testuser'));
  });

  test('navigates to password page with correct state when submit button is clicked', async () => {
    const navigateMock = jest.fn();
    jest.mock('react-router-dom', () => ({
      ...jest.requireActual('react-router-dom'),
      useNavigate: () => navigateMock,
    }));
    render(<Username />);
    const usernameInput = screen.getByLabelText('Username');
    await userEvent.type(usernameInput, 'testuser');
    const submitButton = screen.getByRole('button', { name: /submit/i });
    fireEvent.click(submitButton);
    await waitFor(() =>
      expect(navigateMock).toHaveBeenCalledWith('/password', {
        state: { name: { userName: 'testuser' } },
      })
    );
  });
});