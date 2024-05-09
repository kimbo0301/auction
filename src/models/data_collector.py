import aiohttp
import asyncio
from bs4 import BeautifulSoup

async def fetch_page(session, url):
    try:
        async with session.get(url, timeout=10) as response:  # 타임아웃 설정
            return await response.text()
    except asyncio.TimeoutError:
        print(f"Timeout occurred while fetching {url}")
        return None

async def fetch_details(session, url):
    html = await fetch_page(session, url)
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        # 데이터 추출 로직 구현
        return {
            'details': 'Details extracted here'
        }
    return {}

async def fetch_products(session, product_name, base_url):
    search_url = f"{base_url}?keyword={product_name.replace(' ', '%20')}"
    html = await fetch_page(session, search_url)
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        product_links = [link['href'] for link in soup.find_all('a', class_='product-link')]
        details_tasks = [fetch_details(session, link) for link in product_links]
        return await asyncio.gather(*details_tasks)
    return []

async def main():
    async with aiohttp.ClientSession() as session:
        product_name = "iPhone 13"
        base_url = "https://example.com/search"
        results = await fetch_products(session, product_name, base_url)
        print(results)

if __name__ == "__main__":
    asyncio.run(main())