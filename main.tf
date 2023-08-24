provider "aws" {
  region = "us-east-1"
}

resource "aws_vpc" "main" {
  cidr_block = "10.0.0.0/16"
}

resource "aws_subnet" "public" {
  vpc_id     = aws_vpc.main.id
  cidr_block = "10.0.1.0/24"
}

resource "aws_subnet" "private" {
  vpc_id     = aws_vpc.main.id
  cidr_block = "10.0.2.0/24"
}

resource "aws_instance" "web" {
  ami           = "ami-09e67e426f25ce0d7"
  instance_type = "t2.micro"
  subnet_id     = aws_subnet.public.id

  root_block_device {
    volume_size           = 8 # Change this value to at least 8GB
    volume_type           = "gp2"
    delete_on_termination = true
  }

  tags = {
    purpose = "Assignment"
  }
}
