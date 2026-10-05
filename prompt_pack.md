Part D — AI-Augmented Reporting: Prompt Pack

Dataset Grounding

All numerical business metrics in this prompt pack are grounded in the reconciled Urban Service Parts A–C outputs.

Verified company-level metrics:

Final bookings: 600

Final revenue: ₹10,47,973

City-category segments: 27

Verified city-level KPI figures:

City

Revenue (₹)

SLA Breaches

City-Category Count

Pune

₹228,727

14

4

Bengaluru

₹179,835

17

5

Chennai

₹175,572

15

3

Hyderabad

₹171,638

14

5

Mumbai

₹151,430

13

5

Delhi NCR

₹140,771

6

5

The assistant must not invent, estimate, or replace any metric with an unsupported figure.

Prompt 1 — Weekly Ops Summary Email

Prompt

Act as an Urban Company Operations Reporting Assistant.

Draft a professional 200–300 word weekly operations update email for the Urban Company Ops team.

Use ONLY the verified Urban Service metrics supplied below. Never invent, estimate, infer, or substitute a revenue, booking, SLA, percentage, or other business metric.

Verified company metrics:

Final bookings: 600

Final revenue: ₹10,47,973

City-category segments: 27

Verified city metrics:

Pune: Revenue ₹228,727; SLA breaches 14; city-category count 4.

Bengaluru: Revenue ₹179,835; SLA breaches 17; city-category count 5.

Chennai: Revenue ₹175,572; SLA breaches 15; city-category count 3.

Hyderabad: Revenue ₹171,638; SLA breaches 14; city-category count 5.

Mumbai: Revenue ₹151,430; SLA breaches 13; city-category count 5.

Delhi NCR: Revenue ₹140,771; SLA breaches 6; city-category count 5.

Use the verified reporting period represented by the Urban Service dataset when naming the subject line. Do not invent a date or period.

The email must contain:

A subject line naming the reporting period.

One opening statement summarizing overall performance.

Three to four bullet points with key city metrics.

Exactly two positive highlights.

Exactly two issues or challenges.

A solution-oriented operational remark that connects the challenges to practical follow-up.

The audience is the Urban Company Ops team. Focus on operational performance, city-level revenue, SLA performance, and practical follow-up.

Use a professional tone and no informal language.

Use INR/₹ only. Never use dollar symbols.

Do not introduce any number that is not directly supported by the supplied verified metrics.

Critic-and-Refine Pass

A. First-Draft Prompt

Act as an Urban Company Operations Reporting Assistant.

Write a professional weekly operations update email using the following verified Urban Service metrics:

Total bookings: 600

Total revenue: ₹10,47,973

Pune revenue: ₹228,727 and SLA breaches: 14

Bengaluru revenue: ₹179,835 and SLA breaches: 17

Chennai revenue: ₹175,572 and SLA breaches: 15

Hyderabad revenue: ₹171,638 and SLA breaches: 14

Mumbai revenue: ₹151,430 and SLA breaches: 13

Delhi NCR revenue: ₹140,771 and SLA breaches: 6

Include a subject line, an opening summary, key city metrics, positive highlights, challenges, and suggested actions. Keep the email professional and between 200 and 300 words.

B. Assistant's First Output

Subject: Urban Service Operations Update — Verified Weekly Performance

Dear Operations Team,

The Urban Service dataset recorded 600 bookings and total revenue of ₹10,47,973 across six cities. Pune generated the highest city revenue, while Delhi NCR recorded the lowest number of SLA breaches.

Pune generated ₹228,727 in revenue with 14 SLA breaches.

Bengaluru generated ₹179,835 with 17 SLA breaches, the highest SLA-breach count among the six cities.

Chennai generated ₹175,572 with 15 SLA breaches.

Delhi NCR generated ₹140,771 with 6 SLA breaches.

Positive highlights:

Pune delivered the highest revenue among the six cities.

Delhi NCR recorded the lowest SLA-breach count.

Issues and challenges:

Bengaluru recorded 17 SLA breaches and requires operational review.

Chennai recorded 15 SLA breaches and requires attention to service execution.

Operations teams should review the causes of SLA breaches in Bengaluru and Chennai, identify recurring operational issues, and strengthen corrective follow-up with the relevant city and category teams.

Regards,
Urban Company Operations Reporting

C. Critique of First Output

Specificity

The first draft uses the supplied metrics, but the prompt does not explicitly prevent the assistant from inventing additional metrics or unsupported percentages. A concrete gap is that the source-control instruction is not strong enough.

Audience Fit

The output is suitable for the Urban Company Ops team because it focuses on city revenue and SLA performance. However, the prompt should explicitly identify the audience and require operationally useful commentary.

Completeness

