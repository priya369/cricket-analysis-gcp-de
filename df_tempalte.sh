python dataflow_job.py \
  --input_file gs://cricket-analysis/batsmen_rankings.csv \
  --output_table valid-verbena-437709-h5.cricket_analysis.batsmen-ranking \
  --runner DataflowRunner \
  --project valid-verbena-437709-h5 \
  --region us-east1 \
  --temp_location gs://dataops-dataflow-2024/temp
