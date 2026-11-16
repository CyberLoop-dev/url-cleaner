#!/usr/bin/env python3
"""Normalize URL lists and remove common tracking parameters."""
import argparse
from pathlib import Path
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

TRACKING = {"fbclid", "gclid", "mc_cid", "mc_eid", "igshid"}

def clean_url(raw: str) -> str:
    parts = urlsplit(raw.strip())
    if parts.scheme.lower() not in {"http", "https"} or not parts.hostname:
        raise ValueError("Expected an absolute http or https URL.")
    scheme = parts.scheme.lower()
    host = parts.hostname.lower()
    if ":" in host and not host.startswith("["):
        host = f"[{host}]"
    port = parts.port
    if port and not ((scheme == "http" and port == 80) or (scheme == "https" and port == 443)):
        host = f"{host}:{port}"
    query = []
    for key, value in parse_qsl(parts.query, keep_blank_values=True):
        lowered = key.lower()
        if lowered in TRACKING or lowered.startswith("utm_"):
            continue
        query.append((key, value))
    path = parts.path or "/"
    return urlunsplit((scheme, host, path, urlencode(query, doseq=True), parts.fragment))

def clean_lines(lines):
    seen, result = set(), []
    for line in lines:
        raw = line.strip()
        if not raw or raw.startswith("#"):
            continue
        normalized = clean_url(raw)
        if normalized not in seen:
            seen.add(normalized)
            result.append(normalized)
    return result

def main():
    parser = argparse.ArgumentParser(description="Clean and deduplicate a text file of URLs.")
    parser.add_argument("input", type=Path)
    parser.add_argument("--output", type=Path, default=Path("clean-urls.txt"))
    args = parser.parse_args()
    try:
        cleaned = clean_lines(args.input.read_text(encoding="utf-8").splitlines())
    except (OSError, ValueError) as exc:
        parser.error(str(exc))
    args.output.write_text("\n".join(cleaned) + ("\n" if cleaned else ""), encoding="utf-8")
    print(f"Kept {len(cleaned)} unique URL(s): {args.output}")
if __name__ == "__main__":
    main()
