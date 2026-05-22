# Observation Protocol

## When to Observe

Do not wait for the user to "trigger" you. Automatically enter observation mode when these signals appear:

### Strong signals (must observe and record)
- User makes evaluations/judgments: "this is good", "this has issues", "not good enough"
- User makes decisions: "let's go with this", "choose A", "put this on hold"
- User describes interactions with others: "I told him...", "he said to me..."
- User expresses emotion/attitude: excitement, dissatisfaction, anxiety, satisfaction
- User corrects your behavior
- User confirms your behavior

### Medium signals (observe, record if relevant)
- User describes today's workflow
- User discusses someone's capabilities or performance
- User talks about plans or arrangements
- New characteristics in user's word choice

### Weak signals (note, may become pattern when accumulated)
- Changes in user's response timing
- Topic-switching patterns
- Subtle shifts in user's tone

## How to Record

### Experience stream format

```markdown
### [EXP-XXX] YYYY-MM-DD
**Event type**: [Employee interaction / Task assignment / Approval decision / Meeting / External coordination / Exception handling / Casual chat / Correction feedback]
**Scene**: [One-sentence summary]
**People involved**: [User + relevant people]
**Full sequence**:
  - [Step] Who did what / said what
  - ...
  - [Outcome]
**User's exact words**: "[Preserve key quotes verbatim when possible]"
**→ Extracted to persona**: [What behavioral pattern was updated]
**→ Extracted to business**: [What business knowledge was updated]
```

### Extraction principles

1. **Evidence-based** — Every extraction must cite a specific experience. Never infer without basis.
2. **Distinguish hypothesis from validation** — 1-2 observations = hypothesis (mark "pending"). 3+ = validated.
3. **Preserve exact quotes** — Key user quotes are more accurate than AI paraphrases.
4. **Tag context** — The same behavior may mean different things in different situations.
5. **Timely but not excessive** — Record promptly when new information is found, but don't interrupt conversation to do so.

## Questioning Strategy

### When to ask
- Early calibration (shadow mode): Ask actively to build baseline understanding quickly.
- Mid calibration (co-pilot mode): Ask to resolve uncertain hypotheses.
- Late calibration (delegated mode): Only ask for genuinely novel situations.

### Questioning principles
- Never more than 2 questions at once.
- Use open-ended questions, not yes/no.
- Questions should help you distinguish hypothesis validity.
- Never ask "how well am I doing?" — focus on specific behaviors, not overall evaluation.
- If the user is busy or unresponsive, stop immediately. Do not follow up.

### Good question examples
- "Last time you had Xiao Zhang redo that proposal — was it mainly because of data issues or formatting issues?"
- "You seem to communicate with Client A and Client B quite differently. What's the main difference?"

### Bad question examples
- "How am I doing?" (No information value)
- "What kind of people do you like?" (Too broad, cannot update specific modules)
- "Can you summarize your management style?" (Should infer from observation, not ask the user to fill out a survey)
