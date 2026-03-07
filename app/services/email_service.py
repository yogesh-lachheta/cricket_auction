"""
Email Service

Handles sending emails for OTP verification and notifications.
Uses SMTP (Gmail) for sending emails.
"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import Optional
import os


class EmailService:
    """Service class for email operations."""

    # Email configuration (from environment variables)
    SMTP_HOST = os.getenv("SMTP_HOST", "smtp.gmail.com")
    SMTP_PORT = int(os.getenv("SMTP_PORT", "587"))
    SMTP_USER = os.getenv("SMTP_USER", "")
    SMTP_PASSWORD = os.getenv("SMTP_PASSWORD", "")
    FROM_EMAIL = os.getenv("FROM_EMAIL", SMTP_USER)
    FROM_NAME = os.getenv("FROM_NAME", "Cricket Auction Platform")

    @staticmethod
    def send_email(
        to_email: str,
        subject: str,
        body: str,
        is_html: bool = False
    ) -> bool:
        """
        Send an email.

        Args:
            to_email: Recipient email address
            subject: Email subject
            body: Email body content
            is_html: Whether body is HTML (default: False)

        Returns:
            bool: True if email sent successfully, False otherwise
        """
        try:
            # Create message
            message = MIMEMultipart("alternative")
            message["From"] = f"{EmailService.FROM_NAME} <{EmailService.FROM_EMAIL}>"
            message["To"] = to_email
            message["Subject"] = subject

            # Add body
            if is_html:
                part = MIMEText(body, "html")
            else:
                part = MIMEText(body, "plain")

            message.attach(part)

            # Check if SMTP is configured
            if not EmailService.SMTP_USER or not EmailService.SMTP_PASSWORD:
                print(f"📧 [DEV MODE] Email to {to_email}")
                print(f"Subject: {subject}")
                print(f"Body:\n{body}")
                print("=" * 50)
                return True

            # Send email via SMTP
            with smtplib.SMTP(EmailService.SMTP_HOST, EmailService.SMTP_PORT) as server:
                server.starttls()
                server.login(EmailService.SMTP_USER, EmailService.SMTP_PASSWORD)
                server.send_message(message)

            print(f"✅ Email sent successfully to {to_email}")
            return True

        except Exception as e:
            print(f"❌ Failed to send email to {to_email}: {str(e)}")
            return False

    @staticmethod
    def send_otp_email(to_email: str, otp_code: str, user_name: Optional[str] = None) -> bool:
        """
        Send OTP verification email.

        Args:
            to_email: Recipient email address
            otp_code: 6-digit OTP code
            user_name: User's name (optional)

        Returns:
            bool: True if email sent successfully, False otherwise
        """
        subject = "Verify Your Email - Cricket Auction Platform"

        # Create email body
        greeting = f"Hello {user_name}," if user_name else "Hello,"

        body = f"""{greeting}

Thank you for registering with Cricket Auction Platform!

Your email verification code is:

    {otp_code}

This code will expire in 5 minutes.

If you didn't request this code, please ignore this email.

Best regards,
Cricket Auction Platform Team
"""

        # HTML version (prettier)
        html_body = f"""
<!DOCTYPE html>
<html>
<head>
    <style>
        body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; }}
        .container {{ max-width: 600px; margin: 0 auto; padding: 20px; }}
        .header {{ background-color: #4CAF50; color: white; padding: 20px; text-align: center; border-radius: 5px; }}
        .content {{ padding: 20px; background-color: #f9f9f9; border-radius: 5px; margin-top: 20px; }}
        .otp-code {{ font-size: 32px; font-weight: bold; color: #4CAF50; text-align: center; padding: 20px; background-color: white; border-radius: 5px; margin: 20px 0; letter-spacing: 5px; }}
        .footer {{ text-align: center; margin-top: 20px; color: #777; font-size: 12px; }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🏏 Cricket Auction Platform</h1>
        </div>
        <div class="content">
            <p>{greeting}</p>
            <p>Thank you for registering with Cricket Auction Platform!</p>
            <p>Your email verification code is:</p>
            <div class="otp-code">{otp_code}</div>
            <p><strong>This code will expire in 5 minutes.</strong></p>
            <p>If you didn't request this code, please ignore this email.</p>
        </div>
        <div class="footer">
            <p>Best regards,<br>Cricket Auction Platform Team</p>
        </div>
    </div>
</body>
</html>
"""

        return EmailService.send_email(to_email, subject, html_body, is_html=True)

    @staticmethod
    def send_welcome_email(to_email: str, user_name: str) -> bool:
        """
        Send welcome email after successful registration.

        Args:
            to_email: Recipient email address
            user_name: User's name

        Returns:
            bool: True if email sent successfully, False otherwise
        """
        subject = "Welcome to Cricket Auction Platform!"

        body = f"""Hello {user_name},

Welcome to Cricket Auction Platform! 🏏

Your account has been successfully created and verified.

You can now:
- Participate in live cricket auctions
- Manage your team
- Bid on your favorite players

Visit our platform to get started: http://localhost:8000

Best regards,
Cricket Auction Platform Team
"""

        return EmailService.send_email(to_email, subject, body)
