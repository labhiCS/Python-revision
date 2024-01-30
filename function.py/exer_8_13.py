def build_profile(first, last, **user_info):
    profile = {
        'first name': first,
        'last name': last,
    }
  
    for key, value in user_info.items():
        profile[key] = value
    return profile

def main():
    user_info = build_profile('abhishek', 'lamichhane', age = 21,address = 'kharibot', profile = 'student')
    user_info2 = build_profile('anup', 'thapa', age = 26)
     
    print(user_info)
    print("\n")
    print(user_info2)

if __name__ == '__main__':
    main()