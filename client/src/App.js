import './App.css';
import axios from 'axios';
import { useState } from 'react';
import ClipLoader from "react-spinners/ClipLoader";

function App() {
  const [company_name, setCompanyName] = useState("");
  const [aiReply, setReply] = useState("");
  const [loading, setLoading] = useState(false);

  const lambdaUrl = "https://v7exa47g23m3yy3chav3iclgme0egtjn.lambda-url.us-west-1.on.aws/";
  // const lambdaUrl = "http://127.0.0.1:8000/"

  const getMarketResearch = async (event) => {
    event.preventDefault();
    if (company_name.length === 0) {
      return;
    }
    try {
      const config = {
        baseURL: lambdaUrl,
      };
      setLoading(true);
      const apiRoute = `/market-research/${company_name}`;
      const response = await axios.get(apiRoute, config);
      const reply = response.data.choices[0].message.content;
      setReply(reply);
      setLoading(false);
    } catch (err) {
      setLoading(false);
      console.log(err);
    }
  }

  const resetPrompt = () => {
    setReply("");
    setCompanyName("");
    setLoading(false);
  }

  return (
    <div className="App">
      <header className="App-header">
        {(aiReply.length === 0 && !loading) &&
          <form onSubmit={getMarketResearch}>
            <label>Conduct Competitive Market Analysis</label>
            <br/>
            <label>Enter company name:
              <input
                type="text"
                value={company_name}
                onChange={(e) => setCompanyName(e.target.value)}
                />
            </label>
            <input style={{fontSize: "15px"}} type="submit"/>
          </form>
        }
        {loading && 
        <div>
          <span>Conducting Research</span>
          <br />
          <ClipLoader
          color="green"
          loading={loading}
          size={150}
          aria-label='Loading Spiiner'
          data-testid="loader"
          />
        </div>
        }
        {aiReply.length > 0 &&
          <div>
            <p style={{margin: "0 auto", width: '70%', whiteSpace: "pre-line", fontSize: "25px"}}>{aiReply}</p>
            <button type="button" style={{fontSize: "25px"}} onClick={resetPrompt}>Reset</button>
          </div>
        }
      </header>
    </div>
  );
}

export default App;
