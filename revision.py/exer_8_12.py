def sandwich_list(*sandwich_names):
    for i in sandwich_names:
        print(i + " sandwich has been ordered.")
        print("\n")

def main():
    sandwich_list('nutella')
    sandwich_list('veg', 'cheesi')
    sandwich_list('chicken', 'grilled')
    
if __name__ == '__main__':
    main()


