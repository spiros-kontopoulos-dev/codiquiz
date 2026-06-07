# Public Documentation Sync Strategy

Codiquiz intentionally has two repositories:

1. A private application repository containing source code, infrastructure files, private operational notes, and full internal implementation history.
2. A public documentation repository containing the portfolio-safe product, architecture, roadmap, diagrams, and demo documentation.

## Rule of thumb

The public repository should explain what the platform is, how the architecture works, what was implemented, and why it is technically interesting.

The public repository should not contain:

- secrets,
- real environment files,
- database dumps/backups,
- private keys,
- personal credentials,
- private server credentials,
- unsafe operational details that are not needed for portfolio review.

## Two-copy workflow

When the private repository documentation changes:

1. Update the private docs first.
2. Copy or adapt the relevant public-safe parts into this repository.
3. Sanitize domains, paths, accounts, secrets, and operational details as needed.
4. Commit the public repository separately.

## Recommended update cadence

Update this public repository when a meaningful milestone is completed, for example:

- Backend Intelligence Layer updates.
- Blueprint/coverage planning changes.
- AI generation or Batch API changes.
- Deployment/security milestones.
- Public preview/demo readiness updates.
- New diagrams or portfolio-facing explanations.
