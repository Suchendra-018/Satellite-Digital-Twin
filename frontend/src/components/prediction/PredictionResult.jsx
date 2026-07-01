import "./Prediction.css";

function PredictionResult({ result }) {
  if (!result) return null;

  return (
    <div className="prediction-result">
      <div className="prediction-header">
        <h2>AI Prediction Result</h2>
      </div>

      <div className="prediction-main-card">
        <h1>{result.prediction}</h1>

        <div className="confidence-section">
          <span>Confidence</span>

          <h2>{result.confidence.toFixed(2)}%</h2>
        </div>
      </div>

      <div className="prediction-grid">
        <div className="prediction-card">
          <h3>Top Predictions</h3>

          {result.top_predictions.map((item) => (
            <div key={item.fault} className="prediction-row">
              <span>{item.fault}</span>

              <strong>{item.confidence.toFixed(2)}%</strong>
            </div>
          ))}
        </div>

        <div className="prediction-card">
          <h3>Top Influencing Features</h3>

          {result.lime.map((item, index) => (
            <div key={index} className="prediction-row">
              <span>{item.feature.split(">")[0].split("<")[0]}</span>

              <strong>{Math.abs(item.impact).toFixed(3)}</strong>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}

export default PredictionResult;
