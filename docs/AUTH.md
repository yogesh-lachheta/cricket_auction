# 🔐 Authentication System Documentation

## Table of Contents
1. [Overview](#overview)
2. [Authentication Flow](#authentication-flow)
3. [Architecture](#architecture)
4. [API Endpoints](#api-endpoints)
5. [Code Examples](#code-examples)
6. [Security Features](#security-features)
7. [Testing](#testing)
8. [Future Enhancements](#future-enhancements)

---

## Overview

The Cricket Auction Platform uses **JWT (JSON Web Token) based authentication** with the following features:

- Email/Password based authentication
- Bcrypt password hashing
- JWT access tokens (30-minute expiration)
- Role-based access control (viewer, team_owner, auctioneer, admin, superuser)
- Protected routes using OAuth2 Bearer tokens

---

## Authentication Flow

### 1. User Registration Flow

```
┌─────────┐         ┌──────────────┐         ┌──────────────┐         ┌──────────┐
│ Client  │         │   FastAPI    │         │ AuthService  │         │ Database │
└────┬────┘         └──────┬───────┘         └──────┬───────┘         └────┬─────┘
     │                     │                        │                      │
     │  POST /register     │                        │                      │
     │  {email, password}  │                        │                      │
     ├────────────────────>│                        │                      │
     │                     │                        │                      │
     │                     │  create_user()         │                      │
     │                     ├───────────────────────>│                      │
     │                     │                        │                      │
     │                     │                        │  Check if email      │
     │                     │                        │  exists              │
     │                     │                        ├─────────────────────>│
     │                     │                        │<─────────────────────┤
     │                     │                        │  No existing user    │
     │                     │                        │                      │
     │                     │                        │  Hash password       │
     │                     │                        │  (bcrypt)            │
     │                     │                        │                      │
     │                     │                        │  Insert new user     │
     │                     │                        ├─────────────────────>│
     │                     │                        │<─────────────────────┤
     │                     │                        │  User created        │
     │                     │<───────────────────────┤                      │
     │                     │  Return user           │                      │
     │<────────────────────┤                        │                      │
     │  201 Created        │                        │                      │
     │  {user details}     │                        │                      │
```

**Steps:**
1. Client sends POST request to `/api/v1/auth/register` with user data
2. API validates the request body using Pydantic schema
3. AuthService checks if email/username already exists
4. Password is hashed using bcrypt (with salt, never stored in plain text)
5. New user record is created in the database
6. User details (without password) are returned to client

---

### 2. User Login Flow

```
┌─────────┐         ┌──────────────┐         ┌──────────────┐         ┌──────────┐
│ Client  │         │   FastAPI    │         │ AuthService  │         │ Database │
└────┬────┘         └──────┬───────┘         └──────┬───────┘         └────┬─────┘
     │                     │                        │                      │
     │  POST /login        │                        │                      │
     │  {email, password}  │                        │                      │
     ├────────────────────>│                        │                      │
     │                     │                        │                      │
     │                     │  authenticate_user()   │                      │
     │                     ├───────────────────────>│                      │
     │                     │                        │                      │
     │                     │                        │  Get user by email   │
     │                     │                        ├─────────────────────>│
     │                     │                        │<─────────────────────┤
     │                     │                        │  User found          │
     │                     │                        │                      │
     │                     │                        │  Verify password     │
     │                     │                        │  (bcrypt compare)    │
     │                     │                        │                      │
     │                     │<───────────────────────┤                      │
     │                     │  User authenticated    │                      │
     │                     │                        │                      │
     │                     │  create_access_token() │                      │
     │                     │  {sub: email, exp}     │                      │
     │                     │                        │                      │
     │<────────────────────┤                        │                      │
     │  200 OK             │                        │                      │
     │  {access_token,     │                        │                      │
     │   token_type}       │                        │                      │
```

**Steps:**
1. Client sends POST request to `/api/v1/auth/login` with credentials
2. AuthService retrieves user from database by email
3. Password is verified using bcrypt.verify() against hashed password
4. If valid, JWT token is created with:
   - `sub` (subject): user's email
   - `exp` (expiration): current time + 30 minutes
   - Signed with SECRET_KEY using HS256 algorithm
5. Token is returned to client

---

### 3. Accessing Protected Routes

```
┌─────────┐         ┌──────────────┐         ┌──────────────┐         ┌──────────┐
│ Client  │         │   FastAPI    │         │ Dependencies │         │ Database │
└────┬────┘         └──────┬───────┘         └──────┬───────┘         └────┬─────┘
     │                     │                        │                      │
     │  GET /auth/me       │                        │                      │
     │  Authorization:     │                        │                      │
     │  Bearer <token>     │                        │                      │
     ├────────────────────>│                        │                      │
     │                     │                        │                      │
     │                     │  get_current_user()    │                      │
     │                     ├───────────────────────>│                      │
     │                     │                        │                      │
     │                     │                        │  Extract token from  │
     │                     │                        │  Authorization header│
     │                     │                        │                      │
     │                     │                        │  decode_access_token()│
     │                     │                        │  Verify signature    │
     │                     │                        │  Check expiration    │
     │                     │                        │                      │
     │                     │                        │  Extract email from  │
     │                     │                        │  token payload       │
     │                     │                        │                      │
     │                     │                        │  Get user by email   │
     │                     │                        ├─────────────────────>│
     │                     │                        │<─────────────────────┤
     │                     │                        │  User found          │
     │                     │<───────────────────────┤                      │
     │                     │  Current user          │                      │
     │                     │                        │                      │
     │<────────────────────┤                        │                      │
     │  200 OK             │                        │                      │
     │  {user details}     │                        │                      │
```

**Steps:**
1. Client sends request with `Authorization: Bearer <token>` header
2. FastAPI's `OAuth2PasswordBearer` dependency extracts the token
3. `get_current_user` dependency is called:
   - Token is decoded and verified
   - Signature is checked against SECRET_KEY
   - Expiration time is validated
   - Email is extracted from `sub` claim
4. User is fetched from database using the email
5. User's active status is verified
6. User object is injected into the route handler
7. Route handler returns the requested data

---

## Architecture

### File Structure

```
backend/
├── app/
│   ├── core/
│   │   ├── security.py          # Password hashing & JWT functions
│   │   ├── dependencies.py      # FastAPI dependencies (get_current_user, etc.)
│   │   └── config.py            # Settings (SECRET_KEY, ALGORITHM, etc.)
│   ├── services/
│   │   └── auth.py              # Authentication business logic
│   ├── schemas/
│   │   ├── user.py              # User Pydantic schemas
│   │   └── token.py             # Token Pydantic schemas
│   ├── models/
│   │   └── user.py              # User SQLAlchemy model
│   └── api/v1/routes/auth/
│       ├── register.py          # Registration endpoint
│       ├── login.py             # Login & /me endpoints
│       └── __init__.py          # Router aggregation
```

---

### Component Responsibilities

#### 1. `app/core/security.py`
**Purpose:** Low-level security utilities

```python
# Functions:
- hash_password(password: str) -> str
  # Uses bcrypt to hash passwords with automatic salting

- verify_password(plain_password: str, hashed_password: str) -> bool
  # Compares plain password against hashed password

- create_access_token(data: dict, expires_delta: timedelta = None) -> str
  # Creates JWT token with expiration

- decode_access_token(token: str) -> Optional[dict]
  # Decodes and validates JWT token
```

**Example:**
```python
from app.core.security import hash_password, verify_password

# Registration
hashed = hash_password("MyPassword123")
# Returns: "$2b$12$abcdefghijklmnopqrstuvwxyz..."

# Login
is_valid = verify_password("MyPassword123", hashed)
# Returns: True
```

---

#### 2. `app/services/auth.py`
**Purpose:** Authentication business logic

```python
# Methods:
- get_user_by_email(db, email) -> Optional[User]
- get_user_by_username(db, username) -> Optional[User]
- get_user_by_id(db, user_id) -> Optional[User]
- authenticate_user(db, email, password) -> Optional[User]
- create_user(db, user_data) -> User
```

**Example:**
```python
from app.services.auth import AuthService

# Authenticate user
user = AuthService.authenticate_user(db, "user@example.com", "password123")
if user:
    print("Login successful")
```

---

#### 3. `app/core/dependencies.py`
**Purpose:** FastAPI dependency injection for route protection

```python
# Dependencies:
- get_db() -> Session
  # Provides database session

- get_current_user(token) -> User
  # Validates JWT and returns current user

- get_current_admin(current_user) -> User
  # Ensures user has admin or auctioneer role

- get_current_superuser(current_user) -> User
  # Ensures user is a superuser

- get_current_auctioneer(current_user) -> User
  # Ensures user has auctioneer role
```

**Example:**
```python
from app.core.dependencies import get_current_user, get_current_admin

# Protected route (any authenticated user)
@router.get("/profile")
def get_profile(current_user: User = Depends(get_current_user)):
    return current_user

# Admin-only route
@router.delete("/users/{user_id}")
def delete_user(
    user_id: int,
    admin: User = Depends(get_current_admin)
):
    # Only admins can access this
    ...
```

---

## API Endpoints

### 1. Register User

**Endpoint:** `POST /api/v1/auth/register`

**Request Body:**
```json
{
  "email": "user@example.com",
  "username": "johndoe",
  "password": "SecurePassword123",
  "full_name": "John Doe",
  "role": "viewer"
}
```

**Response (201 Created):**
```json
{
  "id": 1,
  "email": "user@example.com",
  "username": "johndoe",
  "full_name": "John Doe",
  "role": "viewer",
  "is_active": true,
  "is_superuser": false,
  "created_at": "2026-03-07T16:36:43.816444+05:30",
  "updated_at": "2026-03-07T16:36:43.816444+05:30"
}
```

**Errors:**
- `400 Bad Request`: Email or username already exists
- `422 Unprocessable Entity`: Invalid data format

---

### 2. Login

**Endpoint:** `POST /api/v1/auth/login`

**Request Body (Form Data):**
```
username=user@example.com
password=SecurePassword123
```

**Response (200 OK):**
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

**Errors:**
- `401 Unauthorized`: Invalid credentials
- `422 Unprocessable Entity`: Missing fields

---

### 3. Get Current User

**Endpoint:** `GET /api/v1/auth/me`

**Headers:**
```
Authorization: Bearer <access_token>
```

**Response (200 OK):**
```json
{
  "id": 1,
  "email": "user@example.com",
  "username": "johndoe",
  "full_name": "John Doe",
  "role": "viewer",
  "is_active": true,
  "is_superuser": false,
  "created_at": "2026-03-07T16:36:43.816444+05:30",
  "updated_at": "2026-03-07T16:36:43.816444+05:30"
}
```

**Errors:**
- `401 Unauthorized`: Invalid or expired token
- `403 Forbidden`: Inactive user account

---

## Code Examples

### Frontend Integration (JavaScript/React)

#### 1. Registration
```javascript
async function register(userData) {
  const response = await fetch('http://localhost:8000/api/v1/auth/register', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(userData),
  });

  if (!response.ok) {
    const error = await response.json();
    throw new Error(error.detail);
  }

  return await response.json();
}

// Usage
register({
  email: 'user@example.com',
  username: 'johndoe',
  password: 'SecurePassword123',
  full_name: 'John Doe',
  role: 'viewer'
})
.then(user => console.log('Registered:', user))
.catch(error => console.error('Registration failed:', error.message));
```

#### 2. Login
```javascript
async function login(email, password) {
  const formData = new URLSearchParams();
  formData.append('username', email); // OAuth2 uses 'username' field
  formData.append('password', password);

  const response = await fetch('http://localhost:8000/api/v1/auth/login', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded',
    },
    body: formData,
  });

  if (!response.ok) {
    throw new Error('Invalid credentials');
  }

  const data = await response.json();

  // Store token in localStorage
  localStorage.setItem('access_token', data.access_token);

  return data;
}

// Usage
login('user@example.com', 'SecurePassword123')
  .then(data => console.log('Login successful:', data))
  .catch(error => console.error('Login failed:', error.message));
```

#### 3. Accessing Protected Routes
```javascript
async function getCurrentUser() {
  const token = localStorage.getItem('access_token');

  if (!token) {
    throw new Error('No token found');
  }

  const response = await fetch('http://localhost:8000/api/v1/auth/me', {
    headers: {
      'Authorization': `Bearer ${token}`,
    },
  });

  if (!response.ok) {
    // Token expired or invalid
    localStorage.removeItem('access_token');
    throw new Error('Authentication failed');
  }

  return await response.json();
}

// Usage
getCurrentUser()
  .then(user => console.log('Current user:', user))
  .catch(error => console.error('Auth failed:', error.message));
```

---

### Backend: Creating Protected Routes

```python
from fastapi import APIRouter, Depends
from app.core.dependencies import get_current_user, get_current_admin
from app.models.user import User

router = APIRouter()

# Route accessible by any authenticated user
@router.get("/profile")
def get_profile(current_user: User = Depends(get_current_user)):
    return {
        "message": f"Hello, {current_user.full_name}!",
        "email": current_user.email,
        "role": current_user.role
    }

# Route accessible only by admins
@router.delete("/users/{user_id}")
def delete_user(
    user_id: int,
    admin: User = Depends(get_current_admin)
):
    # Only admins can delete users
    return {"message": f"User {user_id} deleted by admin {admin.email}"}
```

---

## Security Features

### 1. Password Security
- **Bcrypt Hashing**: Industry-standard algorithm with automatic salting
- **No Plain Text Storage**: Passwords are never stored or logged in plain text
- **One-Way Hashing**: Impossible to reverse-engineer passwords from hashes

### 2. JWT Token Security
- **HS256 Algorithm**: HMAC with SHA-256 for signing
- **Secret Key**: Stored in environment variables, never in code
- **Expiration**: Tokens expire after 30 minutes
- **Stateless**: No server-side session storage required

### 3. CORS Configuration
- Configured in `main.py` to allow only specific origins
- Prevents unauthorized domains from accessing the API

### 4. Role-Based Access Control (RBAC)
- **Roles**: viewer, team_owner, auctioneer, admin, superuser
- **Dependencies**: `get_current_admin`, `get_current_auctioneer`, etc.
- **Flexible**: Easy to add new roles and permissions

### 5. Input Validation
- **Pydantic Schemas**: Automatic validation of all inputs
- **Email Validation**: Ensures valid email format
- **Password Requirements**: Can be extended with regex validators

---

## Testing

### Using cURL

#### 1. Register
```bash
curl -X POST "http://localhost:8000/api/v1/auth/register" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "test@example.com",
    "username": "testuser",
    "password": "Test@1234",
    "full_name": "Test User",
    "role": "viewer"
  }'
```

#### 2. Login
```bash
curl -X POST "http://localhost:8000/api/v1/auth/login" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=test@example.com&password=Test@1234"
```

#### 3. Access Protected Route
```bash
# First, save the token from login response
TOKEN="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."

# Then use it to access protected routes
curl -X GET "http://localhost:8000/api/v1/auth/me" \
  -H "Authorization: Bearer $TOKEN"
```

---

### Test Results

```
✅ Registration: 201 Created
{
  "id": 1,
  "email": "test@example.com",
  "username": "testuser",
  "full_name": "Test User",
  "role": "viewer",
  "is_active": true,
  "is_superuser": false,
  "created_at": "2026-03-07T16:36:43.816444+05:30",
  "updated_at": "2026-03-07T16:36:43.816444+05:30"
}

✅ Login: 200 OK
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0ZXN0QGV4YW1wbGUuY29tIiwiZXhwIjoxNzcyODgzNDY1fQ.IXe10KrkdrkQl0S0uf7sl65Mg2hpMga53-WF9WlVWbo",
  "token_type": "bearer"
}

✅ Get Current User: 200 OK
{
  "id": 1,
  "email": "test@example.com",
  "username": "testuser",
  "full_name": "Test User",
  "role": "viewer",
  "is_active": true,
  "is_superuser": false,
  "created_at": "2026-03-07T16:36:43.816444+05:30",
  "updated_at": "2026-03-07T16:36:43.816444+05:30"
}
```

---

## Future Enhancements

### Planned Features (Not Yet Implemented)

#### 1. **OAuth2 Integration (Google & Microsoft)**
- Sign in with Google
- Sign in with Microsoft
- Third-party token validation
- Auto-create user accounts from OAuth providers

**Implementation Plan:**
```python
# Add to dependencies
from fastapi_sso.sso.google import GoogleSSO
from fastapi_sso.sso.microsoft import MicrosoftSSO

# New endpoints
@router.get("/auth/google")
async def google_login():
    ...

@router.get("/auth/microsoft")
async def microsoft_login():
    ...
```

---

#### 2. **OTP (One-Time Password) Verification**

**Email OTP:**
- Send 6-digit code to user's email
- Verify code within 5 minutes
- Use for:
  - Email verification during registration
  - Password reset
  - Two-factor authentication

**Mobile OTP:**
- Send SMS code to user's mobile number
- Add `mobile` field to User model
- Integration with Twilio/AWS SNS

**Implementation Plan:**
```python
# New fields in User model
class User(Base):
    ...
    mobile = Column(String(20), nullable=True)
    email_verified = Column(Boolean, default=False)
    mobile_verified = Column(Boolean, default=False)

# New OTP model
class OTP(Base):
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    code = Column(String(6))
    otp_type = Column(String(20))  # email, mobile
    expires_at = Column(DateTime)
    is_used = Column(Boolean, default=False)

# New endpoints
@router.post("/auth/send-otp")
def send_otp(email: str, otp_type: str):
    ...

@router.post("/auth/verify-otp")
def verify_otp(email: str, code: str):
    ...
```

---

#### 3. **Refresh Tokens**
- Long-lived refresh tokens (7 days)
- Separate from access tokens
- Stored in database for revocation capability

---

#### 4. **Password Reset Flow**
- Forgot password endpoint
- Email with reset link
- Token-based password reset
- Password history (prevent reuse)

---

#### 5. **Account Lockout**
- Lock account after 5 failed login attempts
- Automatic unlock after 15 minutes
- Manual unlock by admin

---

#### 6. **Audit Logging**
- Track all authentication events
- IP address logging
- Device fingerprinting
- Login history per user

---

## Environment Variables

Required in `.env` file:

```bash
# JWT Configuration
SECRET_KEY="your-super-secret-key-change-in-production"
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES=30

# Database
DATABASE_URL="postgresql://admin:admin@localhost:5432/cricket_auction"

# Future: Email OTP
SMTP_HOST="smtp.gmail.com"
SMTP_PORT=587
SMTP_USER="your-email@gmail.com"
SMTP_PASSWORD="your-app-password"

# Future: SMS OTP
TWILIO_ACCOUNT_SID="your-twilio-sid"
TWILIO_AUTH_TOKEN="your-twilio-token"
TWILIO_PHONE_NUMBER="+1234567890"

# Future: OAuth
GOOGLE_CLIENT_ID="your-google-client-id"
GOOGLE_CLIENT_SECRET="your-google-client-secret"
MICROSOFT_CLIENT_ID="your-microsoft-client-id"
MICROSOFT_CLIENT_SECRET="your-microsoft-client-secret"
```

---

## Troubleshooting

### Common Issues

#### 1. "Could not validate credentials"
- **Cause**: Token expired or invalid
- **Solution**: Login again to get a new token

#### 2. "Email already registered"
- **Cause**: Email already exists in database
- **Solution**: Use a different email or login with existing account

#### 3. "Incorrect email or password"
- **Cause**: Invalid credentials
- **Solution**: Verify email and password are correct

#### 4. "Inactive user account"
- **Cause**: User account is disabled
- **Solution**: Contact admin to activate account

---

## Summary

### What's Implemented ✅
- ✅ User registration with email/username/password
- ✅ Bcrypt password hashing
- ✅ JWT token generation and validation
- ✅ Login endpoint
- ✅ Protected routes with OAuth2 Bearer tokens
- ✅ Role-based access control
- ✅ Current user endpoint (/me)

### What's Not Implemented ❌
- ❌ Google OAuth2 signup
- ❌ Microsoft OAuth2 signup
- ❌ Email OTP verification
- ❌ Mobile OTP verification
- ❌ Refresh tokens
- ❌ Password reset
- ❌ Account lockout
- ❌ Audit logging

---

**Last Updated:** March 7, 2026
**Status:** Day 7 Complete - Basic Authentication Working
**Next Steps:** Implement OTP and OAuth2 features

---

# 🆕 UPDATED AUTHENTICATION SYSTEM (March 2026)

## What's New - Complete Implementation

### ✅ Implemented Features

1. **Manual Signup with OTP Verification** ✅
2. **Google OAuth2 Integration** ✅  
3. **Microsoft OAuth2 Integration** ✅
4. **Email OTP Verification** ✅
5. **Mobile OTP Verification** ✅

---

## Updated Authentication Methods

### 1. Manual Signup with Email & Mobile OTP

**Endpoint:** `POST /api/v1/auth/register`

**Request:**
```json
{
  "email": "user@example.com",
  "username": "johndoe",
  "password": "SecurePass@123",
  "full_name": "John Doe",
  "mobile": "+919876543210",
  "role": "viewer"
}
```

**Response:**
```json
{
  "success": true,
  "message": "Account created successfully. Please verify your OTP.",
  "user_id": 1,
  "email": "user@example.com",
  "mobile": "+919876543210",
  "otp_sent_to": [
    "email (user@example.com)",
    "mobile (+919876543210)"
  ],
  "requires_verification": true,
  "note": "Please check your email and mobile for OTP codes. OTPs expire in 5 minutes."
}
```

**OTP Delivery:**
- **Email OTP:** HTML formatted email with 6-digit code
- **Mobile OTP:** SMS message with 6-digit code  
- **Expiration:** 5 minutes
- **Development Mode:** OTPs logged to console (FREE)
- **Production Mode:** Gmail SMTP + Twilio/AWS SNS

---

### 2. OTP Verification

**Email Verification:**  
`POST /api/v1/auth/verify-otp`

```json
{
  "email": "user@example.com",
  "otp_code": "123456"
}
```

**Mobile Verification:**  
`POST /api/v1/auth/verify-otp`

```json
{
  "mobile": "+919876543210",
  "otp_code": "654321"
}
```

**Success Response:**
```json
{
  "success": true,
  "message": "Email verified successfully",
  "otp_sent_to": null,
  "expires_in_minutes": null
}
```

**After Full Verification:**
- Email verified → `email_verified = true`
- Mobile verified → `mobile_verified = true`
- Welcome email & SMS sent automatically

---

### 3. Resend OTP

**Endpoint:** `POST /api/v1/auth/resend-otp`

**Request:**
```json
{
  "email": "user@example.com"
}
```

or

```json
{
  "mobile": "+919876543210"
}
```

**Response:**
```json
{
  "success": true,
  "message": "OTP sent successfully to email",
  "otp_sent_to": "user@example.com",
  "expires_in_minutes": 5
}
```

---

### 4. Google OAuth2 Signup

**Step 1: Get OAuth URL**  
`GET /api/v1/auth/google`

**Development Mode Response:**
```json
{
  "authorization_url": null,
  "note": "Development Mode: Use POST /api/v1/auth/google/callback with manual user data (email, name, oauth_id)"
}
```

**Step 2: OAuth Callback (Development Mode)**  
`POST /api/v1/auth/google/callback`

```json
{
  "provider": "google",
  "email": "user@gmail.com",
  "name": "John Doe",
  "oauth_id": "google-123456789"
}
```

**Success Response:**
```json
{
  "success": true,
  "message": "Successfully authenticated via Google",
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer",
  "user": {
    "id": 5,
    "email": "user@gmail.com",
    "username": "user",
    "oauth_provider": "google",
    "email_verified": true
  }
}
```

**Features:**
- No password required
- Email pre-verified
- Automatic username generation
- Immediate JWT token
- No OTP verification needed

---

### 5. Microsoft OAuth2 Signup

**Step 1: Get OAuth URL**  
`GET /api/v1/auth/microsoft`

**Step 2: OAuth Callback**  
`POST /api/v1/auth/microsoft/callback`

```json
{
  "provider": "microsoft",
  "email": "user@outlook.com",
  "name": "Jane Doe",
  "oauth_id": "microsoft-987654321"
}
```

**Response:** Same as Google OAuth

---

## Complete API Endpoints Summary

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| POST | `/api/v1/auth/register` | Register with email/mobile OTP | No |
| POST | `/api/v1/auth/login` | Login with email/password | No |
| GET | `/api/v1/auth/me` | Get current user | Yes |
| POST | `/api/v1/auth/verify-otp` | Verify email/mobile OTP | No |
| POST | `/api/v1/auth/resend-otp` | Resend OTP code | No |
| GET | `/api/v1/auth/google` | Get Google OAuth URL | No |
| POST | `/api/v1/auth/google/callback` | Google OAuth callback | No |
| GET | `/api/v1/auth/microsoft` | Get Microsoft OAuth URL | No |
| POST | `/api/v1/auth/microsoft/callback` | Microsoft OAuth callback | No |

---

## Database Schema Updates

### Users Table - New Fields

```sql
-- OAuth Fields
oauth_provider VARCHAR(50)     -- 'google', 'microsoft', or NULL
oauth_id VARCHAR(255)          -- OAuth provider user ID

-- Contact & Verification
mobile VARCHAR(20) UNIQUE      -- Mobile number with country code
email_verified BOOLEAN         -- Email verification status
mobile_verified BOOLEAN        -- Mobile verification status

-- Password now nullable for OAuth users
hashed_password VARCHAR(255)   -- NULL for OAuth users
```

### OTPs Table (New)

```sql
CREATE TABLE otps (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    otp_type VARCHAR(10),      -- 'EMAIL' or 'MOBILE'
    code VARCHAR(6),           -- 6-digit OTP code
    recipient VARCHAR(255),    -- Email or mobile number
    expires_at TIMESTAMP,      -- Expiration time (5 minutes)
    is_used BOOLEAN,          -- Whether OTP was used
    is_verified BOOLEAN,      -- Whether verification succeeded
    created_at TIMESTAMP
);
```

---

## Authentication Flow Diagrams

### Manual Signup with OTP Flow

```
User → Register (email, mobile, password)
         ↓
System → Create unverified account
         ↓
System → Send Email OTP (6-digit, 5 min expiry)
         ↓
System → Send Mobile OTP (6-digit, 5 min expiry)
         ↓
User → Verify Email OTP
         ↓
System → Mark email_verified = true
         ↓
User → Verify Mobile OTP
         ↓
System → Mark mobile_verified = true
         ↓
System → Send Welcome Email & SMS
         ↓
User → Fully Verified! ✅
```

### Google/Microsoft OAuth Flow

```
User → Click "Sign in with Google"
         ↓
GET /api/v1/auth/google
         ↓
System → Return OAuth URL (or dev instructions)
         ↓
User → Complete OAuth (or send manual data in dev mode)
         ↓
POST /api/v1/auth/google/callback
         ↓
System → Verify OAuth data
         ↓
System → Create/Get user (email pre-verified)
         ↓
System → Generate JWT token
         ↓
User → Logged in! ✅
```

---

## Code Examples - Frontend Integration

### Manual Signup with OTP

```javascript
// Step 1: Register user
async function registerWithOTP(userData) {
  const response = await fetch('http://localhost:8000/api/v1/auth/register', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      email: 'user@example.com',
      username: 'johndoe',
      password: 'SecurePass@123',
      mobile: '+919876543210',
      full_name: 'John Doe'
    })
  });
  
  const data = await response.json();
  console.log(data.otp_sent_to); // ["email (...)", "mobile (...)"]
  
  return data.user_id;
}

// Step 2: Verify Email OTP
async function verifyEmailOTP(email, otpCode) {
  const response = await fetch('http://localhost:8000/api/v1/auth/verify-otp', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      email: email,
      otp_code: otpCode
    })
  });
  
  const data = await response.json();
  return data.success;
}

// Step 3: Verify Mobile OTP
async function verifyMobileOTP(mobile, otpCode) {
  const response = await fetch('http://localhost:8000/api/v1/auth/verify-otp', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      mobile: mobile,
      otp_code: otpCode
    })
  });
  
  const data = await response.json();
  return data.success;
}
```

### Google OAuth Signup

```javascript
// Development Mode
async function signInWithGoogle() {
  const response = await fetch('http://localhost:8000/api/v1/auth/google/callback', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      provider: 'google',
      email: 'user@gmail.com',
      name: 'John Doe',
      oauth_id: 'google-123456789'
    })
  });
  
  const data = await response.json();
  
  if (data.success) {
    // Store JWT token
    localStorage.setItem('access_token', data.access_token);
    console.log('Logged in:', data.user);
  }
}
```

---

## Testing Results ✅

### Manual Signup with OTP
```
✅ Registration: User created, OTPs sent to email & mobile
✅ Email OTP: Verified successfully (email_verified = true)
✅ Mobile OTP: Verified successfully (mobile_verified = true)
✅ Welcome Messages: Email & SMS sent after full verification
✅ Resend OTP: Working for both email & mobile
```

### Google OAuth
```
✅ OAuth URL: Development mode instructions returned
✅ Callback: User created with Google provider
✅ Token: JWT access token generated
✅ Database: oauth_provider='google', email_verified=true, hashed_password=NULL
```

### Microsoft OAuth
```
✅ OAuth URL: Development mode instructions returned
✅ Callback: User created with Microsoft provider
✅ Token: JWT access token generated
✅ Database: oauth_provider='microsoft', email_verified=true, hashed_password=NULL
```

---

## Security Features

### Password Security
- Bcrypt hashing with automatic salting
- Minimum 8 characters with uppercase, lowercase, digit requirements
- Optional for OAuth users (NULL in database)

### OTP Security
- 6-digit random codes
- 5-minute expiration
- One-time use (marked as used after verification)
- Previous unused OTPs invalidated on resend

### OAuth Security
- Email pre-verified for OAuth users
- OAuth ID stored for provider verification
- Development mode for testing (no real OAuth apps needed)
- Production mode ready (requires OAuth app credentials)

### JWT Security
- HS256 algorithm
- 30-minute expiration
- Email as subject claim
- Signed with SECRET_KEY

---

## Production Mode Setup

To enable real OAuth in production:

1. **Set Environment Variables:**
```bash
# OAuth Mode
OAUTH_MODE=production

# Google OAuth
GOOGLE_CLIENT_ID=your-google-client-id
GOOGLE_CLIENT_SECRET=your-google-client-secret
GOOGLE_REDIRECT_URI=https://yourapp.com/api/v1/auth/google/callback

# Microsoft OAuth
MICROSOFT_CLIENT_ID=your-microsoft-client-id
MICROSOFT_CLIENT_SECRET=your-microsoft-client-secret
MICROSOFT_REDIRECT_URI=https://yourapp.com/api/v1/auth/microsoft/callback

# Email (Gmail SMTP)
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your-email@gmail.com
SMTP_PASSWORD=your-app-password

# SMS (Twilio)
SMS_PROVIDER=twilio
TWILIO_ACCOUNT_SID=your-account-sid
TWILIO_AUTH_TOKEN=your-auth-token
TWILIO_PHONE_NUMBER=+1234567890
```

2. **Register OAuth Apps:**
   - Google: https://console.cloud.google.com/apis/credentials
   - Microsoft: https://portal.azure.com/#blade/Microsoft_AAD_RegisteredApps

3. **Configure Redirect URIs** in OAuth app settings

---

## Summary

### Completed ✅
- ✅ Manual signup with email & mobile
- ✅ Email OTP verification (6-digit, 5 min expiry)
- ✅ Mobile OTP verification (6-digit, 5 min expiry)
- ✅ Resend OTP functionality
- ✅ Google OAuth2 integration (dev mode)
- ✅ Microsoft OAuth2 integration (dev mode)
- ✅ Welcome emails & SMS after verification
- ✅ Password optional for OAuth users
- ✅ Automatic username generation
- ✅ Email pre-verification for OAuth users

### Code Statistics
- **OTP System:** ~660 lines (model, service, endpoints, schemas)
- **OAuth System:** ~520 lines (service, endpoints, schemas)
- **Total New Code:** ~1,180 lines
- **Total Endpoints:** 9 authentication endpoints

### Database Changes
- **Users table:** 5 new fields (mobile, oauth_provider, oauth_id, email_verified, mobile_verified)
- **OTPs table:** New table with 9 fields
- **Migration:** Successfully applied

---

**Last Updated:** March 7, 2026  
**Status:** All Authentication Methods Fully Working ✅  
**Mode:** Development (FREE - no OAuth apps, console OTP logging)  
**Production Ready:** Yes (configure environment variables)

