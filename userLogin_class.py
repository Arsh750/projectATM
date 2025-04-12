from datetime import datetime, timedelta
from userClass import user_Obj
class userLogin:
    def __init__(self,user_Obj):
        self.user = user_Obj
        self.lastLogin_time = None
        self.loginCreated_at = datetime.now()
        self.session_active = False
        self.otp_value = None
        self.otp_created_at = None
    
    def cid(self):
        return self.user.cid()
    
    def cUsername(self):
        return self.user.username
    
    def cPassword(self):
        return self.user.password
    
    def lastLogin(self):
        return f"Last Login: {self.lastLogin_time}" if self.lastLogin_time else "No previous Login recorded"

    def loginCreated(self):
        # app.logger.info(f"Login Created: {self.loginCreated_at}")
        return f"Login Created: {self.loginCreated_at.strftime('%Y-%m-%d %H:%M:%S')}"

    def isSession(self):
        return f"Session Active: {self.session_active}"

    def ttl(self,expiration_minutes = 30):
        if self.lastLogin_time is None:
            return "Error: no login time recorded"
        expiration_time = self.lastLogin_time + timedelta(minutes = expiration_minutes)
        return max((expiration_time - datetime.now()).total_seconds(),0)   

    def otp(self):
        import random
        self.otp_value = random.randint(100000,999999)
        self.otp_created_at = datetime.now()
        return f"Generated OTP: {self.otp_value}"

    def otpCreated(self):
        if self.otp_created_at:
            return f"OTP Created At: {self.otp_created_at.strftime('%Y-%m-%d %H:%M:%S')}"
        return "OTP not generated yet"

    def otp_ttl(self,otp_validity_minutes=5):
        if self.otp_created_at:
            expiration_time = self.otp_created_at + timedelta(minutes = otp_validity_minutes)
            return max((expiration_time - datetime.now()).total_seconds(),0)
        return 0
    
    
    
login = userLogin(user_Obj)

# Access login details
print(login.cid())
print(login.cUsername())
print(login.cPassword())
print(login.lastLogin())
print(login.loginCreated())
print(login.isSession())

# Simulate login
login.last_login_time = datetime.now()
login.session_active = True

print("Session TTL (seconds):", login.ttl())

# OTP generation
print(login.otp())
print(login.otpCreated())
print("OTP TTL (seconds):", login.otp_ttl())

        