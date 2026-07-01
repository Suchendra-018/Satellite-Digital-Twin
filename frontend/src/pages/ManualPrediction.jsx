import PredictionForm from "../components/prediction/PredictionForm";

function ManualPrediction() {
  return (
    <div>
      <div className="page-header">
        <h1>Manual Fault Prediction</h1>

        <p>
          Enter CubeSat telemetry values to predict faults using the trained AI
          models.
        </p>
      </div>

      <PredictionForm />
    </div>
  );
}

export default ManualPrediction;
