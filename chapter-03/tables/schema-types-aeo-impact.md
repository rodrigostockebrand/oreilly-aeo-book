# Schema Types and Their AEO Impact

Companion reference for *Answer Engine Optimization* (O'Reilly) — Chapter 3.

This table expands on the abbreviated version in the book, covering each schema type's impact on Answer Engine Optimization, why it matters for AI-cited content, and where to prioritize implementation.

| Schema Type | AEO Impact | Why It Matters | Implementation Priority |
|---|---|---|---|
| **Organization** | High | Establishes entity identity for knowledge graph matching. Appears on 25% of ChatGPT-cited pages and 34% of AI Mode-cited pages. | Essential for all sites |
| **Article / NewsArticle** | High | Signals content type, author, publication date, and last modified date. Second most common schema on AI-cited pages (20% ChatGPT, 26% AI Mode). | Essential for publishers |
| **Person** | High | Links authors to expertise, credentials, and other entities within Article markup, supporting authorship trust signals in a machine-readable form. | Essential for expert-led content |
| **BreadcrumbList** | Medium-High | Signals topical hierarchy and content relationships. Third most common schema on AI-cited pages (15% ChatGPT, 20% AI Mode). | Important for all sites, essential for large sites |
| **FAQPage** | Medium-High | Provides pre-structured question-answer pairs that align with how users query answer engines. Google restricted FAQ rich results in 2023, but AI retrieval systems still use the markup. | Essential for informational content |
| **HowTo** | Medium-High | Structures step-by-step content into discrete, retrievable units. Google deprecated HowTo rich results in 2023, but the structured format still aids machine parsing for RAG retrieval. | Important for instructional content |
| **Product** | Medium-High | Provides structured product attributes for shopping and comparison queries. | Essential for e-commerce |
| **LocalBusiness** | Medium | Connects entities to geographic information for location-based queries. | Important for local businesses |
| **VideoObject** | Medium | Makes video content discoverable with structured metadata and timestamp markup via `Clip` and `SeekToAction`. | Important for video-heavy sites |
| **Review / AggregateRating** | Low-Medium | Provides social proof signals but shows limited presence on AI-cited pages. | Nice to have |
| **SpeakableSpecification** | Low | Currently in beta, restricted to U.S. English content and Google Assistant only. Limited practical adoption for AI retrieval. | Optional |
