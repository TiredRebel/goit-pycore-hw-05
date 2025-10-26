import sys
from typing import List, Dict
from collections import Counter

def parse_log_line(line: str) -> Dict:
    """
    Парсить рядок логу та повертає словник з компонентами.
    """
    parts = line.strip().split(' ', 3)
    return {
        'date': parts[0],
        'time': parts[1],
        'level': parts[2],
        'message': parts[3]
    }

def load_logs(file_path: str) -> List[Dict]:
    """
    Завантажує логи з файлу.
    """
    try:
        with open(file_path, 'r') as file:
            return [parse_log_line(line) for line in file]
    except FileNotFoundError:
        print(f"Помилка: Файл '{file_path}' не знайдено.")
        sys.exit(1)
    except Exception as e:
        print(f"Помилка при читанні файлу: {e}")
        sys.exit(1)

def filter_logs_by_level(logs: List[Dict], level: str) -> List[Dict]:
    """
    Фільтрує логи за вказаним рівнем.
    """
    return [log for log in logs if log['level'].lower() == level.lower()]

def count_logs_by_level(logs: List[Dict]) -> Dict[str, int]:
    """
    Підраховує кількість записів для кожного рівня логування.
    """
    return Counter(log['level'] for log in logs)

def display_log_counts(counts: Dict[str, int]):
    """
    Виводить результати підрахунку у вигляді таблиці.
    """
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for level, count in counts.items():
        print(f"{level:<17}| {count}")

def main():
    """
    Головна функція для обробки логів.
    """
    if len(sys.argv) < 2:
        print("Використання: python log_parser.py /path/to/logfile.log [level_logging]")
        sys.exit(1)

    file_path = sys.argv[1]
    logs = load_logs(file_path)
    
    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    if len(sys.argv) > 2:
        level_to_filter = sys.argv[2]
        filtered_logs = filter_logs_by_level(logs, level_to_filter)
        
        print(f"\nДеталі логів для рівня '{level_to_filter.upper()}':")
        for log in filtered_logs:
            print(f"{log['date']} {log['time']} - {log['message']}")

if __name__ == "__main__":
    main()
