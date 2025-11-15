import socket  
from flask_cors import CORS
from flask import Flask, request, jsonify
def scan_ports(target,ports):
      results=[]
      for port in ports:
            sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            sock.settimeout(2)
            result=sock.connect_ex((target,port))
            if result==0:
                  try:
                        sock.sendall(b"GET / HTTP/1.0\r\n\r\n")
                        banner=sock.recv(1024).decode().strip()
                        if banner=="":
                               banner="Open (no banner returned)"                 
                  except: 
                        banner="Open(no banner returned)"
                  results.append({"port":port,"status":"OPEN","banner":banner})
            else:
                  results.append({"port":port,"status":"CLOSED","banner":"None"})
            sock.close()
      return results            

app=Flask(__name__)
CORS(app)

@app.route('/scan', methods=['POST'])
def scan_endpoint():
    data = request.json
    target = data.get("target")
    ports = data.get("ports", [21, 22, 80, 443, 8080])
    results = scan_ports(target, ports)
    return jsonify({"target": target, "results": results})

if __name__ == '__main__':
    app.run(debug=True)

