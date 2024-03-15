# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 14:16:45 2024

@author: Ashish Chincholikar

"""
import pandas as pd
import statsmodels.stats.descriptivestats 
from scipy import stats
import numpy as np

#from statsmodels.stats import Weightstats as stats 
import statsmodels.stats.weightstats as stests
#1 sample sign test 
#for given dataset check whether scores are qwual or less than 50 
#H0 = scores are either equal or less than 80 
#H1 = scoress are not equal n greater than 80 
#Whenever there is single sample and data is not normal
marks = pd.read_csv("C:\Hypothesis\hypothesis_datasets/Signtest.csv")
#Normal QQ Plot 

import pylab
stats.probplot(marks.Scores, dist='norm',plot=pylab)
#Data is not normal 
#H0 - data is normal 
#H1 -data is not normal 
stats.shapiro(marks.Scores)
#p_value is 0.024299481883645058, p is low null go 
#p_value is 0.024299481883645058 > 0.005 , p is high null fly/apply
#Decision :  data is not normal
#H1 is valid normal
###########################################
#Let us check the distribution of the data 
marks.Scores.describe()
#1-sample sign test 
sd.sign_test(marks.Scores,mu0=mRKS.Scores.mean())
#p_ value is 0.02> 0.05  so p is high null fly 

#Decision :
#H0 scores one either equal or less than 80

#-----------------1-sample Z-test-------------------


fabric = pd.read_csv("C:/Hypothesis/hypothesis_datasets/Fabric_data.csv")

#calculating the normality test
print(stats.shapiro(fabric))
#0.1460>0.005 H0 is True

#Calculating the mean 
np.mean(fabric)

#ztest 
# parameters in z tests, value is mean of data 
ztest, pval = stests.ztest(fabric,x2=None, value=150)

print(float(pval))

#-------------Mann-Whitney Test-----------------
#vehicles with and without addictive
#Ho : fuel additive does not impact the performance
#H1 : fuell additive does impact the performance

fuel = pd.read_csv("C:/Hypothesis/hypothesis_datasets/mann_whitney_additive.csv")
fuel

fuel.columns = "without_additive" , "with_additive"

#Noramlity test
#Ho : data is normal
print(stats.shapiro(fuel.without_additive)) #p high null fly
print(stats.shapiro(fuel.with_additive))    #p low null go
#Without_additive is normal
#With additive is not normal
#when two samples are not normal then mannwhitney test
#non-Parameteric test case
#Mann-Whitney test
import scipy
scipy.stats.mannwhitneyu(fuel.Without_additive , fuel.With_additive)

#---------Paired T-Test------------
#When two features are normal then paired T test
#A univariate test that tests for a signigicant difference between

sup = pd.read_csv("C:/Hypothesis/hypothesis_datasets/paired2.csv")
sup.describe()

#Ho : There is no significant difference between means of suppliers A and B
#Ha : There is signigicant difference between means of suppliers of A and B
#Normality Test : #Shapiro Test
stats.shapiro(sup.SupplierA)
#pvalue = 0.896 > 0.005 hence data is normal
stats.shapiro(sup.SupplierB)
#Data are Normal

import seaborn as sns
sns.boxplot(data  = sup)

#Assuming the external conditions are same for both the samples
#paired T-test

ttest , pval = stats.ttest_rel(sup['SupplierA'] ,sup['SupplierB'])
print(pval)

#-------------2 Sample T-Test------------

#load the data
prom = pd.read_excel("C:/Hypothesis/hypothesis_datasets/Promotion.xlsx")
prom

#Ho : InterestRateWaiver < StandardPromotion
#Ha : InterestRateWaiver > StandardPromotion

prom.columns = "InterestRateWavier" , "StandardPromotion"

#Normality Test
stats.shapiro(prom.InterestRateWavier)#Shapiro Test
print(stats.shapiro(prom.StandardPromotion))

#Data are Normal
#Variance test
help(scipy.stats.levene)
#Ho : Both columns have equal variance
#Ha : Both columns have not equal variance

scipy.stats.levene(prom.InterestRateWavier , prom.StandardPromotion)
#p-value = 0.287 >0.05 so p high null fly => Equal Variances

#2 sample T-test
scipy.stats.ttest_ind(prom.InterestRateWavier , prom.StandardPromotion)
help(scipy.stats.ttest_ind)

#Ho : 
    
#----------------One way ANOVA---------------

con_renewal = pd.read_excel("C:/Hypothesis/hypothesis_datasets/ContractRenewal_Data(unstacked).xlsx")
con_renewal
con_renewal.columns = "SupplierA" , "SupplierB" , "SupplierC"
#H0 : All the 3 suppliers have equal means transaction time
#H1 : All the 3 suppliers have not equal means transaction time
#Normality test
stats.shapiro(con_renewal.SupplierA) #Shapiro test
#pvalue = 0.89 >0.005 Supplier A is Normal

stats.shapiro(con_renewal.SupplierB) #Shapiro Test
stats.shapiro(con_renewal.SupplierC)#Shapiro Test
#0.57 > 0.005 , supplier c is normal
#Varience Test
help(scipy.stats.levene)
#All 3 suppliers are beign checked for variance
scipy.stats.levene(con_renewal.SupplierA , con_renewal.SupplierB , con_renewal.SupplierC)
#THe levene test tests the null hypothesis
#That all input samples from populations with equal variances 
#the pvalue = 0.777 > 0.005 , p is high null fly
#H0 = ALl input samples are from populations with equal variance

#one way Annova
F, p = stats.f_oneway(con_renewal.SupplierA , con_renewal.SupplierB , con_renewal.SupplierC)

#p values
p
#All the 3 suppliers have equal mean transition time

#----------2-propostion test-----------
import numpy as np
two_prop_test = pd.read_excel("C:/Hypothesis/hypothesis_datasets/JohnyTalkers.xlsx")

from statsmodels.stats.proportion import proportions_ztest

tab1 = two_prop_test.Person.value_counts()
tab1 
tab2 = two_prop_test.Drinks.value_counts()
tab2

#crosstable table
pd.crosstab(two_prop_test.Person , two_prop_test.Drinks)

count = np.array([58 , 152])
nobs = np.array([480 , 740])

stats , pval = proportions_ztest(count , nobs , alternative = "two-sided")
print(pval)#pvalue 0.000

stats , pval = proportions_ztest(count , nobs , alternative= "larger")
print(pval) #pvalue = 0.999

#----------chi-Squared Test---------------
Bahaman = pd.read_excel("C:/Hypothesis/hypothesis_datasets/Bahaman.xlsx")
Bahaman

count = pd.crosstab(Bahaman['Defective'] , Bahaman['Country'])
count

Chisquares_results = scipy.stats.chi2_contingency(count)
Chi_square = [['Test Stastics' , 'p-value'] ,[Chisquares_results[0] , Chisquares_results[1]]]

Chi_square













