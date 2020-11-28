import logging
import csv
from typing import List       

def read_websites_from_csv(csv_path: str, total_lines_to_process: int) -> List[str]:

    with open(csv_path) as csv_file:

        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        websites = []

        for row in csv_reader:
            if line_count >= total_lines_to_process:
                break
            websites.append(row[1])
            line_count += 1
            
        return websites