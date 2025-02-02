import cohere

cohere_client = cohere.Client('GQI8PTe9h9Ii22MbiVXcht0szYcJC8WQSCfCxJw')  # Replace with your API key

try:
    models = cohere_client.list_models()
    print("Available models:")
    for model in models:
        print(model.name)
except Exception as e:
    print(f"Error fetching models: {e}")
