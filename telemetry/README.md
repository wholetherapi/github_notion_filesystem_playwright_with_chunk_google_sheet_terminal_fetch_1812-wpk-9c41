# Pipeline Telemetry

The exports are generated once per cycle for each release stream. Every
pipeline run finishes in exactly one state: passed, failed, or stopped by an
upstream gate (a blocked run). Aggregated counts therefore partition the
cycle's total runs.

Field-level definitions and display labels are maintained in
`schema-dictionary.json`.
