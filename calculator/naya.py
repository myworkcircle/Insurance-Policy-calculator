# #rate
    # n3 = cal.insurance_coverage
    # rate = n3/1000
    
    # #time
    # d_time = cal.tenure
    # n1 = cal.dob
    # n1 = str(n1)
    # n1 = n1[:4]
    # n1 = int(n1)
    # n2 = datetime.date.today().year
    # d_age = n2 - n1 
    
    # #premium_rate
    # premium_rate_val1 = company1.objects.get(age__contains=d_age,tenure__contains=d_time)
    # premium_rate_val2 = company2.objects.get(age__contains=d_age,tenure__contains=d_time)
    # premium_rate_val3 = company3.objects.get(age__contains=d_age,tenure__contains=d_time)
    # premium_rate_val4 = company4.objects.get(age__contains=d_age,tenure__contains=d_time)
    # premium_rate1 = premium_rate_val1.value
    # premium_rate2 = premium_rate_val2.value
    # premium_rate3 = premium_rate_val3.value
    # premium_rate4 = premium_rate_val4.value

    # #mode
    # n4 = cal.mode
    
    # if n4=="Annual":
    #     p_rate1=premium_rate1-2
    #     p_rate2=premium_rate2-2
    #     p_rate3=premium_rate3-2
    #     p_rate4=premium_rate4-2
    # if n4=="Half Yearly":
    #     p_rate1=premium_rate1-1
    #     p_rate2=premium_rate2-1
    #     p_rate3=premium_rate3-1
    #     p_rate4=premium_rate4-1
    # if n4=="Quarterly":
    #     p_rate1=premium_rate1
    #     p_rate2=premium_rate2
    #     p_rate3=premium_rate3
    #     p_rate4=premium_rate4
    # if n4=="Monthly":            
    #     p_rate1=premium_rate1
    #     p_rate2=premium_rate2
    #     p_rate3=premium_rate3
    #     p_rate4=premium_rate4
    
    # print(p_rate1,p_rate2,p_rate3,p_rate4)
    # #premium
    # premium1 = p_rate1*rate
    # premium2 = p_rate2*rate
    # premium3 = p_rate3*rate
    # premium4 = p_rate4*rate