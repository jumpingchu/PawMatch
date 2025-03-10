resource "google_bigquery_dataset" "paw_match" {
  dataset_id  = var.dataset_id
  project     = var.project_id
  location    = "asia-east1"
  description = "Dataset for pet adoption data"
  lifecycle {
    prevent_destroy = true
  }
}

resource "google_bigquery_table" "adoption_opendata" {
  dataset_id = google_bigquery_dataset.paw_match.dataset_id
  table_id   = var.adoption_opendata_table
  project    = var.project_id

  schema = jsonencode([
    { name = "animal_id", type = "STRING" },
    { name = "animal_subid", type = "STRING" },
    { name = "animal_area_pkid", type = "INTEGER" },
    { name = "animal_shelter_pkid", type = "INTEGER" },
    { name = "animal_place", type = "STRING" },
    { name = "animal_kind", type = "STRING" },
    { name = "animal_Variety", type = "STRING" },
    { name = "animal_sex", type = "STRING" },
    { name = "animal_bodytype", type = "STRING" },
    { name = "animal_colour", type = "STRING" },
    { name = "animal_age", type = "STRING" },
    { name = "animal_sterilization", type = "STRING" },
    { name = "animal_bacterin", type = "STRING" },
    { name = "animal_foundplace", type = "STRING" },
    { name = "animal_title", type = "STRING" },
    { name = "animal_status", type = "STRING" },
    { name = "animal_remark", type = "STRING" },
    { name = "animal_caption", type = "STRING" },
    { name = "animal_opendate", type = "TIMESTAMP" },
    { name = "animal_closeddate", type = "TIMESTAMP" },
    { name = "animal_update", type = "TIMESTAMP" },
    { name = "animal_createtime", type = "TIMESTAMP" },
    { name = "shelter_name", type = "STRING" },
    { name = "album_file", type = "STRING" },
    { name = "album_update", type = "TIMESTAMP" },
    { name = "cDate", type = "TIMESTAMP" },
    { name = "shelter_address", type = "STRING" },
    { name = "shelter_tel", type = "STRING" }
  ])

  time_partitioning {
    type = "DAY"
    field = "animal_opendate"
  }

  lifecycle {
    prevent_destroy = true
  }
}
