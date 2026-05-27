provider "aws" {
  region = "ap-south-2"
}

resource "aws_instance" "health_dashboard_ec2" {
  ami           = "ami-024ebedf48d280810"
  instance_type = "t3.micro"

  key_name = "akshara.key" 

  security_groups = ["health-dashboard-sg"]

  tags = {
    Name        = "health-dashboard-server"
    Environment = "dev"
    Project     = "personal-health-dashboard"
  }
}

resource "aws_security_group" "health-dashboard-sg" {
  name = "health-dashboard-sg"

  ingress {
    description = "SSH Access"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    description = "Django App"
    from_port   = 8000
    to_port     = 8000
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    description = "HTTP (Nginx)"
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    description = "Grafana"
    from_port   = 3000
    to_port     = 3000
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    description = "Prometheus"
    from_port   = 9090
    to_port     = 9090
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

output "ec2_public_ip" {
  value = aws_instance.health_dashboard_ec2.public_ip
}
