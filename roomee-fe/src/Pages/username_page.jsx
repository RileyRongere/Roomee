import React from 'react';
import { Link } from "react-router-dom";

export function App(props)
 {
  return (
    <div className="container" >
      <h1>Roomee</h1>
      <h2>Login</h2>
        <form>
          <label>
          <input type="email" placeholder="Username" name="name" />
          </label>
      <input type="submit" value="Submit" />
      </form>
      
    </div>
    
  );
}

// Log to console
console.log('Username Entered')