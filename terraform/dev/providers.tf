terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "6.25.0"
    }
  }
  backend "gcs" {
    bucket = "tfstate-paw-match"
    prefix = "dev"
  }
}

provider "google" {
  project = var.project_id
  region  = var.location
}
