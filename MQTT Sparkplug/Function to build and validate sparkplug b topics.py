def build_sparkplug_topic(group_id, message_type, edge_node_id, device_id=None):
    """
    Builds and validates a Sparkplug B topic string.

    Parameters:
    - group_id (str): The Sparkplug group identifier (e.g., "MyGroup").
    - message_type (str): The Sparkplug message type (e.g., "NBIRTH", "DBIRTH").
    - edge_node_id (str): The Edge Node identifier (e.g., "MyEdge").
    - device_id (str): The Device identifier (optional, e.g., "MyDevice").

    Returns:
    - str: A validated Sparkplug B topic string.
    - ValueError: If the input parameters are invalid.
    """

    # Define valid Sparkplug message types
    valid_message_types = {
        "NBIRTH", "NDEATH", "DBIRTH", "DDEATH", "DATA", "CMD"
    }

    # Validate inputs
    if not group_id or not isinstance(group_id, str):
        raise ValueError("Group ID must be a non-empty string.")
    if message_type not in valid_message_types:
        raise ValueError(f"Invalid message type: {message_type}. Valid types are: {valid_message_types}")
    if not edge_node_id or not isinstance(edge_node_id, str):
        raise ValueError("Edge Node ID must be a non-empty string.")
    if device_id is not None and not isinstance(device_id, str):
        raise ValueError("Device ID must be a string if provided.")

    # Build the topic
    if device_id:
        topic = f"spBv1.0/{group_id}/{message_type}/{edge_node_id}/{device_id}"
    else:
        topic = f"spBv1.0/{group_id}/{message_type}/{edge_node_id}"

    return topic
