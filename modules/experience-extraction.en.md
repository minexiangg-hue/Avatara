# Experience Extraction Rules

## Dual Extraction

Every experience extracts in both directions. But not mechanically for every event — weight based on event type:

| Event type | Persona extraction focus | Business extraction focus |
|-----------|------------------------|--------------------------|
| User evaluates work output | Evaluation criteria, weight | Subject's capabilities/weaknesses |
| User interacts with someone | Communication style, tone, strategy | Counterparty characteristics, relationship dynamics |
| User makes a decision | Decision style, priority logic | Decision context, impact, outcome |
| User expresses emotion | Reaction pattern, personality core | Triggering events/causes |
| User corrects AI | Correct behavioral rules | Correct business rules/processes |
| Casual conversation | Word choice habits, thinking patterns | May not apply |

## Persona Layer Extraction Rules

### → 01_core_traits.md (Personality Core)
**Trigger**: New behavior related to personality traits observed.
**Extract**:
- New Big Five evidence (which behaviors support/refute current inference)
- New personality tags (distilled from recurring behaviors)
- New internal drive clues (what triggers proactivity / what triggers resistance)

### → 02_communication_style.md (Communication Style)
**Trigger**: User says something worth recording (especially typical expressions in specific situations).
**Extract**:
- New situation-utterance mapping entries (what they said in what context)
- New word choice habits or avoided expressions
- Communication style variations across different audiences/situations

### → 03_routine_patterns.md (Behavioral Rhythm)
**Trigger**: User's natural rhythm observed (not planned schedule, but unconscious habits).
**Extract**:
- New entries in daily timeline (NOTE: internalized rhythm, NOT a schedule)
- Changes in recent focus areas
- New work habit discoveries

**Critical**: Only record behaviors that the user does unconsciously and would feel "off" if skipped. Occasional habits do not belong here.

### → 04_decision_model.md (Decision Model)
**Trigger**: User makes a judgment or evaluation.
**Extract**:
- New data for decision style spectrum (what style tends to be used in what context)
- New evaluation criteria dimensions or weight adjustments (anchored quantification: definition + weight + case)
- Changes in delegation boundaries

### → 05_reaction_patterns.md (Reaction Patterns)
**Trigger**: User reacts to something (especially non-standard situations).
**Extract**:
- Typical reactions under specific trigger conditions
- New emotion-behavior mapping entries
- Feedback style differences across audiences (subordinates / peers / superiors / external)

## Business Layer Extraction Rules

### → 00_experience_stream.md (Experience Stream)
**This is the first landing point for ALL experiences.** Every experience is written here first, then extracted to other files.

### → 01_team_profile.md (Team Profiles)
**Trigger**: Experience involves someone's capabilities, performance, or characteristics.
**Extract**:
- New task performance records
- Pattern summary updates (reliability, common blockers, optimal assignment strategy)

### → 02_business_rules.md (Business Rules)
**Trigger**: Repeatable operational rules observed.
**Extract**:
- Task assignment rules, approval rules, collaboration workflow rules
- Exception handling approaches

### → 03_client_relations.md (Client Relations)
**Trigger**: Experience involves external partners.
**Extract**:
- Client characteristics, communication preferences, historical interaction records

### → 04_live_state.md (Current Situation)
**Trigger**: Situation changes (new project, new bottleneck, personnel changes).
**Extract**:
- Active project updates, bottleneck changes, pending decisions

### → 05_pattern_index.md (Pattern Index)
**Trigger**: Similar events appear ≥3 times in experience_stream.
**Extract**:
- Create pattern entry, simultaneously noting implications for both persona and business layers
