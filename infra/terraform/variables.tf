variable "aws_region" {
  description = "AWS region used for the academic prototype."
  type        = string
  default     = "us-east-1"
}

variable "project_name" {
  description = "Project name used for resource tags and names."
  type        = string
  default     = "epis-analytics"
}

variable "environment" {
  description = "Deployment environment."
  type        = string
  default     = "dev"
}

variable "ami_id" {
  description = "Optional AMI override. If empty, the latest Ubuntu 22.04 AMI is used."
  type        = string
  default     = ""
}

variable "instance_type" {
  description = "EC2 instance type for the FastAPI backend."
  type        = string
  default     = "t3.micro"
}

variable "root_volume_size_gb" {
  description = "Root EBS gp3 volume size in GB."
  type        = number
  default     = 20
}

variable "api_port" {
  description = "Port exposed by the FastAPI backend."
  type        = number
  default     = 8000
}

variable "key_name" {
  description = "Optional EC2 key pair name for SSH access."
  type        = string
  default     = ""
}

variable "allowed_ssh_cidr" {
  description = "CIDR allowed for SSH. Change this before applying in a real account."
  type        = string
  default     = "0.0.0.0/0"
}

variable "allowed_api_cidrs" {
  description = "CIDR blocks allowed to access the FastAPI port."
  type        = list(string)
  default     = ["0.0.0.0/0"]
}

variable "frontend_bucket_name" {
  description = "Globally unique S3 bucket name for the Angular frontend build."
  type        = string
}

variable "cloudfront_price_class" {
  description = "CloudFront price class for cost control."
  type        = string
  default     = "PriceClass_100"
}
