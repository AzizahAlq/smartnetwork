import dds  # Python bindings for OpenDDS
from flask import Flask, render_template
import threading

app = Flask(__name__)
router_states = {}

def subscribe_to_router_states():
    # Initialize DDS domain participant, subscriber, and topic
    participant = dds.DomainParticipant(0)
    subscriber = participant.create_subscriber()
    topic = participant.create_topic("RouterState", dds.String)
    reader = subscriber.create_datareader(topic)

    while True:
        # Read data from DDS
        data = reader.read()
        if data:
            router_data = eval(data[0])  # Assuming data comes as a string dict
            router_states[router_data['router_id']] = router_data

@app.route('/')
def dashboard():
    # Find the router with the minimum load
    min_load_router = min(router_states.items(), key=lambda x: x[1]['load'])[0] if router_states else None
    return render_template('dashboard.html', router_states=router_states, min_load_router=min_load_router)

if __name__ == "__main__":
    # Start DDS subscriber in a separate thread
    threading.Thread(target=subscribe_to_router_states).start()

    # Start Flask web server
    app.run(host='0.0.0.0', port=5000)
