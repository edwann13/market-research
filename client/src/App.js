import logo from './logo.svg';
import './App.css';
import axios from 'axios';

function App() {
  const lambdaUrl = "https://v7exa47g23m3yy3chav3iclgme0egtjn.lambda-url.us-west-1.on.aws/";
  const getMarketResearch = async () => {
    const config = {
      baseURL: lambdaUrl,
    };
    const response = await axios.get('/', config);
    console.log(response);
    return response;
  }

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code onClick={getMarketResearch}>src/App.js</code> and save to reload.
          THIS IS A TEST
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
