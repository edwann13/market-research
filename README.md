
# Market Research

A React.js, FastAPI, and AWS Lambda application that allows users to quickly conduct competitive market research.

Backend is supported by Open.ai

## Backend Deployment

To deploy backend api

Setup Virtual Environment
```bash
  python3 -m venv venv
```
Activate Virtual Environment
```bash
  source venv/bin/activate
```
Install Dependencies
```bash
  pip install -r requirements.txt
```
Create Zipfile Archive of Dependencies
```bash
  cd venv/lib/python3.11/site-packages
  zip -r9 ../../../../api.zip .
```
Add API To Zipfile
```bash
  zip -g ./api.zip -r api
```
Upload ZIP File to S3
```bash
  aws s3 cp api.zip s3://{ENTER_YOUR_S3_BUCKET}/api.zip
```
Deploy New Lambda, using Upload S3 Zip File
```bash
  aws lambda update-function-code --function-name YOUR_LAMBDA_FUNCTION_NAME --s3-bucket YOUR_S3_BUCKET_NAME --s3-key api.zip
```

## Frontend Deployment
Enter Client Directory
```bash
  cd client
```
Update NPM
```bash
  sudo npm install -g npm
```
Install Dependencies
```bash
  npm install
```
Build React App
```bash
  npm run build
```
Deploy to Netlify
```bash
  ./node_modules/.bin/netlify deploy --site $NETLIFY_SITE_ID --auth $NETLIFY_ACCESS_TOKEN --prod --dir=build
```