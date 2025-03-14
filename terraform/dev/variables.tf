variable "project_id" {
  description = "The project ID of GCP"
  type        = string
}

variable "location" {
  description = "The location of GCP services"
  type        = string
}
variable "dataset_id" {
  description = "The dataset ID of BigQuery"
  type        = string
}

variable "adoption_opendata_table" {
  description = "The table of adoption opendata"
  type        = string
}
