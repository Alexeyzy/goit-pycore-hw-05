
import sys
import re

from pathlib import Path
from collections import Counter
from collections import defaultdict


def parse_log_line(line: str) -> dict:
    pattern = r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w+) (\w.+)"
    match = re.match(pattern, line)
    return match.groups()


def load_logs(file_path: str) -> list :   
    logs = []
    try:
        with open(file_path, 'r', encoding="UTF-8") as file:  
            for line in file:
                log_data = parse_log_line(line.strip())
                if log_data:
                    logs.append(log_data)
            
    except FileNotFoundError:
        print(f"Файл {file_path} не знайден.")
    except Exception as e:
        print(f"Помілка файлу: {e}")    
    return logs

def filter_logs_by_level(logs: list, level: str) -> list:
    d = defaultdict(list)
    new_logs = list(filter(lambda log: log[1] == level.upper(), logs))
    for log in new_logs:
        d[log[0]]=log[2]
    return dict(d)
    

def count_logs_by_level(logs: list) -> dict:
    level_list = [log[1] for log in logs]
    Counter(level_list)
    return dict(Counter(level_list))


def display_log_counts(counts: dict):
    for level, count in counts.items():
        print(f"{level}: {count}")

if __name__ == "__main__":
    
    if len(sys.argv) < 2:
        print("Не вказан файл")
        sys.exit(1)
 
    file_path = sys.argv[1]
    logs = load_logs(Path(__file__).parent/file_path)
    
    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    if len(sys.argv) == 3:
        level = sys.argv[2]
        logs = filter_logs_by_level(logs, level)      
        display_log_counts(logs)


