# Chapter 3 — _(Chapter Title)_

Code samples referenced in Chapter 3 of *Answer Engine Optimization* (O'Reilly).

## Contents

| File | Listing # in book | Description |
|---|---|---|
| [`python/script-3-1-llm-bot-logs.py`](python/script-3-1-llm-bot-logs.py) | Script 3.1 | Parses Apache/Nginx access logs and reports LLM crawler activity (GPTBot, PerplexityBot, ClaudeBot, etc.) — requests, unique URLs, status codes, peak hour |

## Running

```bash
cd python
# Place your access.log file in the same directory, then:
python script-3-1-llm-bot-logs.py
```

## Notes

- `script-3-1-llm-bot-logs.py` expects a log file named `access.log` in the working directory in **Common Log Format** with the combined `"referer" "user-agent"` suffix (the default for Apache `combined` and Nginx `$http_referer $http_user_agent`).
