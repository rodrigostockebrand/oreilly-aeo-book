# Chapter 3 — _(Chapter Title)_

Code samples referenced in Chapter 3 of *Answer Engine Optimization* (O'Reilly).

## Contents

| File | Listing # in book | Description |
|---|---|---|
| [`python/script-3-1-llm-bot-logs.py`](python/script-3-1-llm-bot-logs.py) | Script 3.1 | Parses Apache/Nginx access logs and reports LLM crawler activity (GPTBot, PerplexityBot, ClaudeBot, etc.) — requests, unique URLs, status codes, peak hour |
| [`data/script-3-1-sample-output.txt`](data/script-3-1-sample-output.txt) | Example output for Script 3.1 | Sample of the report Script 3.1 prints when run against a real access log |
| [`robots/script-3-2-citation-first-robots.txt`](robots/script-3-2-citation-first-robots.txt) | Script 3.2 | Citation-First `robots.txt` — allows real-time retrieval bots and traditional search engines, blocks training-only crawlers |
| [`nginx/script-3-3-llm-bot-rate-limit.conf`](nginx/script-3-3-llm-bot-rate-limit.conf) | Script 3.3 | Nginx rate-limit config — throttles training-only bots, gives real-time retrieval bots generous limits |
| [`tables/schema-types-aeo-impact.md`](tables/schema-types-aeo-impact.md) | Reference table | Schema types and their AEO impact — full version of the abbreviated table in the chapter |
| [`json-ld/script-3-4-organization.json`](json-ld/script-3-4-organization.json) | Script 3.4 | JSON-LD `Organization` schema example with `sameAs` entity-linking to Wikipedia, Wikidata, and social profiles |
| [`json-ld/script-3-5-article.json`](json-ld/script-3-5-article.json) | Script 3.5 | JSON-LD `Article` schema with embedded `Person` (author) and `Organization` (publisher), including `knowsAbout` expertise signals |
| [`json-ld/script-3-6-breadcrumblist.json`](json-ld/script-3-6-breadcrumblist.json) | Script 3.6 | JSON-LD `BreadcrumbList` schema — signals topical hierarchy across Home → Guides → Article |
| [`json-ld/script-3-7-graph-connected-entities.json`](json-ld/script-3-7-graph-connected-entities.json) | Script 3.7 | JSON-LD `@graph` connecting `WebPage`, `Article`, `Person`, and `Organization` via `@id` references — the entity-linking pattern AI retrieval systems use to build knowledge graphs |
| [`json-ld/script-3-8-article-faqpage-hybrid.json`](json-ld/script-3-8-article-faqpage-hybrid.json) | Script 3.8 | JSON-LD hybrid `Article` + `FAQPage` with embedded `Question`/`Answer` pair — dual-typing pattern for retrievable Q&A within an article |
| [`json-ld/script-3-9-howto-robots-txt.json`](json-ld/script-3-9-howto-robots-txt.json) | Script 3.9 | JSON-LD `HowTo` schema with four `HowToStep` items — structures a robots.txt setup tutorial into discrete, retrievable steps for RAG systems |

## Running

```bash
cd python
# Place your access.log file in the same directory, then:
python script-3-1-llm-bot-logs.py
```

## Notes

- `script-3-1-llm-bot-logs.py` expects a log file named `access.log` in the working directory in **Common Log Format** with the combined `"referer" "user-agent"` suffix (the default for Apache `combined` and Nginx `$http_referer $http_user_agent`).
