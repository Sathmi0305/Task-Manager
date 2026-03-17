import pytest
from httpx import AsyncClient, ASGITransport
from app.main import app
 
# This test checks that creating a task works
@pytest.mark.asyncio
async def test_create_task():
    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url='http://test'
    ) as client:
        response = await client.post(
            '/tasks/',
            json={'title': 'Buy milk'}
        )
 
    # Check the response is correct
    assert response.status_code == 201           # 201 means 'created'
    assert response.json()['title'] == 'Buy milk'
    assert response.json()['status'] == 'todo'
 
# This test checks that listing tasks works
@pytest.mark.asyncio
async def test_list_tasks():
    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url='http://test'
    ) as client:
        response = await client.get('/tasks/')
 
    assert response.status_code == 200           
