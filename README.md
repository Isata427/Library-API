# Limkokwing Library Digital System 

## Project Description
[span_1](start_span)This repository contains a basic digital system for the Limkokwing library[span_1](end_span). [span_2](start_span)It simulates a backend API that allows users to search for books and manage borrowing and returning tasks concurrently[span_2](end_span). [span_3](start_span)The project is built using asynchronous Python to handle multiple users at once[span_3](end_span).

## Features
* **[span_4](start_span)Search System**: Search for books by title or category[span_4](end_span).
* **[span_5](start_span)Borrow/Return**: Simulates borrowing logic with status updates[span_5](end_span).
* **[span_6](start_span)Concurrency**: Implemented with `asyncio` to support multiple simultaneous requests[span_6](end_span).
* **[span_7](start_span)Type Safety**: Uses Python type annotations for all list-based data[span_7](end_span).

## File Structure
* `main.py`: The core Python implementation.
* `README.md`: Project documentation.
* `.gitignore`: Specifies files to be ignored by Git.

## How to Run
1. Ensure you have Python installed.
2. Run the simulation using:
   ```bash
   python main.py