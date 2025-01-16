import paho.mqtt.client as mqtt
from sparkplug_b import sparkplug_b_pb2  # Sparkplug Protobuf

# MQTT Broker settings
BROKER = "localhost"
PORT = 1883
TOPIC = "spBv1.0/MyGroup/NBIRTH/MyEdge"

# Create NBIRTH payload
def create_nbirth_payload():
    payload = sparkplug_b_pb2.Payload()
    payload.timestamp = int(time.time() * 1000)

    # Add metrics (e.g., device metrics)
    metric = payload.metrics.add()
    metric.name = "Device Status"
    metric.value.int_value = 1
    metric.datatype = sparkplug_b_pb2.Payload.DataType.INT32

    return payload

# Serialize and publish payload
def publish_nbirth(client):
    payload = create_nbirth_payload()
    serialized_payload = payload.SerializeToString()
    client.publish(TOPIC, serialized_payload)

# Set up MQTT Client
client = mqtt.Client()
client.connect(BROKER, PORT)
publish_nbirth(client)
client.loop_forever()
