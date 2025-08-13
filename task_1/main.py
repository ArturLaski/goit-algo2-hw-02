from typing import List, Dict
from dataclasses import dataclass


@dataclass
class PrintJob:
    id: str
    volume: float
    priority: int
    print_time: int


@dataclass
class PrinterConstraints:
    max_volume: float
    max_items: int


def optimize_printing(print_jobs: List[Dict], constraints: Dict) -> Dict:

    # Tworzymy obiekty z listy słowników
    print_jobs_objects = [PrintJob(**job) for job in print_jobs]
    printer_constraints = PrinterConstraints(**constraints)

    # Sortowanie po priorytecie (mniejsza liczba = wyższy priorytet)
    print_jobs_objects.sort(key=lambda x: x.priority)

    print_order = []
    total_time = 0
    current_group_volume = 0
    current_group_items = 0
    current_group_max_time = 0

    for job in print_jobs_objects:
        if (current_group_volume + job.volume <= printer_constraints.max_volume and
                current_group_items < printer_constraints.max_items):
            print_order.append(job.id)
            current_group_volume += job.volume
            current_group_items += 1
            current_group_max_time = max(current_group_max_time, job.print_time)
        else:
            total_time += current_group_max_time
            current_group_volume = job.volume
            current_group_items = 1
            current_group_max_time = job.print_time
            print_order.append(job.id)

    total_time += current_group_max_time

    return {
        "print_order": print_order,
        "total_time": total_time
    }


def test_printing_optimization():

    test1_jobs = [
        {"id": "M1", "volume": 100, "priority": 1, "print_time": 120},
        {"id": "M2", "volume": 150, "priority": 1, "print_time": 90},
        {"id": "M3", "volume": 120, "priority": 1, "print_time": 150}
    ]

    test2_jobs = [
        {"id": "M1", "volume": 100, "priority": 2, "print_time": 120},
        {"id": "M2", "volume": 150, "priority": 1, "print_time": 90},
        {"id": "M3", "volume": 120, "priority": 3, "print_time": 150}
    ]

    test3_jobs = [
        {"id": "M1", "volume": 250, "priority": 1, "print_time": 180},
        {"id": "M2", "volume": 200, "priority": 1, "print_time": 150},
        {"id": "M3", "volume": 180, "priority": 2, "print_time": 120}
    ]

    constraints = {
        "max_volume": 300,
        "max_items": 2
    }

    print("Test 1 (ten sam priorytet):")
    result1 = optimize_printing(test1_jobs, constraints)
    print(f"Kolejność druku: {result1['print_order']}")
    print(f"Całkowity czas: {result1['total_time']} minut")

    print("\nTest 2 (różne priorytety):")
    result2 = optimize_printing(test2_jobs, constraints)
    print(f"Kolejność druku: {result2['print_order']}")
    print(f"Całkowity czas: {result2['total_time']} minut")

    print("\nTest 3 (przekroczenie ograniczeń):")
    result3 = optimize_printing(test3_jobs, constraints)
    print(f"Kolejność druku: {result3['print_order']}")
    print(f"Całkowity czas: {result3['total_time']} minut")


if __name__ == "__main__":
    test_printing_optimization()
