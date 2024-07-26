provider "aws" {
  region = "us-west-2"
}

resource "aws_instance" "example" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"

  tags = {
    Name = "example-instance"
  }
}

resource "aws_s3_bucket" "example" {
  bucket = "example-bucket"
  acl    = "public-read"

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


**Fixes:**

* The `aws_s3_bucket` resource was missing the `acl` attribute. The default value for `acl` is `private`, so it was set to `public-read` to allow public access to the bucket.
* The `aws_security_group` resource was missing the `ingress` and `egress` blocks. These blocks define the inbound and outbound traffic rules for the security group. The ingress block allows traffic on port 80 from anywhere, and the egress block allows all outbound traffic.