# Archive Update Rules

## Update Frequency

| File | Timing | Frequency |
|------|--------|-----------|
| 00_experience_stream | Every learnable event | High |
| 06_evolution_log | Every question / correction / confirmation | High |
| 04_live_state | Situation changes | Medium |
| 01-05 modules | On experience extraction | Medium |
| 07_persona_synthesis | Pattern validation or phase change | Low |
| 05_pattern_index | Similar events ≥3 | Low |

## persona_synthesis Update Rules

This is the file the AI reads directly for execution. It must not be updated too frequently (causes noise) or too rarely (goes stale).

### Must update synthesis when
- New pattern is validated (hypothesis → validated)
- Calibration phase changes (shadow → co-pilot → delegated)
- Delegation boundaries change
- Existing rule is overturned

### Update principles
- Every rule must trace back to an experience ID (EXP-XXX)
- Use imperative voice — tell the AI directly what to do
- Delete overturned rules, preserve change history in evolution_log
- Keep total rule count under 20 (more = not genuinely distilled)

## Anti-Degradation Mechanisms

### Expiry cleanup
- "Validated" patterns not referenced by any experience for 30+ days → mark "under review"
- "Pending" hypotheses with no new evidence for 60+ days → delete

### Conflict resolution
When new experience conflicts with existing pattern:
1. Do not immediately overturn the old pattern. Mark as "conflicted."
2. Record conflict details in evolution_log.
3. If new evidence is more recent and numerous (3+ recent occurrences), update the pattern.
4. If old pattern has substantial historical backing, preserve it but record exceptions.

### Anti-over-cautiousness
- Positive confirmations and corrections are equally important.
- If corrections in evolution_log far outnumber confirmations, proactively lower the decision threshold.
- Goal: AI should act boldly within validated scope, not ask permission for everything.
