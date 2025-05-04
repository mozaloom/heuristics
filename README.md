# Heuristics

Python implementations of heuristic algorithms and optimization problems.

## Components

- **Coin Change Algorithms**: 
  - `greedy_coin.py`: Greedy approach for minimum coin problem
  - `coin.py`: Alternative coin change implementation

- **Traveling Salesman Problem**:
  - `fetch_cities_lat_long.py`: CLI tool to calculate shortest path between cities

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Run greedy coin algorithm
./greedy_coin.py 0.99

# Find optimal path between cities
./fetch_cities_lat_long.py cities "New York" "Chicago" "Miami"

# Run simulations
./fetch_cities_lat_long.py simulate --count 10
```

## Testing

```bash
make test
```