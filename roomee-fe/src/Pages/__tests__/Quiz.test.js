import { render, screen, cleanup, fireEvent } from "@testing-library/react";
import Quiz from "../Quiz";
import { MemoryRouter } from "react-router-dom";

afterEach(() => {
  cleanup();
});

test("Test that the page renders correctly", () => {
  render(
    <MemoryRouter>
      <Quiz />
    </MemoryRouter>
  );
  const pageHeader = screen.getByText(/Quiz Page/i);
  expect(pageHeader).toBeInTheDocument();
});

test("Test that the submit button works", () => {
  render(
    <MemoryRouter>
      <Quiz />
    </MemoryRouter>
  );
  const submitButton = screen.getByText(/Submit Answers/i);
  expect(submitButton).toBeInTheDocument();

  console.log = jest.fn();

  fireEvent.click(submitButton);
  expect(console.log.mock.calls[0][0]).toBe("Answers Submitted!");
});

// Not gonna worry about this
// test("Test that a pop-up appears when the page is unloaded", () => {
//   render(
//     <MemoryRouter>
//       <Quiz />
//     </MemoryRouter>
//   );

//   // window.dispatchEvent(new Event("beforeunload"));
//   // const unloadNotice = screen.getByText(/Reload site?/i);
//   // expect(unloadNotice).toBeInTheDocument();
// });
