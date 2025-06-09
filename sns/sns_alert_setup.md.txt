# 📬 SNS Alert Setup

This document outlines how an SNS topic was created and integrated with CloudWatch to send email alerts when submissions exceed a threshold.

---

## ✅ Steps

1. **Create an SNS Topic**
   - Go to SNS → Create topic
   - Type: Standard
   - Name: `surveyAlertTopic`

2. **Create Email Subscription**
   - Go to the topic → Create subscription
   - Protocol: **Email**
   - Endpoint: `your-email@example.com`
   - Confirm the subscription via the email sent to you

3. **Create CloudWatch Alarm**
   - Go to CloudWatch → Alarms → Create alarm
   - Metric: `submission_count` (your custom metric)
   - Condition: Whenever value > 5 within **1 minute**

4. **Attach Action**
   - Choose SNS topic: `surveyAlertTopic`

5. **Test the Alarm**
   - Trigger 6 submissions quickly
   - You should receive an email alert like:

   > 🔔 **Alert**: More than 5 submissions received in the last minute.

---

## 📝 Notes

- You can customize the message by using Lambda to publish messages directly to the topic if needed.
- Use **CloudWatch Logs Insights** for deeper debugging.

