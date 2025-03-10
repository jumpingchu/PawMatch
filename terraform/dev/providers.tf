terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 5.0"
    }
  }
  backend "gcs" {
    bucket = "tfstate-bucket"
    prefix = "paw-match/dev"
  }
}

provider "google" {
  project = var.project_id
  region  = "asia-east1"
}
