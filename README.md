# flask-grpc-protobuf

A basic "Greeter" example gRPC server using protobuf and Flask to grasp the gist of it.

## Usage

Create a virtual environment, then install the dependencies using `pip` or `pipenv`:

```
pip install grpcio grpcio-tools Flask
```

If not done already, generate gRPC code from the `.proto` file using the gRPC Python tools.

```
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. greeter.proto
```

1. Start the gRPC server: `python grpc_server.py`
2. In another terminal, start the Flask app: `python app.py`
3. Access http://127.0.0.1:5000/greet?name=SpamSpam in your browser or use a tool like curl to send a request.
