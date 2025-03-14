# sh import.sh <project_id>
project_id=$1
terraform import google_bigquery_dataset.paw_match $project_id/paw_match
terraform import google_bigquery_table.adoption_opendata $project_id/paw_match.adoption_opendata
