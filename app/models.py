# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Academiclevel(models.Model):
    academiclevelid = models.AutoField(db_column='academicLevelId', primary_key=True)  # Field name made lowercase.
    name = models.CharField(unique=True, max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'AcademicLevel'


class Address(models.Model):
    addressid = models.AutoField(db_column='addressId', primary_key=True)  # Field name made lowercase.
    user_userid = models.ForeignKey('User', models.DO_NOTHING, db_column='User_userId')  # Field name made lowercase.
    addressnametype = models.CharField(db_column='addressNameType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(max_length=255, blank=True, null=True)
    city_addresscityid = models.IntegerField(db_column='City_addressCityId')  # Field name made lowercase.
    addressinfoadditional = models.CharField(db_column='addressInfoAdditional', max_length=255, blank=True, null=True)  # Field name made lowercase.
    longitude = models.CharField(max_length=10, blank=True, null=True)
    latitude = models.CharField(max_length=10, blank=True, null=True)
    pluscodes = models.CharField(db_column='plusCodes', max_length=10, blank=True, null=True)  # Field name made lowercase.
    statusaddress_statusaddressid = models.ForeignKey('Statusaddress', models.DO_NOTHING, db_column='StatusAddress_statusAddressId')  # Field name made lowercase.
    createdat = models.IntegerField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Address'


class Ambulancetogoservice(models.Model):
    idambulancetogoservice = models.AutoField(db_column='idAmbulanceToGoService', primary_key=True)  # Field name made lowercase.
    ambulancetogoserviceaddress = models.CharField(db_column='AmbulanceToGoServiceAddress', max_length=128, blank=True, null=True)  # Field name made lowercase.
    ambulancetogoserviceuserphone = models.CharField(db_column='AmbulanceToGoServiceUserPhone', max_length=45, blank=True, null=True)  # Field name made lowercase.
    diasnoticimagesserviceusername = models.CharField(db_column='diasnoticImagesServiceUserName', max_length=80, blank=True, null=True)  # Field name made lowercase.
    diasnoticimagesserviceemail = models.CharField(db_column='diasnoticImagesServiceEmail', max_length=128, blank=True, null=True)  # Field name made lowercase.
    diasnoticimagesservicevalue = models.CharField(db_column='diasnoticImagesServiceValue', max_length=45, blank=True, null=True)  # Field name made lowercase.
    ambulancetogoserviceplan_idambulancetogo = models.ForeignKey('Ambulancetogoserviceplan', models.DO_NOTHING, db_column='AmbulanceToGoServicePlan_idAmbulanceToGo')  # Field name made lowercase.
    ambulancetogoserviceuserid = models.ForeignKey('User', models.DO_NOTHING, db_column='AmbulanceToGoServiceUserId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AmbulanceToGoService'


class Ambulancetogoserviceplan(models.Model):
    idambulancetogo = models.AutoField(db_column='idAmbulanceToGo', primary_key=True)  # Field name made lowercase.
    ambulancetogoservicename = models.CharField(db_column='AmbulanceToGoServiceName', max_length=45, blank=True, null=True)  # Field name made lowercase.
    ambulancetogoserviceurlimage = models.CharField(db_column='AmbulanceToGoServiceUrlImage', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ambulancetogoserviceprice = models.CharField(db_column='AmbulanceToGoServicePrice', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AmbulanceToGoServicePlan'


class Appformulary(models.Model):
    idappformulary = models.AutoField(db_column='idAppFormulary', primary_key=True)  # Field name made lowercase.
    appformularydescription = models.CharField(db_column='AppFormularyDescription', max_length=80, blank=True, null=True)  # Field name made lowercase.
    appformularypath = models.CharField(db_column='AppFormularyPath', max_length=80, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AppFormulary'


class Assistant(models.Model):
    assistantid = models.AutoField(db_column='assistantId', primary_key=True)  # Field name made lowercase.
    user_assistantid = models.ForeignKey('User', models.DO_NOTHING, db_column='User_AssistantId', blank=True, null=True)  # Field name made lowercase.
    doctype_doctypeid = models.ForeignKey('Doctype', models.DO_NOTHING, db_column='DocType_DocTypeId')  # Field name made lowercase.
    basicdatadocnumber = models.CharField(db_column='basicDataDocNumber', max_length=15, blank=True, null=True)  # Field name made lowercase.
    basicdatafirstname = models.CharField(db_column='basicDataFirstName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    basicdatalastname = models.CharField(db_column='basicDataLastName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    basicdataphoto = models.CharField(db_column='basicDataPhoto', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sex_sexid = models.ForeignKey('Sex', models.DO_NOTHING, db_column='Sex_sexId')  # Field name made lowercase.
    personaldatatelephone = models.CharField(db_column='personalDataTelephone', max_length=50, blank=True, null=True)  # Field name made lowercase.
    personaldatacellphone = models.CharField(db_column='personalDataCellphone', max_length=50, blank=True, null=True)  # Field name made lowercase.
    personaldataaddress = models.CharField(db_column='personalDataAddress', max_length=255, blank=True, null=True)  # Field name made lowercase.
    personaldataaddresscomplement = models.CharField(db_column='personalDataAddressComplement', max_length=255, blank=True, null=True)  # Field name made lowercase.
    personaldataemailaddress = models.CharField(db_column='personalDataEmailAddress', max_length=255, blank=True, null=True)  # Field name made lowercase.
    personaldataaddresscity = models.CharField(db_column='personalDataAddressCity', max_length=255, blank=True, null=True)  # Field name made lowercase.
    personaldataaddresslocality = models.CharField(db_column='personalDataAddressLocality', max_length=255, blank=True, null=True)  # Field name made lowercase.
    basicdatabirthdate = models.DateField(db_column='basicDataBirthDate', blank=True, null=True)  # Field name made lowercase.
    basicdatabirthplacecity = models.CharField(db_column='basicDataBirthPlaceCity', max_length=255, blank=True, null=True)  # Field name made lowercase.
    socialbenefitsarl = models.CharField(db_column='socialBenefitsARL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    socialbenefitshealth = models.CharField(db_column='socialBenefitsHealth', max_length=255, blank=True, null=True)  # Field name made lowercase.
    socialbenefitspension = models.CharField(db_column='socialBenefitsPension', max_length=255, blank=True, null=True)  # Field name made lowercase.
    educationacademiclevel = models.ForeignKey(Academiclevel, models.DO_NOTHING, db_column='educationAcademicLevel', blank=True, null=True)  # Field name made lowercase.
    professionaljobtitle = models.CharField(db_column='professionalJobTitle', max_length=255, blank=True, null=True)  # Field name made lowercase.
    professionalsalaryaspiration = models.IntegerField(db_column='professionalSalaryAspiration', blank=True, null=True)  # Field name made lowercase.
    professionalresume = models.CharField(db_column='professionalResume', max_length=255, blank=True, null=True)  # Field name made lowercase.
    paymentfifteen = models.IntegerField(db_column='paymentFifteen', blank=True, null=True)  # Field name made lowercase.
    professionalhvurl = models.CharField(db_column='professionalHVUrl', max_length=255, blank=True, null=True)  # Field name made lowercase.
    experiencemovility = models.IntegerField(db_column='experienceMovility', blank=True, null=True)  # Field name made lowercase.
    bossobservation = models.CharField(db_column='bossObservation', max_length=255, blank=True, null=True)  # Field name made lowercase.
    experiencecateter = models.IntegerField(db_column='experienceCateter', blank=True, null=True)  # Field name made lowercase.
    experiencetraqueo = models.IntegerField(db_column='experienceTraqueo', blank=True, null=True)  # Field name made lowercase.
    experienceintravain = models.IntegerField(db_column='experienceIntraVain', blank=True, null=True)  # Field name made lowercase.
    companybegindate = models.DateField(db_column='companyBeginDate', blank=True, null=True)  # Field name made lowercase.
    assistantregisterdate = models.DateTimeField(db_column='assistantRegisterDate', blank=True, null=True)  # Field name made lowercase.
    defaultworktime = models.CharField(db_column='defaultWorkTime', max_length=255, blank=True, null=True)  # Field name made lowercase.
    registeredbyuserid = models.IntegerField(db_column='registeredByUserId', blank=True, null=True)  # Field name made lowercase.
    companyid = models.ForeignKey('Company', models.DO_NOTHING, db_column='companyId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Assistant'


class Availability(models.Model):
    idavailability = models.AutoField(db_column='idAvailability', primary_key=True)  # Field name made lowercase.
    availabilitydate = models.DateField(db_column='AvailabilityDate', blank=True, null=True)  # Field name made lowercase.
    availabilityjourney = models.CharField(db_column='AvailabilityJourney', max_length=20, blank=True, null=True)  # Field name made lowercase.
    availabilitystatus = models.CharField(db_column='AvailabilityStatus', max_length=45, blank=True, null=True)  # Field name made lowercase.
    availability_assistantid = models.ForeignKey(Assistant, models.DO_NOTHING, db_column='Availability_AssistantId', blank=True, null=True)  # Field name made lowercase.
    availability_request = models.ForeignKey('Request', models.DO_NOTHING, db_column='Availability_Request_Id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Availability'


class Avatar(models.Model):
    avatarid = models.AutoField(db_column='avatarId', primary_key=True)  # Field name made lowercase.
    name = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'Avatar'


class Cancellation(models.Model):
    cancellationid = models.AutoField(db_column='cancellationId', primary_key=True)  # Field name made lowercase.
    cancellationdatetime = models.IntegerField(db_column='cancellationDateTime', blank=True, null=True)  # Field name made lowercase.
    cancellationnumweekiso = models.IntegerField(db_column='cancellationNumWeekISO', blank=True, null=True)  # Field name made lowercase.
    cancellationyear = models.IntegerField(db_column='cancellationYear', blank=True, null=True)  # Field name made lowercase.
    request_requestid = models.ForeignKey('Request', models.DO_NOTHING, db_column='Request_requestId')  # Field name made lowercase.
    assistant_assistantid = models.ForeignKey(Assistant, models.DO_NOTHING, db_column='Assistant_assistantId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Cancellation'


class City(models.Model):
    idcity = models.AutoField(db_column='idCity', primary_key=True)  # Field name made lowercase.
    cityname = models.CharField(db_column='CityName', max_length=64, blank=True, null=True)  # Field name made lowercase.
    zipcode = models.IntegerField(db_column='ZipCode', blank=True, null=True)  # Field name made lowercase.
    state_idstate = models.ForeignKey('State', models.DO_NOTHING, db_column='State_idState')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'City'


class Cityplanday(models.Model):
    idcityplanday = models.AutoField(db_column='idCityPlanDay', primary_key=True)  # Field name made lowercase.
    plan_idplan = models.ForeignKey('Plan', models.DO_NOTHING, db_column='Plan_idPlan')  # Field name made lowercase.
    city_idcity1 = models.ForeignKey(City, models.DO_NOTHING, db_column='City_idCity1')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CityPlanDay'


class Company(models.Model):
    companyid = models.AutoField(db_column='companyId', primary_key=True)  # Field name made lowercase.
    name = models.CharField(unique=True, max_length=100)
    nit = models.CharField(unique=True, max_length=15)
    address = models.CharField(max_length=80)
    contactphone = models.CharField(db_column='contactPhone', max_length=20)  # Field name made lowercase.
    contactname = models.CharField(db_column='contactName', max_length=255)  # Field name made lowercase.
    contactemail = models.CharField(db_column='contactEmail', max_length=80)  # Field name made lowercase.
    imageurl = models.CharField(db_column='imageUrl', max_length=255)  # Field name made lowercase.
    ruturl = models.CharField(db_column='rutURL', max_length=255)  # Field name made lowercase.
    imageappdisabled = models.CharField(db_column='imageAppDisabled', max_length=255, blank=True, null=True)  # Field name made lowercase.
    imageappenabled = models.CharField(db_column='imageAppEnabled', max_length=255, blank=True, null=True)  # Field name made lowercase.
    commissionpercent = models.IntegerField(db_column='commissionPercent', blank=True, null=True)  # Field name made lowercase.
    statuscompany_statuscompanyid = models.ForeignKey('Statuscompany', models.DO_NOTHING, db_column='StatusCompany_statusCompanyId')  # Field name made lowercase.
    cityid = models.IntegerField(db_column='CityId', blank=True, null=True)  # Field name made lowercase.
    companytype = models.ForeignKey('Companytype', models.DO_NOTHING, db_column='CompanyType', blank=True, null=True)  # Field name made lowercase.
    appformularyid = models.ForeignKey(Appformulary, models.DO_NOTHING, db_column='AppFormularyID', blank=True, null=True)  # Field name made lowercase.
    companyimportance = models.IntegerField(db_column='CompanyImportance', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Company'


class CompanyCity(models.Model):
    companycityid = models.AutoField(db_column='companyCityId', primary_key=True)  # Field name made lowercase.
    city_idcity = models.IntegerField(db_column='City_idCity')  # Field name made lowercase.
    company_companyid = models.IntegerField(db_column='Company_companyId')  # Field name made lowercase.
    deliveryvalue = models.IntegerField(db_column='DeliveryValue', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Company_City'
        unique_together = (('city_idcity', 'company_companyid'),)


class Country(models.Model):
    idcountry = models.AutoField(db_column='idCountry', primary_key=True)  # Field name made lowercase.
    countryname = models.CharField(db_column='CountryName', max_length=80, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Country'


class Coupon(models.Model):
    couponid = models.AutoField(db_column='couponId', primary_key=True)  # Field name made lowercase.
    code = models.CharField(max_length=100, blank=True, null=True)
    createddatetime = models.IntegerField(db_column='createdDateTime', blank=True, null=True)  # Field name made lowercase.
    expireddatetime = models.IntegerField(db_column='expiredDateTime', blank=True, null=True)  # Field name made lowercase.
    statuscoupon_statuscouponid = models.ForeignKey('Statuscoupon', models.DO_NOTHING, db_column='StatusCoupon_statusCouponId')  # Field name made lowercase.
    user_userid = models.ForeignKey('User', models.DO_NOTHING, db_column='User_userId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Coupon'


class Currencycode(models.Model):
    currencycodeid = models.AutoField(db_column='currencyCodeId', primary_key=True)  # Field name made lowercase.
    name = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'CurrencyCode'


class Device(models.Model):
    deviceid = models.AutoField(db_column='deviceId', primary_key=True)  # Field name made lowercase.
    user_userid = models.IntegerField(db_column='User_userId')  # Field name made lowercase.
    uuid = models.CharField(db_column='UUID', unique=True, max_length=100)  # Field name made lowercase.
    statusdevice_statusdeviceid = models.IntegerField(db_column='StatusDevice_statusDeviceId')  # Field name made lowercase.
    subscriptiondatetime = models.IntegerField(db_column='subscriptionDateTime', blank=True, null=True)  # Field name made lowercase.
    lastconnectiondatetime = models.IntegerField(db_column='lastConnectionDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Device'


class Deviceos(models.Model):
    deviceosid = models.AutoField(db_column='deviceOSId', primary_key=True)  # Field name made lowercase.
    name = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'DeviceOS'


class DeviceNotification(models.Model):
    deviceid = models.ForeignKey(Device, models.DO_NOTHING, db_column='Deviceid', primary_key=True)  # Field name made lowercase.
    notificationid = models.ForeignKey('Notification', models.DO_NOTHING, db_column='Notificationid')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Device_Notification'
        unique_together = (('deviceid', 'notificationid'),)


class Doctype(models.Model):
    doctypeid = models.AutoField(db_column='docTypeId', primary_key=True)  # Field name made lowercase.
    name = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'DocType'


class Family(models.Model):
    memberid = models.AutoField(db_column='memberId', primary_key=True)  # Field name made lowercase.
    user_userid = models.IntegerField(db_column='User_userId')  # Field name made lowercase.
    relationship_accountrelationshipid = models.IntegerField(db_column='Relationship_accountRelationshipId')  # Field name made lowercase.
    basicdatabirthdate = models.DateField(db_column='basicDataBirthDate', blank=True, null=True)  # Field name made lowercase.
    basicdatadisability = models.CharField(db_column='basicDataDisability', max_length=100, blank=True, null=True)  # Field name made lowercase.
    doctype_doctypeid = models.IntegerField(db_column='DocType_docTypeId')  # Field name made lowercase.
    basicdatadocnumber = models.CharField(db_column='basicDataDocNumber', unique=True, max_length=15, blank=True, null=True)  # Field name made lowercase.
    basicdatafirstname = models.CharField(db_column='basicDataFirstName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    basicdatalastname = models.CharField(db_column='basicDataLastName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    sex_sexid = models.IntegerField(db_column='Sex_sexId')  # Field name made lowercase.
    mobility_basicdatamobiilityid = models.IntegerField(db_column='Mobility_basicDataMobiilityId')  # Field name made lowercase.
    basicdataheight = models.CharField(db_column='basicDataHeight', max_length=3, blank=True, null=True)  # Field name made lowercase.
    basicdataweight = models.CharField(db_column='basicDataWeight', max_length=3, blank=True, null=True)  # Field name made lowercase.
    personaldatacellphone = models.CharField(db_column='personalDataCellphone', max_length=15, blank=True, null=True)  # Field name made lowercase.
    emergencycontactcellphone = models.CharField(db_column='emergencyContactCellphone', max_length=15, blank=True, null=True)  # Field name made lowercase.
    emergencycontactnameperson = models.CharField(db_column='emergencyContactNamePerson', max_length=100, blank=True, null=True)  # Field name made lowercase.
    userepsname = models.CharField(db_column='userEpsName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    userobservations = models.CharField(db_column='userObservations', max_length=255, blank=True, null=True)  # Field name made lowercase.
    statususer_statususerid = models.IntegerField(db_column='StatusUser_statusUserId')  # Field name made lowercase.
    rol_rolid = models.IntegerField(db_column='Rol_rolId')  # Field name made lowercase.
    avatar_avatarid = models.IntegerField(db_column='Avatar_avatarId')  # Field name made lowercase.
    relationship_emergencycontactrelationshipid = models.IntegerField(db_column='Relationship_emergencyContactRelationshipId')  # Field name made lowercase.
    userallergies = models.CharField(db_column='userAllergies', max_length=255, blank=True, null=True)  # Field name made lowercase.
    usermedicines = models.CharField(db_column='userMedicines', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Family'


class Frequency(models.Model):
    frequencyid = models.AutoField(db_column='frequencyId', primary_key=True)  # Field name made lowercase.
    name = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'Frequency'


class Holiday(models.Model):
    holidayid = models.AutoField(db_column='HolidayId', primary_key=True)  # Field name made lowercase.
    holidaydate = models.DateField(db_column='HolidayDate')  # Field name made lowercase.
    country_idcountry = models.IntegerField(db_column='Country_idCountry')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Holiday'
        unique_together = (('holidayid', 'country_idcountry'),)


class Messagechat(models.Model):
    user_fromid = models.ForeignKey('User', models.DO_NOTHING, db_column='User_fromId')  # Field name made lowercase.
    sendeddatetime = models.IntegerField(db_column='sendedDateTime', blank=True, null=True)  # Field name made lowercase.
    message = models.CharField(max_length=255, blank=True, null=True)
    roomchat_roomchatid = models.ForeignKey('Roomchat', models.DO_NOTHING, db_column='RoomChat_roomChatId')  # Field name made lowercase.
    seen = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MessageChat'


class Messagesupport(models.Model):
    support_supportid = models.ForeignKey('Support', models.DO_NOTHING, db_column='Support_supportId')  # Field name made lowercase.
    user_fromid = models.ForeignKey('User', models.DO_NOTHING, db_column='User_fromId')  # Field name made lowercase.
    sendeddatetime = models.IntegerField(db_column='sendedDateTime', blank=True, null=True)  # Field name made lowercase.
    seen = models.IntegerField(blank=True, null=True)
    message = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MessageSupport'


class Mobility(models.Model):
    mobilityid = models.AutoField(db_column='mobilityId', primary_key=True)  # Field name made lowercase.
    name = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'Mobility'


class Notification(models.Model):
    notificationid = models.AutoField(db_column='notificationId', primary_key=True)  # Field name made lowercase.
    user_userid = models.IntegerField(db_column='User_userId')  # Field name made lowercase.
    sendeddatetime = models.IntegerField(db_column='sendedDateTime', blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(max_length=255, blank=True, null=True)
    subtitle = models.CharField(max_length=255, blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    imagepath = models.TextField(db_column='imagePath', blank=True, null=True)  # Field name made lowercase.
    lanuchurl = models.TextField(db_column='lanuchURL', blank=True, null=True)  # Field name made lowercase.
    additionaldata = models.TextField(db_column='additionalData', blank=True, null=True)  # Field name made lowercase.
    actionsbuttons = models.TextField(db_column='actionsButtons', blank=True, null=True)  # Field name made lowercase.
    seen = models.IntegerField(blank=True, null=True)
    uuidnotification = models.CharField(db_column='UUIDNotification', max_length=255, blank=True, null=True)  # Field name made lowercase.
    typenotification_typenotificationid = models.IntegerField(db_column='TypeNotification_typeNotificationId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Notification'


class Permission(models.Model):
    permissionid = models.AutoField(db_column='PermissionId', primary_key=True)  # Field name made lowercase.
    permissionname = models.CharField(db_column='PermissionName', max_length=64)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Permission'


class Pillbox(models.Model):
    pillboxid = models.AutoField(db_column='pillboxId', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=100, blank=True, null=True)
    quantity = models.CharField(max_length=50, blank=True, null=True)
    frequency = models.IntegerField(blank=True, null=True)
    typepillbox = models.CharField(db_column='typePillbox', max_length=10, blank=True, null=True)  # Field name made lowercase.
    family_familyid = models.IntegerField(db_column='Family_familyId')  # Field name made lowercase.
    frequency_frequencyid = models.IntegerField(db_column='Frequency_frequencyId', blank=True, null=True)  # Field name made lowercase.
    typepillbox_typepillboxid = models.IntegerField(db_column='TypePillbox_typePillboxId', blank=True, null=True)  # Field name made lowercase.
    startedat = models.TimeField(db_column='startedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Pillbox'


class Plan(models.Model):
    idplan = models.AutoField(db_column='idPlan', primary_key=True)  # Field name made lowercase.
    planname = models.CharField(db_column='PlanName', max_length=64, blank=True, null=True)  # Field name made lowercase.
    pacientsammount = models.IntegerField(db_column='PacientsAmmount')  # Field name made lowercase.
    holidayprice = models.IntegerField(db_column='HolidayPrice', blank=True, null=True)  # Field name made lowercase.
    workdayprice = models.IntegerField(db_column='WorkDayPrice', blank=True, null=True)  # Field name made lowercase.
    companyid = models.IntegerField(db_column='companyId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Plan'


class Plandays(models.Model):
    idplandays = models.AutoField(db_column='idPlanDays', primary_key=True)  # Field name made lowercase.
    cardinality = models.CharField(db_column='Cardinality', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PlanDays'


class PlanHasPlandays(models.Model):
    idplanhasdays = models.AutoField(db_column='IdPlanHasDays', primary_key=True)  # Field name made lowercase.
    plan_idplan = models.ForeignKey(Plan, models.DO_NOTHING, db_column='Plan_idPlan', blank=True, null=True)  # Field name made lowercase.
    plandays_idplandays = models.ForeignKey(Plandays, models.DO_NOTHING, db_column='PlanDays_idPlanDays', blank=True, null=True)  # Field name made lowercase.
    numberofdays = models.IntegerField(db_column='NumberOfDays')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Plan_has_PlanDays'


class Product(models.Model):
    productid = models.AutoField(db_column='productId', primary_key=True)  # Field name made lowercase.
    nameproduct = models.CharField(db_column='nameProduct', max_length=255)  # Field name made lowercase.
    imageurl = models.CharField(db_column='ImageUrl', max_length=255)  # Field name made lowercase.
    costproduct = models.IntegerField(db_column='costProduct', blank=True, null=True)  # Field name made lowercase.
    disccount = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    typeproduct_typeproductid = models.ForeignKey('Typeproduct', models.DO_NOTHING, db_column='TypeProduct_typeProductId')  # Field name made lowercase.
    company_companyid = models.ForeignKey(Company, models.DO_NOTHING, db_column='Company_companyId')  # Field name made lowercase.
    productstatusid = models.ForeignKey('Productstatus', models.DO_NOTHING, db_column='ProductStatusId', blank=True, null=True)  # Field name made lowercase.
    eancode = models.CharField(db_column='EanCode', unique=True, max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Product'


class Professionalspecialty(models.Model):
    professionalspecialtyid = models.AutoField(db_column='professionalSpecialtyId', primary_key=True)  # Field name made lowercase.
    assistant_assistantid = models.ForeignKey(Assistant, models.DO_NOTHING, db_column='Assistant_assistantId')  # Field name made lowercase.
    specialtyname = models.CharField(db_column='SpecialtyName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    specialtyyearsexperience = models.IntegerField(db_column='SpecialtyYearsExperience', blank=True, null=True)  # Field name made lowercase.
    assistantprofessionaljobtitle = models.CharField(db_column='AssistantprofessionalJobTitle', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ProfessionalSpecialty'


class Provieded(models.Model):
    proviededid = models.AutoField(db_column='proviededId', primary_key=True)  # Field name made lowercase.
    servicedatetimeontheroadstarted = models.IntegerField(db_column='serviceDateTimeOnTheRoadStarted', blank=True, null=True)  # Field name made lowercase.
    servicelatepenalty = models.IntegerField(db_column='serviceLatePenalty', blank=True, null=True)  # Field name made lowercase.
    servicenumweekiso = models.IntegerField(db_column='serviceNumWeekISO', blank=True, null=True)  # Field name made lowercase.
    servicedatetimearrival = models.IntegerField(db_column='serviceDateTimeArrival', blank=True, null=True)  # Field name made lowercase.
    servicedatetimedeparture = models.IntegerField(db_column='serviceDateTimeDeparture', blank=True, null=True)  # Field name made lowercase.
    servicerequestpayforassistant = models.IntegerField(db_column='serviceRequestPayForAssistant', blank=True, null=True)  # Field name made lowercase.
    servicerequestpenaltycost = models.IntegerField(db_column='serviceRequestPenaltyCost', blank=True, null=True)  # Field name made lowercase.
    serviceyear = models.IntegerField(db_column='serviceYear', blank=True, null=True)  # Field name made lowercase.
    request_requestid = models.ForeignKey('Request', models.DO_NOTHING, db_column='Request_requestId')  # Field name made lowercase.
    assistant_assistantid = models.ForeignKey(Assistant, models.DO_NOTHING, db_column='Assistant_assistantId')  # Field name made lowercase.
    controlobservations = models.CharField(db_column='controlObservations', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Provieded'


class Purchaseorder(models.Model):
    purchaseorderid = models.AutoField(db_column='purchaseOrderId', primary_key=True)  # Field name made lowercase.
    address_addressid = models.ForeignKey(Address, models.DO_NOTHING, db_column='Address_addressId')  # Field name made lowercase.
    product_productid = models.ForeignKey(Product, models.DO_NOTHING, db_column='Product_productId')  # Field name made lowercase.
    quantity = models.IntegerField(blank=True, null=True)
    producttotalamount = models.IntegerField(db_column='productTotalAmount', blank=True, null=True)  # Field name made lowercase.
    transactionpaymentgateway_transactionpaymentgatewayid = models.ForeignKey('Transactionpaymentgateway', models.DO_NOTHING, db_column='TransactionPaymentGateway_transactionPaymentGatewayId')  # Field name made lowercase.
    temp_address = models.CharField(max_length=255, blank=True, null=True)
    temp_addressinfo = models.CharField(db_column='temp_addressInfo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    purchaseorderdatetime = models.IntegerField(db_column='purchaseOrderDateTime', blank=True, null=True)  # Field name made lowercase.
    currencycode_producttotalamount = models.ForeignKey(Currencycode, models.DO_NOTHING, db_column='CurrencyCode_productTotalAmount')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PurchaseOrder'


class Relationship(models.Model):
    relationshipid = models.AutoField(db_column='relationshipId', primary_key=True)  # Field name made lowercase.
    name = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'Relationship'


class Request(models.Model):
    requestid = models.AutoField(db_column='requestId', primary_key=True)  # Field name made lowercase.
    statusservice_servicestatusid = models.IntegerField(db_column='StatusService_serviceStatusId')  # Field name made lowercase.
    family_userserviceid = models.IntegerField(db_column='Family_userServiceId')  # Field name made lowercase.
    statusservice = models.IntegerField(db_column='StatusService')  # Field name made lowercase.
    address_addressid = models.IntegerField(db_column='Address_addressId', blank=True, null=True)  # Field name made lowercase.
    requestdatetime = models.IntegerField(db_column='requestDateTime', blank=True, null=True)  # Field name made lowercase.
    servicedatetimestart = models.DateField(db_column='serviceDateTimeStart', blank=True, null=True)  # Field name made lowercase.
    servicedatetimeend = models.DateField(db_column='serviceDateTimeEnd', blank=True, null=True)  # Field name made lowercase.
    servicemeridian = models.CharField(db_column='serviceMeridian', max_length=45, blank=True, null=True)  # Field name made lowercase.
    servicetotalamount = models.IntegerField(db_column='serviceTotalAmount', blank=True, null=True)  # Field name made lowercase.
    currencycode_servicetotalamountcurrencycode = models.IntegerField(db_column='CurrencyCode_serviceTotalAmountCurrencyCode')  # Field name made lowercase.
    userrequestobservations = models.CharField(db_column='userRequestObservations', max_length=255, blank=True, null=True)  # Field name made lowercase.
    temp_address = models.CharField(max_length=255, blank=True, null=True)
    temp_addressinfo = models.CharField(db_column='temp_addressInfo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    transactionpaymentgateway_transactionpaymentgatewayid = models.IntegerField(db_column='TransactionPaymentGateway_transactionPaymentGatewayId', blank=True, null=True)  # Field name made lowercase.
    planname = models.CharField(db_column='PlanName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    companyid = models.ForeignKey(Company, models.DO_NOTHING, db_column='CompanyId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Request'


class Rol(models.Model):
    rolid = models.AutoField(db_column='rolId', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Rol'


class Rolpermission(models.Model):
    rolpermissionid = models.AutoField(db_column='RolPermissionId', primary_key=True)  # Field name made lowercase.
    permissionid = models.IntegerField(db_column='PermissionId')  # Field name made lowercase.
    rolid = models.IntegerField(db_column='RolId')  # Field name made lowercase.
    create = models.IntegerField(db_column='Create')  # Field name made lowercase.
    read = models.IntegerField(db_column='Read')  # Field name made lowercase.
    update = models.IntegerField(db_column='Update')  # Field name made lowercase.
    delete = models.IntegerField(db_column='Delete')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RolPermission'


class Roomchat(models.Model):
    roomchatid = models.AutoField(db_column='roomChatId', primary_key=True)  # Field name made lowercase.
    roomdatetimestarted = models.IntegerField(db_column='roomDateTimeStarted', blank=True, null=True)  # Field name made lowercase.
    provieded_proviededid = models.ForeignKey(Provieded, models.DO_NOTHING, db_column='Provieded_proviededId')  # Field name made lowercase.
    statusroomchat_statusroomchatid = models.ForeignKey('Statusroomchat', models.DO_NOTHING, db_column='StatusRoomChat_statusRoomChatId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RoomChat'


class Service(models.Model):
    serviceid = models.AutoField(db_column='serviceId', primary_key=True)  # Field name made lowercase.
    company_companyid = models.ForeignKey(Company, models.DO_NOTHING, db_column='Company_companyId')  # Field name made lowercase.
    name = models.CharField(unique=True, max_length=100)
    costamount = models.IntegerField(db_column='costAmount', blank=True, null=True)  # Field name made lowercase.
    typeservice_typeserviceid = models.ForeignKey('Typeservice', models.DO_NOTHING, db_column='TypeService_typeServiceId')  # Field name made lowercase.
    servicedetail = models.CharField(db_column='serviceDetail', max_length=255, blank=True, null=True)  # Field name made lowercase.
    isdayholiday = models.IntegerField(db_column='isDayHoliday', blank=True, null=True)  # Field name made lowercase.
    durationservice = models.IntegerField(db_column='durationService', blank=True, null=True)  # Field name made lowercase.
    serviceimageurl = models.CharField(db_column='ServiceImageURL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    paymentid = models.ForeignKey('Transactionpaymentgateway', models.DO_NOTHING, db_column='PaymentId', blank=True, null=True)  # Field name made lowercase.
    servicestatus = models.ForeignKey('Statusservice', models.DO_NOTHING, db_column='ServiceStatus', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Service'


class Sex(models.Model):
    sexid = models.AutoField(db_column='sexId', primary_key=True)  # Field name made lowercase.
    name = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'Sex'


class State(models.Model):
    idstate = models.AutoField(db_column='idState', primary_key=True)  # Field name made lowercase.
    statename = models.CharField(db_column='StateName', max_length=80, blank=True, null=True)  # Field name made lowercase.
    country_idcountry = models.ForeignKey(Country, models.DO_NOTHING, db_column='Country_idCountry')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'State'


class Statusaddress(models.Model):
    statusaddressid = models.AutoField(db_column='statusAddressId', primary_key=True)  # Field name made lowercase.
    name = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'StatusAddress'


class Statuscompany(models.Model):
    statuscompanyid = models.AutoField(db_column='statusCompanyId', primary_key=True)  # Field name made lowercase.
    name = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'StatusCompany'


class Statuscoupon(models.Model):
    statuscouponid = models.AutoField(db_column='statusCouponId', primary_key=True)  # Field name made lowercase.
    name = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'StatusCoupon'


class Statusdevice(models.Model):
    statusdeviceid = models.AutoField(db_column='StatusDeviceId', primary_key=True)  # Field name made lowercase.
    name = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'StatusDevice'


class Statuspayment(models.Model):
    statuspaymentid = models.AutoField(db_column='statusPaymentId', primary_key=True)  # Field name made lowercase.
    name = models.CharField(unique=True, max_length=100)
    status = models.CharField(max_length=100)
    description = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'StatusPayment'


class Statusroomchat(models.Model):
    statusroomchatid = models.AutoField(db_column='statusRoomChatId', primary_key=True)  # Field name made lowercase.
    name = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'StatusRoomChat'


class Statusservice(models.Model):
    statusserviceid = models.AutoField(db_column='statusServiceId', primary_key=True)  # Field name made lowercase.
    name = models.CharField(unique=True, max_length=100)
    namedisplay = models.CharField(db_column='nameDisplay', max_length=50, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'StatusService'


class Statususer(models.Model):
    statususerid = models.AutoField(db_column='statusUserId', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'StatusUser'


class Support(models.Model):
    supportid = models.AutoField(db_column='supportId', primary_key=True)  # Field name made lowercase.
    supportdatetimestarted = models.IntegerField(db_column='supportDateTimeStarted', blank=True, null=True)  # Field name made lowercase.
    user_assistantid = models.ForeignKey('User', models.DO_NOTHING, db_column='User_AssistantId')  # Field name made lowercase.
    statusroomchat_statusroomid = models.ForeignKey(Statusroomchat, models.DO_NOTHING, db_column='StatusRoomChat_statusRoomId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Support'


class Transactionpaymentgateway(models.Model):
    transactionpaymentgatewayid = models.AutoField(db_column='transactionPaymentGatewayId', primary_key=True)  # Field name made lowercase.
    refnumber = models.CharField(db_column='refNumber', max_length=20)  # Field name made lowercase.
    orderidentifier = models.CharField(db_column='orderIdentifier', max_length=50)  # Field name made lowercase.
    creationdatetime = models.IntegerField(db_column='creationDateTime')  # Field name made lowercase.
    updatedatetime = models.IntegerField(db_column='updateDateTime', blank=True, null=True)  # Field name made lowercase.
    orderdescription = models.CharField(db_column='orderDescription', max_length=255, blank=True, null=True)  # Field name made lowercase.
    method = models.CharField(max_length=20, blank=True, null=True)
    checkouturl = models.TextField(db_column='checkoutURL')  # Field name made lowercase.
    statuspayment_statuspaymentid = models.ForeignKey(Statuspayment, models.DO_NOTHING, db_column='StatusPayment_statusPaymentId')  # Field name made lowercase.
    formularytype = models.ForeignKey(Appformulary, models.DO_NOTHING, db_column='FormularyType', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TransactionPaymentGateway'


class Typenotification(models.Model):
    typenotificationid = models.AutoField(db_column='typeNotificationId', primary_key=True)  # Field name made lowercase.
    name = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'TypeNotification'


class Typepillbox(models.Model):
    typepillboxid = models.AutoField(db_column='typePillboxId', primary_key=True)  # Field name made lowercase.
    name = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'TypePillbox'


class Typeproduct(models.Model):
    typeproductid = models.AutoField(db_column='typeProductId', primary_key=True)  # Field name made lowercase.
    name = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'TypeProduct'


class Typeservice(models.Model):
    typeserviceid = models.AutoField(db_column='typeServiceId', primary_key=True)  # Field name made lowercase.
    name = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'TypeService'


class User(models.Model):
    userid = models.AutoField(db_column='userId', primary_key=True)  # Field name made lowercase.
    lastconnectiondatetime = models.IntegerField(db_column='lastConnectionDateTime', blank=True, null=True)  # Field name made lowercase.
    userdocnumber = models.CharField(db_column='userDocNumber', max_length=15, blank=True, null=True)  # Field name made lowercase.
    accountemail = models.CharField(db_column='accountEmail', unique=True, max_length=255)  # Field name made lowercase.
    accountpassword = models.CharField(db_column='accountPassword', max_length=255, blank=True, null=True)  # Field name made lowercase.
    accountcellphone = models.CharField(db_column='accountCellphone', unique=True, max_length=15, blank=True, null=True)  # Field name made lowercase.
    accountname = models.CharField(db_column='accountName', max_length=255)  # Field name made lowercase.
    isemailverified = models.IntegerField(db_column='isEmailVerified', blank=True, null=True)  # Field name made lowercase.
    isnewuser = models.IntegerField(db_column='isNewUser', blank=True, null=True)  # Field name made lowercase.
    isonline = models.IntegerField(db_column='isOnline', blank=True, null=True)  # Field name made lowercase.
    photourl = models.CharField(db_column='photoURL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    rol_rolid = models.ForeignKey(Rol, models.DO_NOTHING, db_column='Rol_rolId')  # Field name made lowercase.
    status_statusid = models.ForeignKey(Statususer, models.DO_NOTHING, db_column='Status_statusId')  # Field name made lowercase.
    tokenfacebook = models.CharField(db_column='tokenFacebook', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tokengoogle = models.CharField(db_column='tokenGoogle', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tokenapple = models.CharField(db_column='tokenApple', max_length=255, blank=True, null=True)  # Field name made lowercase.
    createdat = models.IntegerField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.
    updatedat = models.IntegerField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.
    temppasswordtoken = models.CharField(db_column='tempPasswordToken', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tokenpasswordexpiredat = models.IntegerField(db_column='tokenPasswordExpiredAt', blank=True, null=True)  # Field name made lowercase.
    company_companyid = models.ForeignKey(Company, models.DO_NOTHING, db_column='Company_companyId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'User'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Companytype(models.Model):
    idcompanytype = models.AutoField(db_column='idcompanyType', primary_key=True)  # Field name made lowercase.
    companytypedescription = models.CharField(db_column='companyTypeDescription', max_length=45, blank=True, null=True)  # Field name made lowercase.
    companytypeimageurl = models.CharField(db_column='companyTypeImageUrl', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'companyType'


class Diasnoticimagesservice(models.Model):
    iddiasnoticimagesservice = models.AutoField(db_column='iddiasnoticImagesService', primary_key=True)  # Field name made lowercase.
    diasnoticimagesserviceaddress = models.CharField(db_column='diasnoticImagesServiceAddress', max_length=128, blank=True, null=True)  # Field name made lowercase.
    diasnoticimagesserviceuserphone = models.CharField(db_column='diasnoticImagesServiceUserPhone', max_length=45, blank=True, null=True)  # Field name made lowercase.
    diasnoticimagesserviceusername = models.CharField(db_column='diasnoticImagesServiceUserName', max_length=80, blank=True, null=True)  # Field name made lowercase.
    diasnoticimagesserviceemail = models.CharField(db_column='diasnoticImagesServiceEmail', max_length=128, blank=True, null=True)  # Field name made lowercase.
    diasnoticimagesservicevalue = models.CharField(db_column='diasnoticImagesServiceValue', max_length=45, blank=True, null=True)  # Field name made lowercase.
    diasnoticimagesserviceplan_iddiasnoticimagesserviceplan = models.ForeignKey('Diasnoticimagesserviceplan', models.DO_NOTHING, db_column='diasnoticImagesServicePlan_iddiasnoticImagesServicePlan')  # Field name made lowercase.
    diasnoticimagesserviceuserid = models.ForeignKey(User, models.DO_NOTHING, db_column='diasnoticImagesServiceUserId')  # Field name made lowercase.
    diasnoticimagesservicetransaction = models.ForeignKey(Transactionpaymentgateway, models.DO_NOTHING, db_column='diasnoticImagesServiceTransaction', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'diasnoticImagesService'


class Diasnoticimagesserviceplan(models.Model):
    iddiasnoticimagesserviceplan = models.AutoField(db_column='iddiasnoticImagesServicePlan', primary_key=True)  # Field name made lowercase.
    diasnoticimagesserviceplandescription = models.CharField(db_column='diasnoticImagesServicePlanDescription', max_length=80, blank=True, null=True)  # Field name made lowercase.
    diasnoticimagesserviceplanvalue = models.CharField(db_column='diasnoticImagesServicePlanValue', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'diasnoticImagesServicePlan'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Productstatus(models.Model):
    idproductstatus = models.IntegerField(db_column='idProductStatus', primary_key=True)  # Field name made lowercase.
    productstatusdescription = models.CharField(db_column='productStatusDescription', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'productStatus'


class Productspayment(models.Model):
    idproductspayment = models.AutoField(db_column='idproductsPayment', primary_key=True)  # Field name made lowercase.
    paymentusername = models.CharField(db_column='paymentUserName', max_length=80, blank=True, null=True)  # Field name made lowercase.
    paymentuseremail = models.CharField(db_column='paymentUserEmail', max_length=80, blank=True, null=True)  # Field name made lowercase.
    paymentaddress = models.CharField(db_column='paymentAddress', max_length=128, blank=True, null=True)  # Field name made lowercase.
    paymentzipcode = models.CharField(db_column='paymentZipCode', max_length=6, blank=True, null=True)  # Field name made lowercase.
    paymentcityid = models.ForeignKey(City, models.DO_NOTHING, db_column='paymentCityId')  # Field name made lowercase.
    paymenttransactionid = models.ForeignKey(Transactionpaymentgateway, models.DO_NOTHING, db_column='paymentTransactionId', blank=True, null=True)  # Field name made lowercase.
    paymentuserid = models.ForeignKey(User, models.DO_NOTHING, db_column='paymentUserId')  # Field name made lowercase.
    paymentvalue = models.CharField(db_column='paymentValue', max_length=80, blank=True, null=True)  # Field name made lowercase.
    paymentdeliveryvalue = models.CharField(db_column='paymentDeliveryValue', max_length=80, blank=True, null=True)  # Field name made lowercase.
    servicestatus = models.ForeignKey(Statusservice, models.DO_NOTHING, db_column='ServiceStatus', blank=True, null=True)  # Field name made lowercase.
    paymentorderdate = models.DateTimeField(db_column='PaymentOrderDate', blank=True, null=True)  # Field name made lowercase.
    paymentphonenumber = models.CharField(db_column='PaymentPhoneNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    paymentuserdocument = models.CharField(db_column='PaymentUserDocument', max_length=50, blank=True, null=True)  # Field name made lowercase.
    paymentuserdocumenttype = models.ForeignKey(Doctype, models.DO_NOTHING, db_column='PaymentUserDocumentType', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'productsPayment'


class ProductspaymentHasProduct(models.Model):
    productspayment_idproductspayment = models.ForeignKey(Productspayment, models.DO_NOTHING, db_column='productsPayment_idproductsPayment', primary_key=True)  # Field name made lowercase.
    product_productid = models.ForeignKey(Product, models.DO_NOTHING, db_column='Product_productId')  # Field name made lowercase.
    productcount = models.CharField(db_column='productCount', max_length=45, blank=True, null=True)  # Field name made lowercase.
    productammount = models.FloatField(db_column='productAmmount', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'productsPayment_has_Product'
        unique_together = (('productspayment_idproductspayment', 'product_productid'),)
