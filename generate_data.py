import pandas as pd
import numpy as np

np.random.seed(7)
n = 850

years = np.random.choice([2019, 2020, 2021, 2022, 2023, 2024], n,
                          p=[0.14, 0.13, 0.16, 0.18, 0.20, 0.19])
months = np.random.choice(range(1, 13), n)

departments = ['Underground Mining', 'Open Pit Operations', 'Processing Plant',
               'Maintenance', 'Electrical', 'Logistics & Transport',
               'Tailings Management', 'Drilling & Blasting', 'HSE / Supervision']
dept_weights = [0.20, 0.18, 0.15, 0.14, 0.08, 0.10, 0.07, 0.05, 0.03]

incident_types = ['Slip / Trip / Fall', 'Equipment Contact', 'Struck by Object',
                  'Manual Handling', 'Electrical Incident', 'Vehicle Collision',
                  'Chemical Exposure', 'Near Miss', 'Fire / Explosion']
type_weights = [0.22, 0.18, 0.16, 0.14, 0.08, 0.10, 0.05, 0.04, 0.03]

severity = ['Near Miss', 'First Aid', 'Medical Treatment', 'Lost Time Injury', 'Fatality']
sev_weights = [0.35, 0.30, 0.20, 0.13, 0.02]

shifts = ['Day', 'Night', 'Afternoon']
shift_weights = [0.45, 0.30, 0.25]

experience = ['<1 year', '1–3 years', '3–5 years', '5–10 years', '>10 years']
exp_weights = [0.18, 0.25, 0.22, 0.20, 0.15]

root_causes = ['Inadequate procedure', 'Insufficient training', 'Equipment failure',
               'Environmental condition', 'Human error', 'Poor communication',
               'Fatigue', 'Inadequate supervision', 'PPE non-compliance']
cause_weights = [0.18, 0.20, 0.12, 0.08, 0.17, 0.10, 0.07, 0.05, 0.03]

sev_days = {'Near Miss': 0, 'First Aid': 0, 'Medical Treatment': 1,
            'Lost Time Injury': np.nan, 'Fatality': np.nan}

records = []
for i in range(n):
    sev = np.random.choice(severity, p=sev_weights)
    if sev == 'Lost Time Injury':
        days = int(np.random.exponential(8)) + 1
    elif sev == 'Fatality':
        days = 0
    else:
        days = sev_days[sev]

    records.append({
        'incident_id': f'INC-{i+1:04d}',
        'year': years[i],
        'month': months[i],
        'department': np.random.choice(departments, p=dept_weights),
        'incident_type': np.random.choice(incident_types, p=type_weights),
        'severity': sev,
        'shift': np.random.choice(shifts, p=shift_weights),
        'worker_experience': np.random.choice(experience, p=exp_weights),
        'root_cause': np.random.choice(root_causes, p=cause_weights),
        'days_lost': days,
        'corrective_action_taken': np.random.choice(['Yes', 'No', 'Partial'],
                                                     p=[0.55, 0.20, 0.25])
    })

df = pd.DataFrame(records)
df.to_csv('/home/claude/project2_mining_safety/mining_safety_incidents.csv', index=False)
print(f"Dataset: {len(df)} rows")
print(df['severity'].value_counts())
