import asyncio
from itertools import islice
from playwright import BrowserContext, Page
from pydantic import HttpUrl, TypeAdapter, ValidationError
import settings

url_check = TypeAdapter(HttpUrl)

def create_page(browser: BrowserContext, url: str):
    """Returns a Page immediately in a Task"""
    page_coro = browser.new_page()
    return asyncio.create_task(page_coro)



async def browse(policy: dict, page: Page, verbose: bool=True):
    """
    """
    
    # throws a pydantic.ValidationError if value is malformed
    # extract only a number of sites specified by settings.SITE_COUNT
    url_list = [url_check.validate_python(site) for site in islice(policy['site'], settings.SITE_COUNT)]
     
    async for url in url_list:
        response = await page.goto(url)
        if response.ok:
            break

    match policy['type']:

        case 'form':
            pass

        case _:
            pass
    


    # test cases

    # create_page
    # url_check
    # sample yaml file test
