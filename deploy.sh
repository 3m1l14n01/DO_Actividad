#!/bin/bash
set -e

AWS_REGION="us-east-2"
S3_BUCKET="codepipeline-us-east-2-5bd13784c431-41b7-92b0-2ef4594a151e"   # Ajusta con el nombre real de tu bucket S3

echo "Copiando artefactos al bucket..."
aws s3 cp ./app s3://$S3_BUCKET/ --recursive --region $AWS_REGION
echo "Deploy completado en S3."
