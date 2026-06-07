# GraphQL Roadmap

GraphQL is planned as a focused future enhancement, not as a full replacement for REST.

## Current API direction

REST remains the main API style for Codiquiz commands and CRUD-style workflows.

REST is a good fit for:

- creating generation plans,
- previewing generation batches,
- approving/rejecting drafts,
- running generation actions,
- admin CRUD screens,
- lifecycle actions,
- worker settings/status endpoints.

## Focused GraphQL read model

GraphQL may be useful later for read-heavy nested data, especially the AI Generation Builder.

The builder needs graph-shaped data:

```text
Technology
  Domain
    Modules
      Eligible question types
      Topics
        Concepts
```

A focused GraphQL query could return exactly the nested shape the frontend needs.

Example direction:

```graphql
query AiGenerationBuilder($technologyId: Int!, $domainId: Int!) {
  aiGenerationBuilder(technologyId: $technologyId, domainId: $domainId) {
    technology { id name slug }
    domain { id name slug }
    modules {
      id
      name
      slug
      eligibleQuestionTypes { id name slug }
      topics {
        id
        name
        slug
        concepts { id name slug }
      }
    }
  }
}
```

## Guardrails

The first GraphQL version should follow strict boundaries:

- Add GraphQL only for nested read models.
- Do not migrate existing REST routes.
- Do not add GraphQL mutations initially.
- Do not duplicate business rules inside GraphQL resolvers.
- Reuse existing backend services for eligibility, validation, and planning rules.
- Measure whether GraphQL actually reduces frontend complexity.

## Standalone GraphQL gateway idea

A separate future portfolio project could expose quiz/question data through a GraphQL gateway.

This gateway could demonstrate:

- GraphQL schemas,
- resolvers,
- nested queries,
- mutations,
- API aggregation,
- GraphQL testing.

The standalone gateway would keep the main Codiquiz ecosystem REST-oriented and operationally simpler.

## Recommended positioning

Codiquiz should be described as:

```text
REST-first for commands and operational workflows, with a focused future GraphQL read model for complex nested admin data.
```

Not:

```text
GraphQL-first platform
```
