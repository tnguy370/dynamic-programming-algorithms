# Dynamic Programming Algorithms – Milestone 2

This repository contains implementations and analysis of dynamic programming algorithms
for solving an optimization problem involving arranging paintings on display platforms
to minimize total height.

This project was completed as **Milestone 2** for an Algorithm Abstraction & Design course.

---

## Problem Overview
Given a sequence of paintings with fixed order, each having a width and height, and a
maximum platform width **W**, the goal is to assign paintings to platforms such that:
- The total width on each platform does not exceed **W**
- The height of a platform is the maximum height of paintings placed on it
- The total height across all platforms is minimized

---

## Implemented Algorithms
- **Program 3:** Naive exponential-time algorithm for the general problem
- **Program 4:** Dynamic programming solution with higher polynomial complexity
- **Program 5A:** Top-down dynamic programming with memoization
- **Program 5B:** Bottom-up dynamic programming implementation

---

## Files
- `program3.py` – Naive algorithm implementation  
- `program4.py` – Dynamic programming solution  
- `program5A.py` – Top-down DP with memoization  
- `program5B.py` – Bottom-up DP solution  
- `report.pdf` – Algorithm design, analysis, and experimental results  

---

## How to Run
Requirements:
- Python 3.x

Run any program directly, for example:
```bash
python program5B.py
