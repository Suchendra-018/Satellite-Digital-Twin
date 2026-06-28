def get_dashboard_data():
    """
    Returns dashboard summary.

    Later this function will read live values from:
    - Digital Twin
    - XGBoost
    - LSTM
    - Telemetry Engine
    """

    return {
        "mission_health": 98.6,
        "current_fault": "Normal",
        "prediction_confidence": 96.3,
        "active_alerts": 1,
        "satellite_mode": "Nominal",
    }