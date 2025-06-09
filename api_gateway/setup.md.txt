# 🌐 API Gateway Setup

This guide explains how the API Gateway was configured to receive survey form submissions and invoke the Lambda function.

---

## ✅ Steps

1. **Create a new API**
   - Go to API Gateway → Create API → Choose **HTTP API**

2. **Add Integration**
   - Integration type: **Lambda function**
   - Select your region and choose your Lambda (e.g., `surveyLambdaFunction`)

3. **Configure Routes**
   - Method: `POST`
   - Path: `/submit`

4. **Enable CORS**
   - Allowed Origins: `https://mysurveysite.s3.us-east-1.amazonaws.com`
   - Allowed Methods: `POST, OPTIONS`
   - Allowed Headers: `Content-Type, x-api-key`

5. **Deploy API**
   - Create a new stage (e.g., `prod`)
   - Copy the endpoint URL (e.g., `https://your-api-id.execute-api.us-east-1.amazonaws.com/submit`)

6. **Connect to Frontend**
   - In your HTML/JS form, submit the form using `fetch()` or `axios()` to the API Gateway endpoint.

---

## 🧪 Testing

- Open the S3 website and submit the form.
- Check CloudWatch logs to ensure Lambda is triggered.
