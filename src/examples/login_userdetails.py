from firstock import firstock

# ---------------------------------------------------------------------------
# Credentials - replace with your actual values
# ---------------------------------------------------------------------------
userId="Your_UserId"
password="Your_password"
totp="Your_totp"
vendorCode="Your Vendor_code"
apiKey="Your_api_key"

# ---------------------------------------------------------------------------
# Step 1: Login
# ---------------------------------------------------------------------------
print("==> Logging in...")

login = firstock.login(
    userId=userId,
    password=password,
    TOTP=totp,
    vendorCode=vendorCode,
    apiKey=apiKey,
)

print("Login successful!")
print("Login Response:", login)

# ---------------------------------------------------------------------------
# Step 2: Fetch User Details
# ---------------------------------------------------------------------------
print("\n==> Fetching user details...")

userDetails = firstock.userDetails(userId=userId)

print("User details fetched successfully!")
print("User Details:", userDetails)