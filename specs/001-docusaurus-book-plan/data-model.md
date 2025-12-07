# Data Model

This document outlines the content structure for the Docusaurus book.

## Entities

### Chapter

- **`title`**: (string) The title of the chapter.
- **`order`**: (integer) The order of the chapter in the book.
- **Relationship**: A `Chapter` has many `Lesson`s.

### Lesson

- **`title`**: (string) The title of the lesson.
- **`content`**: (Markdown) The content of the lesson.
- **`order`**: (integer) The order of the lesson within a chapter.
- **Relationship**: A `Lesson` belongs to a `Chapter`.
