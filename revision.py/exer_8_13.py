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
    user_info = build_profile('abhishek', 'bahadur', 'lamichhane', age = 19, profile = 'student')
    print(user_info)
    print("\n")

if __name__ == '__main__':
    main()