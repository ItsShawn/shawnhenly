# Shawn Henly – CS-499 ePortfolio

Welcome to my professional ePortfolio for the CS-499 Computer Science course at Southern New Hampshire University. This repository showcases my enhanced software artifacts, project documentation, and reflections aligned with industry standards and program outcomes.

## Code Review Video

Watch my detailed code review for all three key categories (Software Engineering, Algorithms, and Databases):

➡ [Click here to watch the Code Review on YouTube](https://youtu.be/aB0SDyJuNUE)

This video walks through the original structure of each artifact, highlights code analysis findings, and explains my enhancement plans in detail.

---

## Enhancement One – Software Design and Engineering

**Artifact Title:** `AppointmentService.java`  
**Course Origin:** CS-320: Software Testing, Automation, and Quality Assurance  
**Enhancement Focus:** Interface-driven architecture, error handling, logging, and SOLID design principles

### Overview

The original artifact was a single Java class responsible for managing appointment and contact records using in-memory HashMaps. It included basic methods to create, delete, and retrieve these records, but lacked modularity, validation, and error handling.

### Enhancement Summary

The enhanced version of this class reflects my progression toward professional software development standards. It introduces meaningful improvements such as:

- Refactored logic into two clean interfaces: `IAppointmentService` and `IContactService`
- Introduced `AppointmentException`, a custom runtime exception for better error signaling
- Integrated **SLF4J** with **Logback** for structured logging
- Added null checks and duplicate entry protection for input validation
- Applied **SOLID** principles to improve maintainability and extensibility

### Narrative Document

You can read my full reflection and enhancement narrative here:

[Milestone Two Narrative – Enhancement One](https://github.com/ItsShawn/shawnhenly/blob/main/CS-499%20Milestone%202%20Enhancement%20One/CS-499%20Milestone%20Two.docx)

This document explains why I chose this artifact, how I improved it, and what I learned during the enhancement process.

### Source Code

Compare the original and enhanced versions of the `AppointmentService` class:

- [Original AppointmentService.java](https://github.com/ItsShawn/shawnhenly/blob/main/CS-499%20Milestone%202%20Enhancement%20One/AppointmentService.java)
- [Enhanced AppointmentServiceEnhanced.java](https://github.com/ItsShawn/shawnhenly/blob/main/CS-499%20Milestone%202%20Enhancement%20One/AppointmentServiceEnhanced.java)

---

## Enhancement Two – Algorithms and Data Structures

**Artifact Title:** `qtrain()` Function (Reinforcement Learning Agent)  
**Course Origin:** CS-370: Artificial Intelligence  
**Enhancement Focus:** Modular design, logging, configuration handling, and defensive coding

### Overview
This artifact was originally a monolithic Python function used to train a Deep Q-learning agent. It suffered from code bloat, hardcoded parameters, and no traceability, making it difficult to debug or extend.

### Enhancement Summary
The enhanced version reflects my ability to apply algorithmic principles while improving modularity and maintainability:
- Extracted logic into modular helper functions like `choose_action()` and `log_progress()`
- Integrated Python’s `logging` module for visibility
- Cleaned up the training loop by eliminating global variables
- Added fallback handling for missing `free_cells` and edge cases

### Narrative Document
You can read my full reflection and enhancement narrative here:  
[Milestone Three Narrative – Enhancement Two](https://github.com/ItsShawn/shawnhenly/blob/main/CS-499%20Milestone%203%20Enhancement%20Two/CS-499%20Milestone%20Three.docx)

### Source Code
Compare the original and enhanced versions of the `qtrain()` function:  
- [Original qtrain_artifact.py](https://github.com/ItsShawn/shawnhenly/blob/main/CS-499%20Milestone%203%20Enhancement%20Two/qtrain_artifact.py)  
- [Enhanced qtrain_artifact-enhanced.py](https://github.com/ItsShawn/shawnhenly/blob/main/CS-499%20Milestone%203%20Enhancement%20Two/qtrain_artifact-enhanced.py)

---

## Enhancement Three – Databases

**Artifact Title:** `animal_shelter.py`  
**Course Origin:** CS-340: Advanced Programming Concepts  
**Enhancement Focus:** Secure credential management, logging, error handling, performance optimization

### Overview
This artifact allows MongoDB-based CRUD operations for animal records. Initially, it had hardcoded credentials and no safeguards.

### Enhancement Summary
The updated version transforms the script into a production-ready backend component:
- Environment variables replace hardcoded credentials (via `os.getenv`)
- Logging captures all CRUD operations and failure points
- `try/except` blocks catch MongoDB-related errors
- Indexes added for `breed`, `location`, and `adoption_status`
- Input validation and fallback logic improve robustness

### Narrative Document
You can read my full reflection and enhancement narrative here:  
[Milestone Four Narrative – Enhancement Three](https://github.com/ItsShawn/shawnhenly/blob/main/CS-499%20Milestone%204%20Enhancement%20Three/CS-499%20Milestone%20Four.docx)

### Source Code
Compare the original and enhanced versions of the `animal_shelter.py` module:  
- [Original animal_shelter.py](https://github.com/ItsShawn/shawnhenly/blob/main/CS-499%20Milestone%204%20Enhancement%20Three/animal_shelter.py)  
- [Enhanced animal_shelter-enhanced.py](https://github.com/ItsShawn/shawnhenly/blob/main/CS-499%20Milestone%204%20Enhancement%20Three/animal_shelter-enhanced.py)

---
