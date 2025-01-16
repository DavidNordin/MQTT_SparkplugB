from sparkplug_b import sparkplug_b_pb2

def on_message(client, userdata, msg):
    payload = sparkplug_b_pb2.Payload()
    payload.ParseFromString(msg.payload)
    print("Received Sparkplug Payload:", payload)

client.on_message = on_message
