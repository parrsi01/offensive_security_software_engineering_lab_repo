# Lab07: Packet Analysis (tcpdump Header Review)

Author: Simon Parris  
Generated: 2026-02-24

## Concept Overview
This lab captures or reviews local loopback traffic and analyzes packet headers using `tcpdump` output. The focus is protocol identification and understanding what metadata is exposed even without decrypting payloads.

## Threat Model
- Asset: network metadata confidentiality and operational visibility
- Attacker capability: passive observation in a local or authorized network segment
- Unsafe condition: unencrypted or overly verbose traffic patterns
- Impact: traffic analysis, service fingerprinting, workflow disclosure
- Training scope: loopback traffic and offline sample output only

## Step-by-Step CLI Instructions
```bash
cd labs/lab07_packet_analysis
bash capture_loopback.sh
python3 analyze_headers.py
```

## VS Code Workflow Instructions
1. Open `sample_tcpdump.txt` and `analyze_headers.py`.
2. Run the analyzer script and compare counts to the sample lines.
3. If `tcpdump` is installed, run `capture_loopback.sh` and inspect the generated pcap path.

## Expected Output
- Analyzer prints counts for `ICMP` and `TCP` lines in the sample capture.
- Capture script saves a loopback pcap when `tcpdump` and `ping` are available.

## Common Debugging Errors
- `tcpdump not installed`: install `tcpdump` or use offline sample.
- `Permission denied` on capture: run in an Ubuntu VM where your user has packet-capture permissions.
- No packets captured: verify loopback traffic generation and interface name.

## Secure Rewrite
Operational hardening focus:
- prefer encrypted protocols
- reduce sensitive metadata in URLs and headers
- segment traffic and monitor exposure points
- minimize debug traffic in production environments

## Security Implications
Packet headers alone often reveal protocols, ports, and timing patterns that support reconnaissance and incident investigations.

## Professional Skill Alignment
- Security Analyst / Reverse Engineering Analyst: packet header interpretation
- Security Software Engineer: protocol hygiene and telemetry design awareness
