output "api_public_ip" {
  description = "Public IP address of the FastAPI backend EC2 instance."
  value       = aws_instance.api.public_ip
}

output "api_url" {
  description = "HTTP URL for the FastAPI backend."
  value       = "http://${aws_instance.api.public_ip}:${var.api_port}"
}

output "frontend_bucket_name" {
  description = "S3 bucket name for Angular static files."
  value       = aws_s3_bucket.frontend.bucket
}

output "frontend_cloudfront_domain" {
  description = "CloudFront distribution domain for the Angular frontend."
  value       = aws_cloudfront_distribution.frontend.domain_name
}
