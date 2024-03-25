def build_profile(first, last, middle,  **user_info):
    profile = {
        'first name': first,
        'middle name': middle,
        'last name': last,
    }
  
    for key, value in user_info.items():
        profile[key] = value
    return profile

def main():
    user_info = build_profile('Abhishek', 'Lamichhane', 'Bahadur', age = 19, profile = 'student')
    print(user_info)
    stunent_info1 = build_profile('Abhijeet', 'Thapa', 'Bikram', profile = 'student', Address = 'Kharibot')
    print(stunent_info)
    print("\n")
    stunent_info2 = build_profile('Anusha', 'Thapa', Address = 'USA')
    print(stunent_info2)

if __name__ == '__main__':
    main()