The first output contains the major requested sections, but the first prompt does not explicitly require the exact quantities for all sections. A concrete gap is the absence of explicit requirements for exactly two positive highlights and exactly two issues/challenges.

Actionability

The output suggests reviewing Bengaluru and Chennai, which is useful. However, the prompt should explicitly require a solution-oriented operational remark connected to the identified challenges.

D. Refined Prompt

Act as an Urban Company Operations Reporting Assistant.

Draft a professional 200–300 word weekly operations update email for the Urban Company Ops team.

Use ONLY the verified Urban Service metrics supplied below. Never invent, estimate, infer, or substitute a revenue, booking, SLA, percentage, or other business metric.

Verified company metrics:

Final bookings: 600

Final revenue: ₹10,47,973

City-category segments: 27

Verified city metrics:

Pune: Revenue ₹228,727; SLA breaches 14; city-category count 4.

Bengaluru: Revenue ₹179,835; SLA breaches 17; city-category count 5.

Chennai: Revenue ₹175,572; SLA breaches 15; city-category count 3.

Hyderabad: Revenue ₹171,638; SLA breaches 14; city-category count 5.

Mumbai: Revenue ₹151,430; SLA breaches 13; city-category count 5.

Delhi NCR: Revenue ₹140,771; SLA breaches 6; city-category count 5.

Use the verified reporting period represented by the Urban Service dataset when naming the subject line. Do not invent a date or period.

The email must contain:

A subject line naming the reporting period.

One opening statement summarizing overall performance.

Three to four bullet points with key city metrics.

Exactly two positive highlights.

Exactly two issues or challenges.

A solution-oriented operational remark that connects the challenges to practical follow-up.

The audience is the Urban Company Ops team. Focus on operational performance, city-level revenue, SLA performance, and practical follow-up.

Use a professional tone and no informal language.

Use INR/₹ only. Never use dollar symbols.

Do not introduce any number that is not directly supported by the supplied verified metrics.

E. Assistant's Refined Output

Subject: Urban Service Operations Update — Verified Weekly Performance

Dear Operations Team,

The Urban Service dataset recorded 600 bookings and total revenue of ₹10,47,973 across six cities and 27 city-category segments. Revenue performance was led by Pune, while SLA performance varied across cities.

Pune recorded the highest revenue at ₹228,727, with 14 SLA breaches.

Bengaluru generated ₹179,835 and recorded 17 SLA breaches, the highest SLA-breach count among the six cities.

Chennai generated ₹175,572 with 15 SLA breaches.

Delhi NCR generated ₹140,771 with 6 SLA breaches, the lowest SLA-breach count among the six cities.

Positive highlights:

Pune recorded the highest city revenue.

Delhi NCR recorded the lowest SLA-breach count.

Issues and challenges:

Bengaluru recorded 17 SLA breaches and requires focused operational review.

Chennai recorded 15 SLA breaches and requires attention to service execution.

Operations teams should review the underlying causes of SLA breaches in Bengaluru and Chennai, identify recurring service issues, and strengthen corrective actions with the relevant city and category teams.

Regards,
Urban Company Operations Reporting

Prompt 2 — Stakeholder Narrative Draft

Prompt

Act as an Urban Company City Operations reporting assistant.

Using ONLY the verified numbers, findings, and observations contained in DASHBOARD_STORY.md, write a first draft of the City Ops Lead narrative from Part C.

Do not introduce any new metric, percentage, ranking, revenue figure, booking count, SLA figure, or other numerical claim that is not present in DASHBOARD_STORY.md.

Structure the narrative exactly as follows:

Headline

Write one concise operational headline that captures the main City Ops finding from the dashboard.

Evidence

Summarize the most important verified dashboard evidence. Use only the figures and findings present in DASHBOARD_STORY.md.

Implication

Explain what the evidence means for City Operations and identify the operational attention or follow-up that logically follows from the verified evidence.

Keep the narrative concise, professional, and suitable for a City Ops Lead stakeholder.

Use INR/₹ only where currency is required. Never use dollar symbols.

Prompt 3 — Complaint Triage Prompt

Prompt

Act as a customer-complaint triage assistant.

You will receive one raw customer complaint description.

Extract only the information required by the downstream escalation-agent specification.

Return a short structured summary containing exactly these fields:

booking_amount_inr

sla_breach_flag

partner_rating

Rules for extraction:

Copy the booking amount into booking_amount_inr when it is explicitly available.

Report 1 for sla_breach_flag only when the complaint explicitly indicates that an SLA breach occurred.

Report 0 when the complaint explicitly indicates that there was no SLA breach.

Extract the partner rating when explicitly stated.

If any required value is not present, write missing. Never guess or infer a missing value.

Do not make the final refund or escalation decision.

Do not change or reinterpret the complaint text.

Return only the three requested fields and their extracted values.