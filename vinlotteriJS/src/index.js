import React from "react";
import ReactDOM from "react-dom";

import "./app.css";

class App extends React.Component {
  render() {
    return (
      <div className="App">
        <h1>Hello World</h1>
        <input></input>
        <button>Click me</button>
      </div>
    );
  }
}

const rootElement = document.getElementById("root");
ReactDOM.render(<App />, rootElement);
