# AEO Implementation Checklist

Companion reference for *Answer Engine Optimization* (O'Reilly) — Chapter 3.

This is the full version of the abbreviated checklist in the book, covering every action item across the five implementation categories — Crawler Management, Structured Data, Site Architecture, Indexing, and AI Protocols — along with each item's priority.

| Category | Action Item | Priority |
|---|---|---|
| **Crawler Management** | Verify LLM bot identity via reverse DNS for new bot types | High |
| **Crawler Management** | Set up weekly automated log analysis for LLM crawlers | High |
| **Crawler Management** | Implement robots.txt directives for each bot category | High |
| **Crawler Management** | Choose and document your crawl access strategy (Citation-First, Full Open, Selective, or Lockdown) | High |
| **Crawler Management** | Configure rate limiting to prioritize real-time retrieval bots over training bots | Medium |
| **Crawler Management** | Add `Crawl-delay` directives for training-only bots | Medium |
| **Crawler Management** | Block low-value crawl targets (faceted nav, session IDs, tag archives, print versions) | Medium |
| **Crawler Management** | Set up server performance alerts at 500ms TTFB threshold | Medium |
| **Structured Data** | Implement `Organization` schema with `sameAs` links to knowledge base entries | High |
| **Structured Data** | Add `Article` + `Person` schema on all authored content with author `sameAs` links | High |
| **Structured Data** | Implement `BreadcrumbList` schema sitewide | High |
| **Structured Data** | Use the `@graph` pattern to create connected entity markup rather than isolated blocks | High |
| **Structured Data** | Add `FAQPage` schema to informational content pages | High |
| **Structured Data** | Add `HowTo` schema to any step-by-step instructional content | Medium |
| **Structured Data** | Validate all schema with Google's Rich Results Test and Schema.org validator | High |
| **Structured Data** | Make `sameAs` links bidirectional wherever possible | Medium |
| **Site Architecture** | Audit for JavaScript rendering issues using `curl` simulation | High |
| **Site Architecture** | Implement SSR, SSG, pre-rendering, or dynamic rendering for content pages | High |
| **Site Architecture** | Consolidate paginated long-form content onto single URLs with "View All" canonicals | High |
| **Site Architecture** | Audit canonical tag implementation for HTTP/HTTPS, www/non-www, trailing slashes, and parameters (and confirm canonicals live in the `<head>`) | High |
| **Site Architecture** | Implement hub-and-spoke internal linking architecture | Medium |
| **Site Architecture** | Use descriptive, hierarchical URL structures (`domain/category/topic`) | Medium |
| **Site Architecture** | Ensure syndicated content includes canonical tags pointing back to your original | High |
| **Indexing** | Submit and validate XML sitemaps with accurate, meaningful `lastmod` dates | High |
| **Indexing** | Implement IndexNow with automated submission on publish/update | Medium |
| **Indexing** | Set consistent freshness signals across `Article` schema `dateModified`, HTTP `Last-Modified` headers, and visible "Last Updated" dates | High |
| **Indexing** | Create and maintain RSS/Atom feeds advertised in page `<head>` | Low-Medium |
| **Indexing** | Cross-reference crawl patterns with server performance data to identify conflict windows | Medium |
| **AI Protocols** | Create an `llms.txt` file at your site root | Medium |
| **AI Protocols** | Document your AI content policy in human-readable terms of service | Medium |
| **AI Protocols** | Implement TDM Reservation meta tag or HTTP header if you're reserving training rights | Low |
| **AI Protocols** | Monitor evolving platform opt-in/opt-out policies quarterly | Ongoing |
