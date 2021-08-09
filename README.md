# flask-messaging-api
A nice anonymous message api (Uses Flask's restful api)

## How it works:

### 1. The user send a `put` request to your api server:

Required fields: `newMessage`

Content type: `json`

Ratelimiting: 2 posts / hour
#### Example put request with curl:
```bash
curl -d '{"newMessage": "Hello everyone!"}' -H 'Content-Type: application/json' http://127.0.0.1:5000/api/message
```

The newMessage value will be stored inside the message.txt file.

You will recieve a statuscode 200 if it works

### 2. The next user send a `get` request to your api server

#### Example get request with curl:
```bash
curl http://127.0.0.1:5000/api/message
```

You will recieve the previous message in json format.

Example:

{
  "message": "Hello everyone!"
}
