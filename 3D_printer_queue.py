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
    """
    Optimizes the 3D printing queue according to priorities and printer constraints

    Args:
        print_jobs: List of print jobs
        constraints: Printer constraints

    Returns:
        Dict with print order and total time
    """

    try:
        if not print_jobs or not constraints:
            raise ValueError("Input data is missing or invalid")

        sorted_jobs_by_priority = sorted(print_jobs, key=lambda x: (x["priority"]))

        max_volume = constraints["max_volume"]
        max_items = constraints["max_items"]

        total_time = 0
        current_volume = 0
        items_processed = 0
        current_groups = []
        print_order_array = []

        for job in sorted_jobs_by_priority:
            if (
                items_processed < max_items
                and current_volume + job["volume"] <= max_volume
            ):
                current_groups.append(job["id"])
                current_volume += job["volume"]
                total_time = max(total_time, job["print_time"])
                items_processed += 1
            else:
                if current_groups:
                    print_order_array.append(current_groups)
                current_groups = [job["id"]]
                current_volume = job["volume"]
                total_time += job["print_time"]
                items_processed = 1

        if current_groups:
            print_order_array.append(current_groups)

        return {
            "print_order": print_order_array,
            "total_time": total_time,
        }

    except (ValueError, KeyError, TypeError) as e:
        print(f"Error processing data: {e}")


# Testing
def test_printing_optimization():
    # Test 1: Models with the same priority
    test1_jobs = [
        {"id": "M1", "volume": 100, "priority": 1, "print_time": 120},
        {"id": "M2", "volume": 150, "priority": 1, "print_time": 90},
        {"id": "M3", "volume": 120, "priority": 1, "print_time": 150},
    ]

    # Test 2: Models with different priorities
    test2_jobs = [
        {"id": "M1", "volume": 100, "priority": 2, "print_time": 120},  # lab work
        {"id": "M2", "volume": 150, "priority": 1, "print_time": 90},  # thesis
        {
            "id": "M3",
            "volume": 120,
            "priority": 3,
            "print_time": 150,
        },  # personal project
    ]

    # Test 3: Exceeding volume constraints
    test3_jobs = [
        {"id": "M1", "volume": 250, "priority": 1, "print_time": 180},
        {"id": "M2", "volume": 200, "priority": 1, "print_time": 150},
        {"id": "M3", "volume": 180, "priority": 2, "print_time": 120},
    ]

    constraints = {"max_volume": 300, "max_items": 2}

    print("Test 1 (same priority):")
    result1 = optimize_printing(test1_jobs, constraints)
    print(f"Print order: {result1['print_order']}")
    print(f"Total time: {result1['total_time']} minutes")

    print("\nTest 2 (different priorities):")
    result2 = optimize_printing(test2_jobs, constraints)
    print(f"Print order: {result2['print_order']}")
    print(f"Total time: {result2['total_time']} minutes")

    print("\nTest 3 (exceeding constraints):")
    result3 = optimize_printing(test3_jobs, constraints)
    print(f"Print order: {result3['print_order']}")
    print(f"Total time: {result3['total_time']} minutes")


if __name__ == "__main__":
    test_printing_optimization()
