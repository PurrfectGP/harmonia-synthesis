"""
Email Service - Zoho Mail Integration
Handles all email functionality with secure configuration
"""

import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from typing import List, Optional
import logging

logger = logging.getLogger(__name__)


class EmailService:
    """Email service using Zoho Mail SMTP"""

    def __init__(self):
        # Zoho Mail SMTP Configuration
        self.smtp_host = os.getenv('SMTP_HOST', 'smtp.zoho.com')
        self.smtp_port = int(os.getenv('SMTP_PORT', '465'))  # SSL port
        self.smtp_user = os.getenv('SMTP_USER')  # Your Zoho email
        self.smtp_password = os.getenv('SMTP_PASSWORD')  # Zoho app-specific password
        self.from_email = os.getenv('FROM_EMAIL', self.smtp_user)
        self.from_name = os.getenv('FROM_NAME', 'Harmonia')
        self.use_ssl = os.getenv('SMTP_USE_SSL', 'true').lower() == 'true'

        if not self.smtp_user or not self.smtp_password:
            logger.warning("⚠️  Email credentials not configured. Email functionality disabled.")
            self.enabled = False
        else:
            self.enabled = True
            logger.info(f"✅ Email service initialized: {self.smtp_user}")

    def send_email(
        self,
        to_email: str,
        subject: str,
        body_html: str,
        body_text: Optional[str] = None,
        attachments: Optional[List[dict]] = None,
        reply_to: Optional[str] = None
    ) -> bool:
        """
        Send email via Zoho Mail SMTP

        Args:
            to_email: Recipient email address
            subject: Email subject
            body_html: HTML body content
            body_text: Plain text body (optional, will be auto-generated if not provided)
            attachments: List of dicts with 'filename' and 'content' keys
            reply_to: Reply-to email address

        Returns:
            bool: True if sent successfully, False otherwise
        """
        if not self.enabled:
            logger.error("❌ Email service not configured")
            return False

        try:
            # Create message
            msg = MIMEMultipart('alternative')
            msg['Subject'] = subject
            msg['From'] = f"{self.from_name} <{self.from_email}>"
            msg['To'] = to_email

            if reply_to:
                msg['Reply-To'] = reply_to

            # Add plain text version
            if body_text:
                part1 = MIMEText(body_text, 'plain')
                msg.attach(part1)

            # Add HTML version
            part2 = MIMEText(body_html, 'html')
            msg.attach(part2)

            # Add attachments if provided
            if attachments:
                for attachment in attachments:
                    part = MIMEBase('application', 'octet-stream')
                    part.set_payload(attachment['content'])
                    encoders.encode_base64(part)
                    part.add_header(
                        'Content-Disposition',
                        f"attachment; filename= {attachment['filename']}"
                    )
                    msg.attach(part)

            # Send email
            if self.use_ssl:
                # Use SSL (port 465)
                with smtplib.SMTP_SSL(self.smtp_host, self.smtp_port) as server:
                    server.login(self.smtp_user, self.smtp_password)
                    server.send_message(msg)
            else:
                # Use TLS (port 587)
                with smtplib.SMTP(self.smtp_host, self.smtp_port) as server:
                    server.starttls()
                    server.login(self.smtp_user, self.smtp_password)
                    server.send_message(msg)

            logger.info(f"✅ Email sent to {to_email}: {subject}")
            return True

        except Exception as e:
            logger.error(f"❌ Failed to send email to {to_email}: {e}")
            return False

    def send_compatibility_report(
        self,
        to_email: str,
        user_name: str,
        partner_name: str,
        overall_score: float,
        report_url: str
    ) -> bool:
        """Send compatibility report notification email"""

        subject = f"Your Harmonia Compatibility Report with {partner_name} is Ready!"

        html_body = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <style>
                body {{
                    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
                    line-height: 1.6;
                    color: #333;
                    max-width: 600px;
                    margin: 0 auto;
                    padding: 20px;
                }}
                .header {{
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    color: white;
                    padding: 30px;
                    border-radius: 10px 10px 0 0;
                    text-align: center;
                }}
                .content {{
                    background: white;
                    padding: 30px;
                    border: 1px solid #e0e0e0;
                    border-top: none;
                }}
                .score {{
                    font-size: 48px;
                    font-weight: bold;
                    color: #667eea;
                    text-align: center;
                    margin: 20px 0;
                }}
                .button {{
                    display: inline-block;
                    padding: 15px 30px;
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    color: white;
                    text-decoration: none;
                    border-radius: 5px;
                    font-weight: bold;
                    margin: 20px 0;
                }}
                .footer {{
                    text-align: center;
                    margin-top: 30px;
                    color: #666;
                    font-size: 14px;
                }}
            </style>
        </head>
        <body>
            <div class="header">
                <h1>💫 Harmonia</h1>
                <p>Your Compatibility Analysis is Complete</p>
            </div>
            <div class="content">
                <h2>Hi {user_name},</h2>
                <p>We've completed your compatibility analysis with {partner_name}!</p>

                <div class="score">
                    {overall_score:.1f}%
                </div>
                <p style="text-align: center; color: #666;">Overall Compatibility Score</p>

                <p>Your detailed report includes:</p>
                <ul>
                    <li>🧬 Personality Compatibility Analysis</li>
                    <li>👁️ Visual Chemistry Assessment</li>
                    <li>🧪 Genetic Harmony Insights</li>
                    <li>💡 Relationship Recommendations</li>
                    <li>📊 Detailed Compatibility Breakdown</li>
                </ul>

                <center>
                    <a href="{report_url}" class="button">View Your Full Report</a>
                </center>

                <p style="margin-top: 30px;">Thank you for using Harmonia to explore your connections!</p>
            </div>
            <div class="footer">
                <p>Harmonia - Understanding Connections Through Science</p>
                <p>Questions? Reply to this email - we're here to help!</p>
            </div>
        </body>
        </html>
        """

        text_body = f"""
        Hi {user_name},

        Your Harmonia compatibility analysis with {partner_name} is complete!

        Overall Compatibility Score: {overall_score:.1f}%

        Your detailed report includes:
        - Personality Compatibility Analysis
        - Visual Chemistry Assessment
        - Genetic Harmony Insights
        - Relationship Recommendations
        - Detailed Compatibility Breakdown

        View your full report: {report_url}

        Thank you for using Harmonia!

        ---
        Harmonia - Understanding Connections Through Science
        """

        return self.send_email(to_email, subject, html_body, text_body)

    def send_welcome_email(self, to_email: str, user_name: str) -> bool:
        """Send welcome email to new users"""

        subject = "Welcome to Harmonia! 🌟"

        html_body = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <style>
                body {{
                    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
                    line-height: 1.6;
                    color: #333;
                    max-width: 600px;
                    margin: 0 auto;
                    padding: 20px;
                }}
                .header {{
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    color: white;
                    padding: 30px;
                    border-radius: 10px 10px 0 0;
                    text-align: center;
                }}
                .content {{
                    background: white;
                    padding: 30px;
                    border: 1px solid #e0e0e0;
                    border-top: none;
                }}
                .feature {{
                    margin: 20px 0;
                    padding: 15px;
                    background: #f8f9fa;
                    border-radius: 5px;
                }}
                .footer {{
                    text-align: center;
                    margin-top: 30px;
                    color: #666;
                    font-size: 14px;
                }}
            </style>
        </head>
        <body>
            <div class="header">
                <h1>💫 Welcome to Harmonia</h1>
            </div>
            <div class="content">
                <h2>Hi {user_name}! 👋</h2>
                <p>Welcome to Harmonia - where science meets connection!</p>

                <p>We're excited to help you understand your relationships through:</p>

                <div class="feature">
                    <strong>🧬 Personality Analysis</strong>
                    <p>Deep insights into behavioral patterns and compatibility</p>
                </div>

                <div class="feature">
                    <strong>👁️ Visual Chemistry</strong>
                    <p>AI-powered assessment of mutual attraction</p>
                </div>

                <div class="feature">
                    <strong>🧪 Genetic Harmony</strong>
                    <p>HLA compatibility analysis for biological insight</p>
                </div>

                <h3>Getting Started</h3>
                <ol>
                    <li>Complete your personality assessment</li>
                    <li>Upload your photo (optional)</li>
                    <li>Add your genetic data (optional)</li>
                    <li>Generate compatibility reports!</li>
                </ol>

                <p>Ready to discover meaningful connections? Let's begin!</p>
            </div>
            <div class="footer">
                <p>Harmonia - Understanding Connections Through Science</p>
                <p>Have questions? Just reply to this email!</p>
            </div>
        </body>
        </html>
        """

        text_body = f"""
        Hi {user_name}!

        Welcome to Harmonia - where science meets connection!

        We're excited to help you understand your relationships through:

        🧬 Personality Analysis - Deep insights into behavioral patterns
        👁️ Visual Chemistry - AI-powered attraction assessment
        🧪 Genetic Harmony - HLA compatibility analysis

        Getting Started:
        1. Complete your personality assessment
        2. Upload your photo (optional)
        3. Add your genetic data (optional)
        4. Generate compatibility reports!

        Ready to discover meaningful connections? Let's begin!

        ---
        Harmonia - Understanding Connections Through Science
        Have questions? Just reply to this email!
        """

        return self.send_email(to_email, subject, html_body, text_body)

    def send_analysis_complete(
        self,
        to_email: str,
        user_name: str,
        analysis_type: str,
        download_url: str
    ) -> bool:
        """Send notification when analysis is complete"""

        subject = f"Your {analysis_type} Analysis is Ready!"

        html_body = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <style>
                body {{
                    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
                    line-height: 1.6;
                    color: #333;
                    max-width: 600px;
                    margin: 0 auto;
                    padding: 20px;
                }}
                .header {{
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    color: white;
                    padding: 30px;
                    border-radius: 10px 10px 0 0;
                    text-align: center;
                }}
                .content {{
                    background: white;
                    padding: 30px;
                    border: 1px solid #e0e0e0;
                    border-top: none;
                }}
                .button {{
                    display: inline-block;
                    padding: 15px 30px;
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    color: white;
                    text-decoration: none;
                    border-radius: 5px;
                    font-weight: bold;
                    margin: 20px 0;
                }}
                .footer {{
                    text-align: center;
                    margin-top: 30px;
                    color: #666;
                    font-size: 14px;
                }}
            </style>
        </head>
        <body>
            <div class="header">
                <h1>✅ Analysis Complete!</h1>
            </div>
            <div class="content">
                <h2>Hi {user_name},</h2>
                <p>Great news! Your {analysis_type} analysis is complete and ready to download.</p>

                <center>
                    <a href="{download_url}" class="button">Download Report</a>
                </center>

                <p>This report is generated specifically for you and contains detailed insights.</p>

                <p>Thank you for using Harmonia!</p>
            </div>
            <div class="footer">
                <p>Harmonia - Understanding Connections Through Science</p>
            </div>
        </body>
        </html>
        """

        return self.send_email(to_email, subject, html_body)
