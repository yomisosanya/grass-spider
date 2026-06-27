
import asyncio
from playwright.async_api import async_playwright, expect, Playwright, BrowserType, Response, \
    Locator, Page
from typing import Optional, List

site = 'https://scholar.google.com/'

query = 'cuny graduate center'

async def main():

    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=True)
        context = await browser.new_context(
            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            viewport={'width': 1280, 'height': 720},
        )
        page: Page = await context.new_page()
        response: Optional[Response] = await page.goto(site)

        if response:
            input_locator = page.locator('input[name="q"]')
            await input_locator.fill(query)
            await input_locator.press('Enter')
            await page.wait_for_load_state('load')
        
            await page.screenshot(path='/app/spider-app/debug.png')
            # await asyncio.sleep(0)

            # async with page.expect_response('**/scholar**') as response_info:
            #     await page.locator('#gs_hdr_tsb').click()
            #     # await page.keyboard.press('Enter')
            #     await asyncio.sleep(0)

            # await page.wait_for_load_state('domcontentloaded')
            # ptr: Locator = page.locator('div#gs_bdy').locator('div.gs_r')
            # await ptr.wait_for(state='attached')

            # results
            # ptr = page.locator('div#gs_top').locator('div#gs_bdy').locator('div#gs_bdy_ccl')
            # ptr =  ptr.locator('div#gs_res_ccl').locator('div.gs_r')
            # await ptr.wait_for(state='attached')

            ptr = page.locator('div#gs_bdy').locator('div.gs_r')
            await ptr.first.wait_for(state='attached', timeout=60000)
            results: List[Locator] = await ptr.all()

            print(f'{len(results)} items returned\n')
            for result in results:
                txt = await result.inner_html()
                print(txt)
        else:
            print(f'Failure: call to {site} returned None')
        
        await browser.close()


if __name__ == '__main__':
    asyncio.run(main())

