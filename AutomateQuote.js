import React, { useState } from "react";
import "./App.css";

const quotes = [
  "Men like us, Mr. Shelby, will always be alone. And what love we get, we will have to pay for.",
  "May you be in heaven a full half-hour before the Devil knows you are Dead.",
  "Sometimes the women have to take over. Like in the war.",
  "Already broken.",
  "I dont pay for suits. My suits are on the house or the house burns down.",
  "In politics, no one is indispensable. I regret I have not been successful.",
  "I am sad... to be giving up the best job in the world.",
  "I am not a great actor. I am a great actor.",
  "I will support the new leader."
]

function App() {
  const [quote, setQuote] = useState(quotes[0])

  function randomizeQuote() {
    const randomQuote = quotes[Math.floor(Math.random() * quotes.length)];
    setQuote(randomQuote);
  }

  return (
    <div className="App">
      <div>
        {quote}
      </div>
      <button onClick={randomizeQuote}>Click Me Hard</button>
    </div>
  );
}

export default App;
