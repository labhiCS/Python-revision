def sandwich_list(*sandwich_names):#pointer
    for i in sandwich_names:
        print(i.title() + " sandwich is being ordered." + "\n")

def main():
    sandwich_list('peeporoni')
    sandwich_list('buff', 'cheesi')
    sandwich_list('chicken', 'veg')

    
if __name__ == '__main__':
    main()