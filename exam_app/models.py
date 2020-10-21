from django.db import models
from datetime import date

class UserManager(models.Manager):
    def loginValidator(self, FormInfo):
        errors = {}
        if FormInfo['usernameLog'] == "":
            errors['blankerror'] = "Invalid Username"
            return errors
        loginUser = User.objects.filter(username=FormInfo['usernameLog'])
        if len(loginUser) != 0:
            if FormInfo['passwordLog'] != loginUser[0].password:
                errors['loginerror'] = "Invalid Password"
            return errors
        errors['usernamenotvalid'] = "Invalid Username"
        return errors
    def RegisterValidator(self, FormInfo):
        errors = {}
        filterResult = User.objects.filter(username=FormInfo['usernameReg'])
        if len(filterResult) > 0:
            errors['usernameError'] = "Username is already in use."
            return errors
        if len(FormInfo['passwordReg']) < 8:
            errors['passwordLenError'] = "Password must contain at least 8 characters."
        if len(FormInfo['usernameReg']) < 3:
            errors['lentooshortusernameerror'] = "Username requires 3 characters or more."
        if len(FormInfo['name']) < 3:
            errors['nameerror'] = "Name requires 3 characters or more."
        if FormInfo['passwordReg'] != FormInfo['confirmPW']:
            errors['passwordMatchError'] = "Passwords should match."
        return errors

class User(models.Model):
    name = models.CharField(max_length = 255)
    username = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class TripManager(models.Manager):
    def tripValidator(self, FormInfo):
        errors = {}
        if len(FormInfo['destination']) == 0:
            errors['lenofdesterror'] = "no empty entries"
        if len(FormInfo['description']) == 0:
            errors['lenofdescerror'] = "no empty entries"
        if len(FormInfo['datefrom']) == 0:
            errors['datefromerror'] = "no empty entries"
        if len(FormInfo['dateto']) == 0:
            errors['datetoerror'] = "no empty entries"
        today = date.today()
        if FormInfo['datefrom'] < str(today):
            errors['dateerror'] = "Date must be in future."
        if FormInfo['datefrom'] > FormInfo['dateto']:
            errors['dateerror2'] = "Date to must be after date from."
        return errors

class Trip(models.Model):
    planned_by = models.CharField(max_length = 255, null = True)
    destination = models.CharField(max_length = 255)
    desc = models.CharField(max_length = 255)
    travel_date_from = models.DateField()
    travel_date_to = models.DateField()
    user = models.ManyToManyField(User, related_name = "trips")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = TripManager()

