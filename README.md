# Health Graduate Outcomes Analysis

This project analyzes health graduate employment and education outcomes in Ireland using data from the CSO. It explores how gender, field of study, and time since graduation affect graduate paths.

## Key Questions
- How have graduate outcomes changed over time?
- Are there gender-based differences?
- What is the impact of years since graduation?
- Do different fields of study show statistically significant differences?

## Dataset
- Source: Central Statistics Office (CSO) – [Data.gov.ie](https://data.gov.ie/dataset/hgo03-health-graduate-outcomes)
- Records: 4,356
- Variables: Graduation Year, Gender, Field of Study, Graduate Outcome, Years Since Graduation, etc.

## Methods
- Data cleaning and exploration
- Grouping and aggregating data
- Statistical tests:
  - One-way ANOVA
  - Independent T-test
  - Chi-Square test
- Visualization with `matplotlib` and `seaborn`

## Results
- **Gender**: Females tend to have higher graduate numbers across most outcomes.
- **Time Since Graduation**: Employment decreases steadily after graduation.
- **Fields of Study**: Significant variation in outcomes across disciplines.
- **Statistical Tests**:
  - ANOVA showed strong differences by field
  - T-Test found gender-based differences
  - Chi-Square found no significant association between gender and outcome

## Author
Ilham Oussanna 
