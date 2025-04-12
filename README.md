# REQuirement
## ATM
### Requirement
- [] Get statement
- [] Check balance
- [] Login/Logut (Last thing to integrate with UI)
- [] Transactio(Debit, Credit)
- [] Generate OTP
- [] Futurer extension
    - [] Register of Users

### Integrate with Persistence
 - [] File based
 - [] DB setup

### Entities
- [] User(cid, type,name,description, cif, ifsc, address, created_at)
- [] UserLogin(cid, cUserNname, cPassword, last_login, login_created, isSession, ttl, otp, otp_created, otp_ttl=Max5min)
- [] Account(cid, balance, status, Cards)
- [] UPI(upi_id, cid)
- [] Transaction(tid, cid, trnx_type[debit/credit], trnx_amt,remarks, trnx_time_at)

- [] User_Transaction(cid, tid, trx_time) {1U -> *T}



- [] User_Account(cid, balance)
- [] Cards[card_id, car_type]

- [] Country(name, region) 
- [] State(name, Country)
- [] City(name, State)

### REST API
- [] /miniStatement?month=n ('n' denote last n month to get statement)
- [] /checkBalance
- [] /login and /logout
- [] /transaction
    REQUEST:
    {
        "amount":XXX,
        "from":"source",
        "to":"target",
        "upiId": XXX@xxx,
        "type":"DEBIT/CREDIT",
        "remarks":"note/remark"
    }
    RESPONSE:
    {
        "message":"Success/Failed",
        "status":200/408/500,
        "desctiption":"Tranx complte/Error message",
        "transactionId":"XXXXXX/null"
    }
 - [] /generateOTP?cid=XXX
 - [] /validateOTP
    REQ
    {
        "cid": XXX,
        "otp": Zkafhuhkfk
    }
    RES
    {
    status:"200/400",
    message:"Successfully validate/Wrong OTP"
    }