# Pagination

This project implements various pagination techniques in Python, focusing on handling large datasets efficiently and robustly. It is part of the Holberton School Web Back-end curriculum.

## Overview

Pagination is essential when dealing with large datasets, allowing clients to retrieve data in manageable chunks. This project demonstrates:

- Simple helper functions for calculating index ranges.
- Basic pagination of a CSV dataset.
- Hypermedia pagination with metadata.
- Deletion‑resilient pagination that gracefully handles missing rows.

## Data Source

The project uses the `Popular_Baby_Names.csv` file, which contains baby name data from the US. The file is expected to be present in the same directory as the Python scripts.

## Tasks

### 0. Simple helper function
**File:** `0-simple_helper_function.py`

Implements `index_range(page, page_size)`, which returns a tuple `(start_index, end_index)` for the given pagination parameters (1‑indexed pages).

```python
>>> index_range(1, 7)
(0, 7)
>>> index_range(3, 15)
(30, 45)
