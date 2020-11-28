import azure.functions as func
import analyze_websites.website_reader as webreader
import analyze_websites.header_analyzer as analyzer

import aiohttp
import asyncio
import os
import logging
import time
import pprint

from aiohttp import ClientSession

logger = logging.getLogger(__name__)

async def main(req: func.HttpRequest) -> func.HttpResponse:
    start_time = time.perf_counter()

    total_websites = 1000
    if req.params.get('total_websites'):
        total_websites = int(req.params.get('total_websites'))

    websites = webreader.read_websites_from_csv("assets/website_list.csv", total_websites)

    async with ClientSession(connector=aiohttp.TCPConnector(limit=1000, verify_ssl=False)) as session:
        headers = await asyncio.gather(*[__get_website_headers_async(website, session, 30) for website in websites])

    top_ten_headers = analyzer.get_top_ten_headers(headers)
    top_ten_header_percentages = analyzer.get_header_percentages(top_ten_headers, total_websites)

    return func.HttpResponse(f"Took {time.perf_counter() - start_time} seconds." \
                             f"\n\n Top 10 headers:\n {pprint.pformat(top_ten_headers)}" \
                             f"\n\n Percentages of headers used:\n {pprint.pformat(top_ten_header_percentages)}")


async def __get_website_headers_async(website, session, timeout) -> dict:
    url = f"http://{website}"

    try:
        response = await session.request(method='GET', url=url, timeout=timeout)
        response.raise_for_status()
        logger.info(f"Response status ({url}): {response.status}")
        return response.headers
    except aiohttp.ClientError as generalerr:
        logger.info(f"General exception: {generalerr}")
    except asyncio.TimeoutError as timeouterr:
        logger.info(f"Timeout on ({url})")
