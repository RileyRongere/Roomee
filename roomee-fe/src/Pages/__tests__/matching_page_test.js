import { render, screen, cleanup, fireEvent } from "@testing-library/react";
import Match from "../Match";
import { MemoryRouter } from "react-router-dom";

afterEach(() => {
    cleanup();
});

// Tests that the Match page does not crash.
test("Test that Match component renders without crashing", () => {
    render(
      <MemoryRouter>
        <Match />
      </MemoryRouter>
    );
  });

// Tests that the next button is disabled when there are no more matches.
test("Test that the next button is disabled when there are no more matches", () => {
    render(
        <MemoryRouter>
            <Match />
        </MemoryRouter>
    );
    const nextButton = screen.getByText(/Next/i);
    expect(nextButton).toBeEnabled();

    fireEvent.click(nextButton);
    fireEvent.click(nextButton);

    expect(nextButton).toBeDisabled();
});

// Tests that the next button is enabled when there are more matches.
test("Test that the next button is enabled when there are more matches", () => {
    render(
        <MemoryRouter>
            <Match />
        </MemoryRouter>
    );
    const nextButton = screen.getByText(/Next/i);
    expect(nextButton).toBeEnabled();
});

// Tests that the previous button is disabled on the first match.
test("Test that the previous button is disabled on the first match", () => {
    render(
        <MemoryRouter>
            <Match />
        </MemoryRouter>
    );
    const previousButton = screen.getByText(/Previous/i);
    expect(previousButton).toBeDisabled();
});

// Tests that the previous button is enabled when not on the first match.
test("Test that the previous button is enabled when not on the first match", () => {
    render(
        <MemoryRouter>
            <Match />
        </MemoryRouter>
    );
    const previousButton = screen.getByText(/Previous/i);
    const nextButton = screen.getByText(/Next/i);

    fireEvent.click(nextButton);

    expect(previousButton).toBeEnabled();
});

//Tests that the next button increases the amount of match numbers.
test("Test that clicking the Next button increments the match number", () => {
    render(
      <MemoryRouter>
        <Match />
      </MemoryRouter>
    );
    const nextButton = screen.getByText(/Next/i);
    fireEvent.click(nextButton);
    
    //Checks if match number and display/attribute is set correctly.
    expect(screen.getByTestId("match-display")).toHaveTextContent(/Josh/i);
  });
  
// Tests that the score is displayed.
test("Test that the score is displayed", () => {
    render(
        <MemoryRouter>
            <Match />
        </MemoryRouter>
    );
    const matchDisplay = screen.getByTestId("match-display");
    const score = screen.getByText(/100/i); // replace with the score of the first match
    expect(matchDisplay).toContainElement(score);
});

// Tests that the correct match is displayed.
test("Test that the correct match is displayed", () => {
    render(
        <MemoryRouter>
            <Match />
        </MemoryRouter>
    );
    const matchDisplay = screen.getByTestId("match-display");
    const matchName = screen.getByText(/Ethan/i); // replace with the name of the first match
    expect(matchDisplay).toContainElement(matchName);
});