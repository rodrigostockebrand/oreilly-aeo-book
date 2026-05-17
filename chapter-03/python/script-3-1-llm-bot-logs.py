"""
Script 3.1 — LLM Bot Log Analyzer

Parses an Apache/Nginx common-log-format access log and reports on traffic
from known LLM crawlers (GPTBot, PerplexityBot, ClaudeBot, etc.):
    - Total requests per bot
    - Unique URLs crawled
    - HTTP status code distribution
    - Peak crawl hour of the day

Usage:
    Place an `access.log` file in the same directory and run:
        python script-3-1-llm-bot-logs.py

Companion code for "Answer Engine Optimization" (O'Reilly) — Chapter 3.
"""

import re
from collections import defaultdict
from datetime import datetime

# Parse common log format
LOG_PATTERN = re.compile(
    r'(?P<ip>\S+) \S+ \S+ \[(?P<date>[^\]]+)\] '
    r'"(?P<method>\S+) (?P<url>\S+) \S+" (?P<status>\d+) '
    r'(?P<size>\S+) "[^"]*" "(?P<ua>[^"]*)"'
)

# Bot user-agent strings to monitor
LLM_BOTS = {
    'GPTBot': 'OpenAI',
    'ChatGPT-User': 'OpenAI',
    'OAI-SearchBot': 'OpenAI',
    'Google-Extended': 'Google',
    'PerplexityBot': 'Perplexity',
    'ClaudeBot': 'Anthropic',
    'Claude-Web': 'Anthropic',
    'Bytespider': 'ByteDance',
}

stats = defaultdict(lambda: {
    'requests': 0,
    'urls': set(),
    'status_codes': defaultdict(int),
    'hours': defaultdict(int),
})

with open('access.log', 'r') as f:
    for line in f:
        match = LOG_PATTERN.match(line)
        if not match:
            continue
        ua = match.group('ua')
        for bot_name, label in LLM_BOTS.items():
            if bot_name.lower() in ua.lower():
                s = stats[label]
                s['requests'] += 1
                s['urls'].add(match.group('url'))
                s['status_codes'][match.group('status')] += 1
                try:
                    dt = datetime.strptime(
                        match.group('date').split()[0],
                        '%d/%b/%Y:%H:%M:%S',
                    )
                    s['hours'][dt.hour] += 1
                except ValueError:
                    pass
                break

# Generate report
for bot, s in sorted(stats.items(), key=lambda x: -x[1]['requests']):
    print(f"\n{'='*50}")
    print(f"{bot}")
    print(f"  Total Requests: {s['requests']}")
    print(f"  Unique URLs: {len(s['urls'])}")
    print(f"  Status Codes: {dict(s['status_codes'])}")
    peak_hour = max(s['hours'], key=s['hours'].get) if s['hours'] else 'N/A'
    print(f"  Peak Crawl Hour: {peak_hour}:00")
