import pyupbit

access = "3fCmuKAoYgzFhxbSApVwCYpGhoH6Ml9zaCcxd8SH"
secret = "WmMPxyz91TNO71m1j4sEK18gpO3SvhIxdCxU6nCP" 
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-BTC"))
print(upbit.get_balance("KRW"))