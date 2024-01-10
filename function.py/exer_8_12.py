def sandwich_list(*sandwich_names):
    for i in sandwich_names:
        print(i.title() + " sandwich is being ordered.")

def main():
    sandwich_list('veg')
    sandwich_list('chicken', 'cheesi')

    
if __name__ == '__main__':
    main()