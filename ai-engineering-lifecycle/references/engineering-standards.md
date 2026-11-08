# Engineering domain guidance — apply by risk and relevance

This is an evaluation map, not a list of mandatory individual skills. Favor the simplest architecture meeting measured needs; avoid over-scaffolding. Prefer existing project conventions and domain experts.

## Product and application

- **Requirements:** user value, problem statement, personas/journeys where useful, measurable outcomes, functional/nonfunctional requirements, acceptance criteria, MVP boundaries, prioritization, traceability, scope changes.
- **Domain and business rules:** key entities/value objects, invariants, state transitions, transaction boundaries, domain services/events, bounded contexts if complexity merits them; test business invariants.
- **UX and design systems:** existing components and tokens first; interface hierarchy, responsive/mobile behavior, usability, progressive enhancement, accessible errors and visual regression for sensitive UI changes.
- **Accessibility and internationalization:** applicable WCAG, semantics/keyboard/screen readers, contrast/focus/forms, locale-aware formatting, time zones, RTL when needed, translation and fallback policies; test real journeys.

## Architecture, APIs, data

- **Application architecture:** compare modular monolith, monolith, services, event-driven or serverless designs by reliability, developer skill, operations, latency and cost. Horizontal scaling does not require microservices.
- **APIs/integrations:** explicit contracts and versions, error models, authentication, authorization, pagination, idempotency, backoff, timeout, rate limit, webhooks, compatibility/deprecation, contract tests, external service failure cases.
- **Data and databases:** modeling, migrations and rollback/forward compatibility, indexes and plans, transaction boundaries, locking, connection pooling, backup/restore tests, tenancy isolation, PII classification, retention/deletion, lineage and quality.
- **Scaling:** distinguish replicas, containers, servers, zones, regions, read vs. write scalability, caching and invalidation, queues/workers, autoscaling. Measure bottlenecks before sharding or introducing Kubernetes. Use realistic load targets and costs.
- **Infrastructure:** single host/managed PaaS/containers/orchestration chosen based on constraints; network/IAM, least privilege, backups, restore drills, IaC drift, TLS, observability and deployment safety.

## Quality, delivery, operations

- **Tests:** risk-based mix of unit, component, integration, contract, E2E, security, property-based/fuzzing/mutation, accessibility, performance, resilience and recovery; coverage is a signal, not a proof.
- **Delivery:** repeatable builds, dependency pinning, protected branches, safe CI with restricted credentials, release versioning, changelog, rollout checks, feature flags/canaries where justified, database compatibility, rollback and ownership.
- **Reliability/SRE:** SLIs/SLOs/error budgets proportional to criticality, actionable alerts, on-call or support ownership, runbooks, timeouts, bounded retries, degradation, recovery objectives, disaster recovery validation and blameless postmortems.
- **Observability:** useful structured logs, metrics and traces; production-impact context, sampling and retention, privacy-redaction, meaningful p95/p99 latency, error rates, queue depth, database health and spending.
- **Cost/FinOps:** total cost of compute, storage, network, data transfer, managed services, monitoring, CI, paid APIs, AI tokens, retries, evaluation, human time and on-call burden. Compare avoidable idle infrastructure against required availability.
- **Technical debt:** register material debt with cause, risk, owner, effort and business impact; prioritize rather than performing broad untargeted cleanup.

## Governance and ecosystem

- **Privacy/legal:** data minimization, lawful processing, retention/deletion, notices/consent, rights requests, applicable GDPR and other jurisdictional rules; standards like SOC 2/ISO 27001 require organizational evidence, not merely correct code. Never assert compliance or certification without review.
- **Supply chain:** inventory and version direct/transitive dependencies; vuln alerts, integrity, provenance, licensing, container image policies, SBOM if justified, CI credential protection, updates and EOL handling.
- **Multi-project:** separate secrets, tool credentials, source access and memory by project; share generic skills and policies without leaking sensitive code or trust contexts.
- **AI model/provider management:** choose model by measured capability and task risk, latency, availability, privacy, data policies and cost; version/fallback, structured output validation, regression tests. No assumption that any model is always best.
- **Technology adoption:** verify license, maturity, source activity, maintenance, integration, migration path, exit options and a reversible proof of concept; evidence over marketing claims.

## Architecture decision record trigger

Write an ADR for a choice that materially affects service boundaries, permanent data contracts, security posture, operating costs, irreversible migrations, vendor dependence, recovery or deployment patterns. Include context, constraints, alternatives, rationale, trade-offs, status, owner, date and supersession link. Use `assets/adr-template.md` rather than inventing competing formats.
