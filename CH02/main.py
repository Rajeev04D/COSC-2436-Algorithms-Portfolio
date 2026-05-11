"""
Lab 2: Main Program
Demonstrates selection sort and array vs linked list.
"""
import json
import time
from sort import selection_sort, python_builtin_sort
from linked_list import LinkedList


def load_cities(filename: str) -> list:
    """Load cities from JSON file."""
    with open(filename, 'r') as file:
        return json.load(file)


def main():
    # Load city data
    cities = load_cities('data/cities.json')
    print(f"Loaded {len(cities)} cities\n")
    
    # Sort by population (ascending)
    print("\nSorting cities by population (smallest first)...")
    sorted_asc = selection_sort(cities, key=lambda x: x['population'])
    print("\nTop 5 smallest cities:")
    for city in sorted_asc[:5]:
        print(f"  {city['name']}: {city['population']:,}")

    # Sort by population (descending)
    print("\nSorting cities by population (largest first)...")
    sorted_desc = selection_sort(cities, key=lambda x: x['population'], reverse=True)
    print("\nTop 5 largest cities:")
    for city in sorted_desc[:5]:
        print(f"  {city['name']}: {city['population']:,}")

    # Compare with Python's built-in sort
    print("\n" + "-" * 40)
    print("Comparison with Python's built-in sort:")
    python_builtin_sort(cities, key=lambda x: x['population'])

if __name__ == "__main__":
    main()
