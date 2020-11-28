from collections import defaultdict, OrderedDict

def get_header_percentages(headers, total_websites):
    headers = defaultdict(str, headers)
    header_percentages = defaultdict(str)
    for key in headers.keys():
        header_percentages[key] = f"{float((headers[key] / total_websites) * 100)}%"

    return sorted(header_percentages.items(), key = lambda kv:(kv[1], kv[0]), reverse = True)

def get_top_ten_headers(headers):
    filtered_headers = list(filter(None, headers)) 
    
    header_count = defaultdict(int)
    for website_headers in filtered_headers:
        for header in website_headers.items():
            header_count[header] += 1
    
    return sorted(header_count.items(), key = lambda kv:(kv[1], kv[0]), reverse = True)[:10]

