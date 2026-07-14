# 📝 Task Tracker CLI

A simple command-line task tracker built with **Python**. This project allows you to manage your daily tasks directly from the terminal using a JSON file for persistent storage.

This project is part of the **roadmap.sh Backend Projects** collection.

**Project URL:** https://roadmap.sh/projects/task-tracker

---

## ✨ Features

* Add new tasks
* Update existing tasks
* Delete tasks
* Mark tasks as **In Progress**
* Mark tasks as **Done**
* List all tasks
* Filter tasks by status
* Persistent storage using `tasks.json`
* No external libraries required

---

## 📂 Project Structure

```text
task-tracker-cli/
│
├── app.py          # CLI entry point
├── main.py         # Task management logic
├── tasks.json      # Stores all tasks
└── README.md
```

---

## 🚀 Getting Started

### Clone the repository

```bash
git clone https://github.com/yidextech/backend-projects/edit/main/01-Task_Tracker
cd 01-Task_Tracker
```
---

## Requirements

* Python 3.10 or newer (recommended)

Check your Python version:

```bash
python --version
```

or

```bash
python3 --version
```

---

## Usage

Since this project has not yet been packaged as an installable CLI application, all commands are executed through Python.

### Add a task

```bash
python app.py add "Buy groceries"
```

or

```bash
python3 app.py add "Buy groceries"
```

---

### Update a task

```bash
python app.py update 1 "Buy groceries and cook dinner"
```

---

### Delete a task

```bash
python app.py delete 1
```

---

### Mark a task as In Progress

```bash
python app.py mark-in-progress 1
```

---

### Mark a task as Done

```bash
python app.py mark-done 1
```

---

### List all tasks

```bash
python app.py list
```

---

### List tasks by status

```bash
python app.py list done
```

```bash
python app.py list todo
```

```bash
python app.py list in-progress
```

---

## 💾 Data Storage

All tasks are stored inside the `tasks.json` file.

Each task contains:

* ID
* Description
* Status
* Created Timestamp
* Updated Timestamp

Example:

```json
[
  {
    "id": 1,
    "description": "Buy groceries",
    "status": "todo",
    "created-at": "2026-07-14 18:30:10",
    "updated-at": "2026-07-14 18:30:10"
  }
]
```

---

## 📌 Future Improvements

Some features planned for future versions include:

* Installable CLI command (`task-cli`) instead of `python app.py`
* Interactive terminal mode
* Better input validation
* Colored terminal output
* Due dates
* Task priorities
* Search functionality
* Unit tests

---

## 🛠 Built With

* Python
* JSON
* Command Line Interface (CLI)

---

## 📖 Learning Objectives

This project was built to practice:

* Python functions
* File handling
* JSON manipulation
* Command-line arguments (`sys.argv`)
* Pattern matching (`match/case`)
* CRUD operations
* Basic software design

---

## 🙏 Acknowledgements

Project idea from **roadmap.sh**:

https://roadmap.sh/projects/task-tracker

---

## 📄 License

This project is open source and available under the MIT License.
