from flask import Flask, jsonify, request
import grpc
import greeter_pb2
import greeter_pb2_grpc

app = Flask(__name__)

@app.route('/greet', methods=['GET'])
def greet():
    name = request.args.get('name', 'World')
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = greeter_pb2_grpc.GreeterStub(channel)
        response = stub.SayHello(greeter_pb2.HelloRequest(name=name))
    return jsonify(message=response.message)

if __name__ == '__main__':
    app.run(debug=True)
