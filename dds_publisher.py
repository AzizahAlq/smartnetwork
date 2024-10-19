import psutil
import time
import dds  # This assumes the Python bindings for OpenDDS are installed

# Assuming you've set up OpenDDS properly
def publish_router_state(router_id):
    # Initialize DDS domain participant, publisher, and topic
    participant = dds.DomainParticipant(0)
    publisher = participant.create_publisher()
    topic = participant.create_topic("RouterState", dds.String)
    writer = publisher.create_datawriter(topic)

    while True:
        # Get system metrics
        memory = psutil.virtual_memory().percent
        cpu = psutil.cpu_percent(interval=1)
        battery = psutil.sensors_battery().percent if psutil.sensors_battery() else None
        load = sum(psutil.getloadavg()) / len(psutil.getloadavg())

        # Format data to be sent
        data = {
            'router_id': router_id,
            'memory': memory,
            'cpu': cpu,
            'battery': battery,
            'load': load
        }

        # Publish data
        writer.write(str(data))

        # Publish at regular intervals
        time.sleep(5)

if __name__ == "__main__":
    router_id = "router1"  # Change this for each router
    publish_router_state(router_id)
