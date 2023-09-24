# Simple Django Email Authentication System

![Django Version](https://img.shields.io/badge/Django-4.2-brightgreen.svg)

A straightforward and secure Django-based email authentication system with built-in features for password recovery through Gmail and account activation via Gmail. This system is designed to simplify user authentication for your web application while providing robust security and a seamless user experience.

![Demo](demo.gif)

## Features

- **User Registration**: Register user accounts with email addresses and secure passwords.

- **Email Verification**: Verify user emails through email confirmation links.

- **Account Activation**: Activate accounts via email links for added security.

- **Password Reset**: Reset forgotten passwords conveniently via email.

- **User Profile**: Customize user profiles with optional additional information.

- **Gmail Integration**: Seamless integration with Gmail for sending verification and password reset emails.

## Getting Started

To integrate this email authentication system into your Django project, follow these simple steps:

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/shahpankaj123/OTP-based-Authentication-System-in-Django 
   ```

2. Navigate to the project directory:

   ```bash
   cd OTP-based-Authentication-System-in-Django 
   ```

3. Create a virtual environment and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

4. Install project dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Configure your Gmail SMTP credentials by creating a `.env` file in the project root:

   ```env
   EMAIL_HOST_USER=your-email@gmail.com
   EMAIL_HOST_PASSWORD=your-password
   ```

6. Apply database migrations:

   ```bash
   python manage.py migrate
   ```

7. Start the development server:

   ```bash
   python manage.py runserver
   ```

8. Access your application at [http://localhost:8000](http://localhost:8000) in your web browser.

## Usage

1. **User Registration**: Register a new account with your email and password.

2. **Email Verification**: Click the email verification link sent to your registered email address. Check your spam folder if you don't receive the email.

3. **Account Activation**: Log in with your registered email and password.

4. **Password Reset**: If you forget your password, use the "Forgot Password?" link on the login page. You will receive an email with instructions on how to reset your password.

5. **User Profile**: If your application requires additional user information, customize the user profile as needed.

## Configuration

This system can be easily customized to meet your project's specific requirements. Some configuration options include:

- **Additional User Fields**: Add more fields to the user profile to store extra information.

- **Email Templates**: Modify email templates for account activation and password reset.

- **Two-Factor Authentication (2FA)**: Enhance security by implementing 2FA.

- **Email Providers**: Integrate with other email providers besides Gmail.

Please refer to the Django documentation for comprehensive customization guidance.

## Contributing

We welcome contributions to improve this email authentication system. To contribute:

1. Fork the repository.

2. Create a new branch for your feature or bug fix:

   ```bash
   git checkout -b feature-name
   ```

3. Make your changes and commit them:

   ```bash
   git commit -m "Add feature/fix"
   ```

4. Push your branch to your fork:

   ```bash
   git push origin feature-name
   ```

5. Create a pull request on the original repository.



---

Feel free to open issues if you have any questions or encounter any problems while using this Simple Django Email Authentication System. Enjoy simplified and secure user authentication in your web application!
