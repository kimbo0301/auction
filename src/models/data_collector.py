import aiohttp
import asyncio
from bs4 import BeautifulSoup

async def fetch_page(session, url):
    async with session.get(url) as response:
        return await response.text()

async def fetch_product_details(session, product_url):
    html = await fetch_page(session, product_url)
    soup = BeautifulSoup(html, 'html.parser')
    # 데이터 추출 로직 구현
    return {'name': 'Product Name', 'details': 'Some details'}

async def collect_data(product_name):
    async with aiohttp.ClientSession() as session:
        base_url = f"https://example.com/search/{product_name.replace(' ', '%20')}"
        return await fetch_product_details(session, base_url)