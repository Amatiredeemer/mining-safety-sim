import random
import time
import threading

# Simple classes to represent layers
class IntegrationLayer:
    def __init__(self):
        self.thermal_sensor = lambda: random.uniform(20, 80)  # Simulates temp in °C
        self.camera_api = lambda: random.choice(["clear", "person_detected", "equipment_malfunction"])  # Simulates camera feed

    def get_sensor_data(self):
        return {
            "temperature": self.thermal_sensor(),
            "camera_status": self.camera_api()
        }

class ProcessingLayer:
    def __init__(self):
        self.safety_threshold_temp = 50  # °C
        self.geological_risk_factor = 0.1  # Base risk (0-1)

    def process_data(self, data):
        temp = data["temperature"]
        camera = data["camera_status"]
        
        # Simulate MineSight UA Engine: Basic path adjustment (placeholder)
        ua_output = "Path stable" if temp < 40 else "Adjust path for heat"
        
        # Geological Intelligence: Simple risk calc based on temp
        geo_risk = self.geological_risk_factor + (temp / 100)
        
        # Safety Protocol Engine: Check for alerts
        alert = "No alert"
        if temp > self.safety_threshold_temp or camera == "equipment_malfunction":
            alert = "HIGH RISK: Shutdown initiated"  # Simulate control system trigger
        
        return {
            "ua_output": ua_output,
            "geo_risk": geo_risk,
            "alert": alert
        }

class ApplicationLayer:
    def __init__(self):
        self.alerts = []

    def display_dashboard(self, processed_data):
        print("--- Safety Dashboard ---")
        print(f"Temperature: {processed_data.get('temperature', 'N/A')}°C")
        print(f"Camera Status: {processed_data.get('camera_status', 'N/A')}")
        print(f"UA Engine: {processed_data.get('ua_output', 'N/A')}")
        print(f"Geological Risk: {processed_data.get('geo_risk', 'N/A'):.2f}")
        print(f"Alert: {processed_data.get('alert', 'N/A')}")
        print("------------------------")

    def manage_alert(self, alert):
        if alert != "No alert":
            self.alerts.append(alert)
            print(f"ALERT TRIGGERED: {alert} (Logged {len(self.alerts)} alerts)")

# Simulation loop
def run_simulation():
    integration = IntegrationLayer()
    processing = ProcessingLayer()
    application = ApplicationLayer()
    
    print("Starting Mining Safety Simulation... (Press Ctrl+C to stop)")
    try:
        while True:
            # Get raw data
            raw_data = integration.get_sensor_data()
            
            # Process it
            processed_data = processing.process_data(raw_data)
            processed_data.update(raw_data)  # Merge for display
            
            # Display and handle alerts
            application.display_dashboard(processed_data)
            application.manage_alert(processed_data["alert"])
            
            time.sleep(2)  # Simulate real-time delay
    except KeyboardInterrupt:
        print("Simulation stopped.")

# Run in a thread for concurrency (e.g., simulating parallel sensor polling)
if __name__ == "__main__":
    sim_thread = threading.Thread(target=run_simulation)
    sim_thread.start()
    sim_thread.join()