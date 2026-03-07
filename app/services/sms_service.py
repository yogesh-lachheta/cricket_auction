"""
SMS Service

Handles sending SMS for mobile OTP verification.
Development mode: Logs to console (FREE)
Production mode: Can integrate with Twilio, AWS SNS, or other SMS gateways
"""

import os
from typing import Optional


class SMSService:
    """Service class for SMS operations."""

    # SMS configuration (from environment variables)
    SMS_PROVIDER = os.getenv("SMS_PROVIDER", "console")  # console, twilio, aws_sns
    TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID", "")
    TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN", "")
    TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER", "")

    @staticmethod
    def send_sms(to_mobile: str, message: str) -> bool:
        """
        Send an SMS message.

        In development mode (default), logs to console instead of sending real SMS.
        In production, configure SMS_PROVIDER in .env file.

        Args:
            to_mobile: Recipient mobile number (with country code)
            message: SMS message content

        Returns:
            bool: True if SMS sent successfully, False otherwise
        """
        try:
            if SMSService.SMS_PROVIDER == "console":
                # Development mode: Log to console (FREE)
                print("\n" + "=" * 60)
                print("📱 [DEV MODE] SMS MESSAGE")
                print("=" * 60)
                print(f"To: {to_mobile}")
                print(f"Message: {message}")
                print("=" * 60 + "\n")
                return True

            elif SMSService.SMS_PROVIDER == "twilio":
                # Production mode: Use Twilio
                return SMSService._send_via_twilio(to_mobile, message)

            elif SMSService.SMS_PROVIDER == "aws_sns":
                # Production mode: Use AWS SNS
                return SMSService._send_via_aws_sns(to_mobile, message)

            else:
                print(f"❌ Unknown SMS provider: {SMSService.SMS_PROVIDER}")
                return False

        except Exception as e:
            print(f"❌ Failed to send SMS to {to_mobile}: {str(e)}")
            return False

    @staticmethod
    def _send_via_twilio(to_mobile: str, message: str) -> bool:
        """
        Send SMS via Twilio.

        Requires: pip install twilio
        Environment variables: TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_PHONE_NUMBER

        Args:
            to_mobile: Recipient mobile number
            message: SMS message content

        Returns:
            bool: True if SMS sent successfully, False otherwise
        """
        try:
            from twilio.rest import Client

            # Check if Twilio is configured
            if not all([
                SMSService.TWILIO_ACCOUNT_SID,
                SMSService.TWILIO_AUTH_TOKEN,
                SMSService.TWILIO_PHONE_NUMBER
            ]):
                print("❌ Twilio not configured. Set TWILIO_* environment variables.")
                return False

            # Create Twilio client
            client = Client(
                SMSService.TWILIO_ACCOUNT_SID,
                SMSService.TWILIO_AUTH_TOKEN
            )

            # Send SMS
            message_obj = client.messages.create(
                body=message,
                from_=SMSService.TWILIO_PHONE_NUMBER,
                to=to_mobile
            )

            print(f"✅ SMS sent successfully via Twilio. SID: {message_obj.sid}")
            return True

        except ImportError:
            print("❌ Twilio library not installed. Run: pip install twilio")
            return False
        except Exception as e:
            print(f"❌ Twilio SMS failed: {str(e)}")
            return False

    @staticmethod
    def _send_via_aws_sns(to_mobile: str, message: str) -> bool:
        """
        Send SMS via AWS SNS.

        Requires: pip install boto3
        AWS credentials should be configured via AWS CLI or environment variables

        Args:
            to_mobile: Recipient mobile number
            message: SMS message content

        Returns:
            bool: True if SMS sent successfully, False otherwise
        """
        try:
            import boto3

            # Create SNS client
            sns_client = boto3.client('sns')

            # Send SMS
            response = sns_client.publish(
                PhoneNumber=to_mobile,
                Message=message,
                MessageAttributes={
                    'AWS.SNS.SMS.SMSType': {
                        'DataType': 'String',
                        'StringValue': 'Transactional'
                    }
                }
            )

            print(f"✅ SMS sent successfully via AWS SNS. MessageId: {response['MessageId']}")
            return True

        except ImportError:
            print("❌ boto3 library not installed. Run: pip install boto3")
            return False
        except Exception as e:
            print(f"❌ AWS SNS SMS failed: {str(e)}")
            return False

    @staticmethod
    def send_otp_sms(to_mobile: str, otp_code: str, user_name: Optional[str] = None) -> bool:
        """
        Send OTP verification SMS.

        Args:
            to_mobile: Recipient mobile number (with country code, e.g., +919876543210)
            otp_code: 6-digit OTP code
            user_name: User's name (optional)

        Returns:
            bool: True if SMS sent successfully, False otherwise
        """
        # Create SMS message
        message = f"""Cricket Auction Platform

Your mobile verification code is: {otp_code}

This code will expire in 5 minutes.

If you didn't request this code, please ignore this message."""

        return SMSService.send_sms(to_mobile, message)

    @staticmethod
    def send_welcome_sms(to_mobile: str, user_name: str) -> bool:
        """
        Send welcome SMS after successful registration.

        Args:
            to_mobile: Recipient mobile number
            user_name: User's name

        Returns:
            bool: True if SMS sent successfully, False otherwise
        """
        message = f"""Welcome {user_name}!

Your Cricket Auction Platform account is now active. Start bidding on your favorite players!

Visit: http://localhost:8000"""

        return SMSService.send_sms(to_mobile, message)
