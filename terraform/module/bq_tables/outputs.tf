output "adoption_opendata_table" {
  description = "Table ID for each table"
  value       = google_bigquery_table.adoption_opendata_table.table_id
}
