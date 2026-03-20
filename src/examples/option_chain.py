import json
from firstock import firstock

# ---------------------------------------------------------------------------
# Read userId from config.json (saved during login)
# ---------------------------------------------------------------------------
with open("config.json", "r") as f:
    config = json.load(f)

userId = list(config.keys())[0]
print("Using userId:", userId)

# ---------------------------------------------------------------------------
# Step 1: Get Expiry
# ---------------------------------------------------------------------------
print("\n==> Fetching expiry dates...")

getExpiry = firstock.getExpiry(
    userId=userId,
    exchange="NSE",
    tradingSymbol="NIFTY"
)

print("Expiry Response:", getExpiry)

# Convert expiry from DDMMMYYYY to DDMMMYY format (e.g. 24MAR2026 -> 24MAR26)
raw_expiry = getExpiry["data"]["expiryDates"][0]
expiry = raw_expiry[:-4] + raw_expiry[-2:]
print("Using expiry:", expiry)

# ---------------------------------------------------------------------------
# Step 2: Fetch Option Chain
# ---------------------------------------------------------------------------
print("\n==> Fetching Option Chain...")

optionChain = firstock.optionChain(
    userId=userId,
    exchange="NFO",
    symbol="NIFTY",
    strikePrice="23150",  # Replace with current NIFTY market price
    expiry=expiry,
    count="5"
)

print("Option Chain:", optionChain)