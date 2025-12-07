# Research

## Testing Framework

- **Decision**: Use Jest for testing.
- **Rationale**: Jest is the most popular testing framework for JavaScript and is well-integrated with React, which Docusaurus uses. It's a safe and standard choice.
- **Alternatives considered**: Mocha, Chai. Jest is an all-in-one solution which is simpler to set up.

## Performance Goals

- **Decision**: Target a Lighthouse performance score of 90+ for production builds.
- **Rationale**: This is a good baseline for a modern static website and ensures a good user experience. Docusaurus is already optimized for performance, so this is achievable.
- **Alternatives considered**: No specific performance goal. Setting a goal provides a clear target for optimization efforts.

## Scale and Scope

- **Decision**: The book will start with 5 chapters, each with 3-5 lessons. No interactive elements are planned for the initial version.
- **Rationale**: This provides a clear and manageable scope for the initial development phase. Interactive elements can be added later as a separate feature.
- **Alternatives considered**: A larger or smaller initial scope. This scope is a good balance between providing substantial content and keeping the initial effort manageable.
