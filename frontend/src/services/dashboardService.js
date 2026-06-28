const API_URL = "http://127.0.0.1:8000";

export async function getDashboardData() {
    try {
        const response = await fetch(`${API_URL}/api/dashboard`);

        if (!response.ok) {
            throw new Error("Failed to fetch dashboard data");
        }

        return await response.json();

    } catch (error) {

        console.error("Dashboard API Error:", error);

        throw error;
    }
}