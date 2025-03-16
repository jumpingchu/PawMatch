import {
  to = google_bigquery_dataset.paw_match
  id = "paw_match"
}

import {
  to = google_bigquery_table.adoption_opendata
  id = "paw_match.adoption_opendata"
}

resource "google_bigquery_dataset" "paw_match" {
  dataset_id  = var.dataset_id
  project     = var.project_id
  location    = var.location
  description = "Dataset for pet adoption data"
  lifecycle {
    prevent_destroy = true
  }
}

resource "google_bigquery_table" "adoption_opendata" {
  dataset_id = google_bigquery_dataset.paw_match.dataset_id
  table_id   = var.adoption_opendata_table
  project    = var.project_id
  deletion_protection = false

  schema = jsonencode([
    { name = "animal_id", type = "STRING" },
    { name = "animal_subid", type = "STRING" },
    { name = "animal_area_pkid", type = "STRING" },
    { name = "animal_shelter_pkid", type = "STRING" },
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
    { name = "animal_opendate", type = "DATETIME" },
    { name = "animal_closeddate", type = "STRING" },
    { name = "animal_update", type = "STRING" },
    { name = "animal_createtime", type = "STRING" },
    { name = "shelter_name", type = "STRING" },
    { name = "album_file", type = "STRING" },
    { name = "album_update", type = "STRING" },
    { name = "cDate", type = "STRING" },
    { name = "shelter_address", type = "STRING" },
    { name = "shelter_tel", type = "STRING" }
  ])

  time_partitioning {
    type = "DAY"
    field = "animal_opendate"
  }
}
