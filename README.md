# Mining Operations Safety Analytics
### Exploratory Data Analysis of Mine Site Incidents (2019–2024)

**Author:** Ninjin Norovrentsen  
**Tools:** Python (Pandas, Matplotlib, Seaborn), SQL-style queries  
**Dataset:** 850 incidents across 9 departments, 6 years  

---

## Project Overview

End-to-end exploratory data analysis of mine site safety incident data covering 850 incidents from 2019 to 2024. This project demonstrates a full analytical pipeline — data ingestion, cleaning, SQL-style querying, statistical analysis, visualization, and actionable recommendations — applied to an HSE context in mining operations.

Designed to showcase data analyst skills for mining and resources sector roles.

---

## Key Metrics

| Metric | Value |
|---|---|
| Total incidents analyzed | 850 |
| Lost Time Injuries (LTI) | 120 |
| Fatalities | 19 |
| Near Misses | 279 |
| Overall LTI rate | 14.1% |
| Average days lost per LTI | 7.5 days |

---

## Top 3 Findings

**1. Training Gap is the #1 driver of serious incidents**  
Human error and insufficient training account for 51 of 139 serious incidents (37%). Workers with <3 years experience are disproportionately represented in LTI and fatality categories.

**2. Underground Mining and Open Pit are highest-risk departments**  
335 combined incidents with the highest LTI counts. These departments require priority HSE resource allocation.

**3. Corrective Action Closure Gap**  
Only 55% of incidents have confirmed corrective actions taken. This represents a systemic failure in the incident management loop — the same root causes recur without being resolved.

---

## Repository Structure

```
project2_mining_safety/
├── mining_safety_incidents.csv  # Incident dataset (850 records)
├── analysis.py                  # Full EDA pipeline with SQL-style queries
├── generate_data.py             # Data generation script
├── outputs/
│   ├── 01_incident_trends.png
│   ├── 02_department_risk.png
│   ├── 03_root_cause_analysis.png
│   ├── 04_experience_severity.png
│   ├── 05_shift_monthly_patterns.png
│   ├── 06_corrective_actions.png
│   └── findings_report.txt
└── README.md
```

---

## Charts Generated

1. **Incident Trends** — Stacked bar by year/severity + serious incident trend line
2. **Department Risk Profile** — Incident count and serious incident rate by department
3. **Root Cause Analysis** — All incidents vs serious-only comparison
4. **Experience vs Severity Heatmap** — Worker experience level cross-tabulated with severity
5. **Shift & Monthly Patterns** — Time-based incident distribution
6. **Corrective Action Effectiveness** — Severity profile by action status

---

## SQL-Style Queries (via Pandas)

The analysis includes three business-style queries demonstrating SQL logic:

```python
# Q1: Department risk summary (LTI count, fatalities, avg days lost)
# Q2: Year-on-year trend with serious incident rate
# Q3: Root causes of serious incidents ranked
```

These replicate the logic of:
```sql
SELECT department, COUNT(*) as total, 
       SUM(CASE WHEN severity='Lost Time Injury' THEN 1 ELSE 0 END) as lti_count
FROM incidents
GROUP BY department
ORDER BY lti_count DESC
```

---

## How to Run

```bash
# Install dependencies
pip install pandas matplotlib seaborn numpy

# Run full analysis
python analysis.py
```

All outputs saved to `/outputs/` folder.

---

## Recommendations

1. Implement mandatory induction refreshers for workers with <3 years experience
2. Incentivize near-miss reporting — it is the leading indicator for serious incidents
3. Set 100% corrective action closure rate as a tracked monthly KPI
4. Target night shift with additional HSE supervision
5. Apply 5-Why and Fishbone methodology systematically to all LTI investigations

---

## Skills Demonstrated

- End-to-end EDA pipeline (ingest → clean → query → visualize → report)
- SQL-style aggregation and filtering with Pandas
- Time series trend analysis
- Heatmap and multi-panel visualization
- Root cause analysis methodology
- HSE KPI framework (LTI rate, serious incident rate, near-miss ratio)
- ISO 45001 aligned incident classification
- Actionable recommendations from data

---

*For questions or collaboration: n.ninjin@gmit.edu.mn | [LinkedIn](https://linkedin.com/in/ninjin-norovrentsen)*
