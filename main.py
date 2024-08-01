from fastapi import FastAPI, Request
import uvicorn

app = FastAPI()

@app.post("/sbwebhook")
async def handle_sendbird_webhook(request: Request):
    payload = await request.json()
    if payload.get('category') == 'group_channel:message_send':
        print(f"Received Sendbird webhook payload: {payload}")
    return {"status": "ok"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)