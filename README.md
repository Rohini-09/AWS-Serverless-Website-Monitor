# 📊 AWS Serverless Survey Monitoring Project

This is a serverless web application hosted on AWS using S3, API Gateway, Lambda, CloudWatch, and SNS. It collects survey responses, logs metrics, visualizes data, and sends email alerts when submission traffic spikes.

---

## 🔧 Tech Stack

| AWS Service     | Purpose                                                      |
|-----------------|--------------------------------------------------------------|
| Amazon S3       | Hosts static website (survey form)                           |
| API Gateway     | Exposes HTTP endpoint to handle form submissions             |
| AWS Lambda      | Processes submissions, logs custom metrics                   |
| Amazon CloudWatch | Tracks latency, submission count, logs, and dashboards     |
| Amazon SNS      | Sends email alert if more than 5 submissions in 1 minute     |

---

## 🌐 How It Works

1. User opens the survey website hosted on **Amazon S3**
2. On form submission, the request is sent via **API Gateway**
3. The request triggers an **AWS Lambda** function
4. Lambda logs submission data and latency using **CloudWatch**
5. If 5+ submissions occur within a minute, **SNS** sends an alert email

---

## 📈 Example Metrics

- `submission_count`: **28**
- `avg_latency`: **0.00006151**
- `invocation_count`: **4**
- Submissions for Yellow: **5** (7.94%)

---

## 📬 Alert Condition

If 5 or more submissions are received in a single minute, **SNS** triggers an email alert to notify potential spamming or peak load activity.

---


## 📁 Project Structure

aws-serverless-survey/
├── lambda/                # Lambda function code
│   └── lambda_function.py
├── s3_website/            # Static website files (HTML/CSS/JS)
│   ├── index.html
│   ├── survey.html
│   ├── thankyou.html
│   └── styles.css
├── api_gateway/           # API Gateway configuration or setup notes
│   └── setup.md
├── cloudwatch/            # CloudWatch screenshots (monitoring)
│   ├── Screenshot 2025-06-11 123031.png
│   ├── Screenshot 2025-06-11 123131.png
│   ├── Screenshot 2025-06-11 123204.png
│   └── Screenshot 2025-06-11 144739.png
├── sns/                   # SNS setup steps
│   └── sns_alert_setup.md
└── README.md              # This documentation file






---

## 📸 Screenshots

### 📊 CloudWatch Monitoring Screenshots

Here are screenshots showing real-time monitoring of the AWS survey website:

1. **Metric View**
   ![](cloudwatch/Screenshot%202025-06-11%20123031.png)

2. **Latency Tracking**
   ![](cloudwatch/Screenshot%202025-06-11%20123131.png)

3. **Submissions Count**
   ![](cloudwatch/Screenshot%202025-06-11%20123204.png)

4. **SNS Alert Trigger Setup**
   ![](cloudwatch/Screenshot%202025-06-11%20144739.png)


## ✉️ SNS Email Sample

> 🔔 **Alert:** More than 5 submissions received in the past minute.  
> Please review traffic activity on your survey page.

---

## 🚀 Conclusion

This project demonstrates a fully serverless application using AWS cloud services. It showcases frontend hosting, serverless compute, real-time metrics logging, alerting, and observability — all managed without traditional servers.

---

## 🔗 Contact

📧 your.email@example.com  
🔗 [LinkedIn Profile](https://www.linkedin.com/in/rohini-gusain)  
🔗 [GitHub Repo](https://github.com/Rohini-09/aws-serverless-survey)
