# Specification for the Physical AI Book

This document outlines the structure, content guidelines, and technical requirements for the "Physical AI" book, as derived from the project constitution.

## 1. Book Structure

The book will be organized into chapters, each containing a series of lessons. The initial release will feature one chapter.

### Chapter 1: Foundations of Physical AI

This chapter introduces readers to the fundamental concepts of Physical AI, bridging the gap between software and the physical world.

- **Lesson 1: What is Physical AI?**
  - **Description:** A beginner-friendly introduction to the concept of Physical AI. It will define what it is, explore its history, and highlight its importance in modern technology. The lesson will use real-world examples like smart vacuums and autonomous drones to make the concepts relatable.
  - **Objective:** Readers should be able to define Physical AI and identify three examples of it in the real world.

- **Lesson 2: The Core Components of a Physical AI System**
  - **Description:** This lesson breaks down the essential hardware components of a Physical AI system. It will cover sensors (the "senses"), actuators (the "muscles"), and the control system or "brain" (e.g., a microcontroller or single-board computer).
  - **Objective:** Readers should be able to name and describe the function of the three core components of a Physical AI system.

- **Lesson 3: Your First Physical AI Project: A Simple Line-Following Robot**
  - **Description:** A hands-on tutorial where readers will build a basic line-following robot. This project will integrate the concepts from the previous two lessons in a practical, step-by-step guide. The lesson will include a list of required components, circuit diagrams, and code.
  - **Objective:** Readers should be able to assemble and run a simple line-following robot.

## 2. Content Guidelines and Lesson Format

To maintain a consistent and effective learning experience, every lesson must adhere to the following format and guidelines, reflecting the brand voice (Clear, encouraging, and authoritative).

### Lesson Format

Each lesson should be a standalone markdown file and include the following sections:

1.  **Title:** A clear and descriptive title.
2.  **Introduction:** Briefly state what the lesson covers and what the reader will learn.
3.  **Theoretical Concepts:** Explain the core ideas using simple language and analogies.
4.  **Practical Exercise:** A hands-on activity, tutorial, or set of questions to reinforce the theory. For tutorials, provide clear, numbered steps.
5.  **Summary:** A few bullet points summarizing the key takeaways.
6.  **Next Steps:** A brief preview of the next lesson.

### Content Guidelines

- **Beginner-Friendly:** Assume no prior knowledge of Physical AI. Define all jargon.
- **Hands-On:** Every lesson must have a practical component.
- **Code:** All code snippets must be well-commented and accompanied by an explanation.
- **Visuals:** Use diagrams, images, and schematics to illustrate complex concepts.

## 3. Docusaurus-Specific Requirements

The book will be published as a Docusaurus website. The following structure and conventions must be followed to ensure proper organization and navigation.

### File and Directory Structure

The content will reside in the `docs/` directory (which will need to be created). Each chapter will be a subdirectory, and each lesson will be a markdown file within that chapter's directory.

```
docs/
└───foundations-of-physical-ai/
    ├───_category_.json
    ├───what-is-physical-ai.md
    ├───core-components.md
    └───first-project-line-follower.md
```

### Docusaurus Configuration

- **`_category_.json`:** Each chapter directory must contain a `_category_.json` file to define its appearance in the sidebar. For example, for Chapter 1:

  ```json
  {
    "label": "Foundations of Physical AI",
    "position": 1
  }
  ```

- **Markdown Front Matter:** Each lesson file must include front matter to control its sidebar position and label. For example, for Lesson 1:

  ```yaml
  ---
  sidebar_position: 1
  ---
  ```

This structure will ensure that Docusaurus automatically generates a nested sidebar navigation, making the book easy to browse.
