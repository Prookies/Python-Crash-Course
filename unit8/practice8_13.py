def build_profile_1(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value

    return profile


user_1 = build_profile_1('xu', 'hua',
                         age=22, adress='Guangzhou',
                         interest='football')
print(user_1)
