output "paw_match_dataset_id" {
  description = "Table ID for each table"
  value       = google_bigquery_dataset.paw_match.dataset_id
}

output "adoption_opendata_table_id" {
  description = "Table ID for each table"
  value       = google_bigquery_table.adoption_opendata.table_id
}
