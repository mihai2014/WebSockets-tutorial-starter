
# Python WebSocket starter tutorial

http asyncron/duplex communication with python and javascript

## server(python)-client(python)

### simple app
client0.py / server0.py
### more complex comm app
client1.py / server1.py

## server(python)-client(browser)

### same more complex app as above
server1.py / index.html + comm.js

- set python virtual environment:
```
python -m venv venv
source venv/bin/activate
pip install websockets
```

- activate it:
```
source venv/bin/activate
```

- launch simple http python server with :
```./http-server.sh ```

- launch websocket server with:
```python server1.py```
