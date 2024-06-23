import httpx

async def test_create_user():
    async with httpx.AsyncClient() as client:
        url = "http://localhost:8000/user/"
        payload = {
            "telegram_id": "lox007",
            "wallet_address": "0xabc...",
            "claimed_code": "claim456"
        }
        response = await client.post(url, params=payload)
        print(response.status_code)
        print(response.json())

import asyncio
asyncio.run(test_create_user())
