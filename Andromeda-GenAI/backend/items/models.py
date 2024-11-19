from django.db import models

class Item(models.Model):
    customerId = models.CharField(max_length=100)
    gender = models.CharField(max_length=1)
    age = models.IntegerField()
    maritalStatus = models.CharField(max_length=20)
    income = models.IntegerField()
    occupation = models.CharField(max_length=100)
    creditScore = models.IntegerField()
    outStandingLoans = models.IntegerField()
    bankingHistory = models.TextField()
    currentAccountBalance = models.IntegerField()
    savingsAccountBalance = models.IntegerField()
    propertyOwnership = models.TextField()
    vehicleOwned = models.TextField()
    insuranceCoverage = models.TextField()
    investmentPortfolio = models.TextField()
    digitalBankingUsage = models.TextField()
    riskAppetite = models.TextField()
    location = models.TextField()
    spendingHabits = models.TextField()
    

    def __str__(self):
        return self.name
