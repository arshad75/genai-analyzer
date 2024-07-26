provider "aws" {
  region = "us-west-2"
}

resource "aws_instance" "example" {
  # Use AMI from the region specified in the provider
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"

  # Use a variable or data source for VPC ID
  vpc_security_group_ids = ["aws_security_group.example.id"]

  tags = {
    Name = "example-instance"
  }
}

resource "aws_s3_bucket" "example" {
  bucket = "example-bucket"
  # Use the acl argument instead of acl_public
  acl    = "public"

  tags = {
    Name        = "example-bucket"
    Environment = "Dev"
  }
}

resource "aws_security_group" "example" {
  name_prefix = "example-"
  vpc_id      = "vpc-123456"

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}