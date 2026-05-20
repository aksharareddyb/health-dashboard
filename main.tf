provider "aws" {
  region = "ap-south-2"
}

resource "aws_instance" "django_server" {
  ami           = "ami-0abcdef12345"
  instance_type = "t2.micro"

  tags = {
    Name = "HealthDashboardApp"
  }
}