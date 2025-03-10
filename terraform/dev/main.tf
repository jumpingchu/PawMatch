module "bq_tables" {
  source = "../modules/bq_tables"
  project_id = var.project_id
  dataset_id = var.dataset_id
  tables = var.tables
}
