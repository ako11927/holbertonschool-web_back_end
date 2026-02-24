# Python - Async Function

This project focuses on asynchronous programming in Python using `asyncio`. It covers creating coroutines, running multiple coroutines concurrently, measuring runtime, and working with `asyncio.Task` objects.

## Learning Objectives
- Understand `async` and `await` syntax
- Execute multiple coroutines concurrently
- Measure the execution time of asynchronous functions
- Create and manage `asyncio.Task` objects

## Requirements
- All files are interpreted/compiled on Ubuntu 20.04 LTS using Python 3.9
- Code follows the `pycodestyle` style (version 2.5.x)
- All functions and coroutines are type-annotated
- Modules and functions have proper documentation (a real sentence explaining purpose)
- All files must be executable

## Files

| File | Description |
|------|-------------|
| `0-basic_async_syntax.py` | Contains `wait_random` – an asynchronous coroutine that waits for a random delay. |
| `1-concurrent_coroutines.py` | Contains `wait_n` – spawns `wait_random` n times and returns sorted delays. |
| `2-measure_runtime.py` | Contains `measure_time` – measures total execution time for `wait_n(n, max_delay)` and returns average time per call. |
| `3-tasks.py` | Contains `task_wait_random` – returns an `asyncio.Task` for the `wait_random` coroutine. |
| `4-tasks.py` | Contains `task_wait_n` – same as `wait_n` but uses `task_wait_random` to create tasks. |

## Usage Examples

### Task 0: Basic async syntax
```bash
$ ./0-main.py
9.034261504534394
1.6216525464615306
10.634589756751769
Task 1: Multiple coroutines
bash
$ ./1-main.py
[0.9693881173832269, 1.0264573845731002, 1.7992690129519855, 3.641373003434587, 4.500011569340617]
Task 2: Measure runtime
bash
$ ./2-main.py
1.759705400466919
Task 3: Create task
bash
$ ./3-main.py
<class '_asyncio.Task'>
Task 4: Tasks from wait_n
bash
$ ./4-main.py
[0.2261658205652346, 1.1942770588220557, 1.8410422186086628, 2.1457353803430523, 4.002505454641153]
