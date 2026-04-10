#!/bin/bash
set -e

AWS_REGION="us-east-2"
S3_BUCKET="mi-bucket-deploy"   # Ajusta con el nombre real de tu bucket S3

echo "Copiando artefactos al bucket..."
aws s3 cp ./app s3://$S3_BUCKET/ --recursive --region $AWS_REGION
echo "Deploy completado en S3."
