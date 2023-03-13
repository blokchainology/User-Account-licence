from datetime import datetime , timedelta

# Your Account Setting
Licence = ['ProPlus' , 'Pro']

def Active(licenceDays , userLicence):
    if userLicence == Licence[0]:
        print(userLicence)
        licenceStart = datetime.now()
        licenceEnd   = licenceStart + timedelta(days=licenceDays)
        print(licenceEnd)
        print(licenceStart)
        licenceLeftOver = licenceEnd - licenceStart
        print(f"{licenceLeftOver.days} Days Left")
    elif userLicence == Licence[1]:
        print(userLicence)
        licenceStart = datetime.now()
        licenceEnd   = licenceStart + timedelta(days=licenceDays)
        print(licenceEnd)
        print(licenceStart)
        licenceLeftOver = licenceEnd - licenceStart
        print(f"{licenceLeftOver.days} Days Left")
    else:
        print(userLicence)
        licenceStart = datetime.now()
        licenceEnd   = licenceStart + timedelta(days=30)
        print(licenceEnd)
        print(licenceStart)
        licenceLeftOver = licenceEnd - licenceStart
        print(f"{licenceLeftOver.days} Days Left")
        


# Active(Int , Str)
# Active(Days , Account Setting)
Active(24 , 'ProPlus')
