import { render, screen } from "@testing-library/react";
import { BrowserRouter } from "react-router-dom";
import renderer from "react-test-renderer";
import App from "./App";

test("renders learn react link", () => {
  render(
    <BrowserRouter>
      <App />
    </BrowserRouter>
  );

  const linkElement = screen.getByText(/learn react/i);
  expect(linkElement).toBeInTheDocument();
});

it("renders correctly", () => {
  const tree = renderer
    .create(
      <BrowserRouter>
        <App />
      </BrowserRouter>
    )
    .toJSON();
  expect(tree).toMatchSnapshot();
});
