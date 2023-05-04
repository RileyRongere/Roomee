import { render, screen, cleanup, fireEvent } from "@testing-library/react";
import Match from "../Match";
import previousMatch from "../Match";
import nextMatch from "../Match";
import { MemoryRouter } from "react-router-dom";

afterEach(() => {
    cleanup();
});

// tests page rendering 
test("Test that the page renders correctly", () => {
    render(
        <MemoryRouter>
            <Match />
        </MemoryRouter>
    );
    const pageHeader = screen.getByText(/Match Page/i);
    expect(pageHeader).toBeInTheDocument();
});

// tests matching rendering 
test("Test that the matching renders correctly", () => {
    render(
        <MemoryRouter>
            <Match />
        </MemoryRouter>
    );
    const matchDisplay = screen.getByTestId("match-display");
    expect(matchDisplay).toBeInTheDocument();
});

// tests previous button 
test("Test that the previous button works", () => {
    render(
        <MemoryRouter>
            <Match />
        </MemoryRouter>
    );
    const previousButton = screen.getByText(/Previous/i);
    expect(previousButton).toBeInTheDocument();

    console.log = jest.fn();

    fireEvent.click(previousButton);
    expect(console.log.mock.calls[0][0]).toBe(previousMatch);
});

// tests next button 
test("Test that the next button works", () => {
    render(
        <MemoryRouter>
            <Match />
        </MemoryRouter>
    );
    const nextButton = screen.getByText(/Next/i);
    expect(nextButton).toBeInTheDocument();

    console.log = jest.fn();

    fireEvent.click(nextButton);
    expect(console.log.mock.calls[0][0]).toBe(nextMatch);
});

// tests edit button 
test("Test that the edit button works", () => {
    render(
        <MemoryRouter>
            <Match />
        </MemoryRouter>
    );
    const editButton = screen.getByText(/Edit Profile/i);
    expect(editButton).toBeInTheDocument();

    console.log = jest.fn();

    fireEvent.click(editButton);
    expect(console.log.mock.calls[0][0]).toBe("/quiz");
});