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
