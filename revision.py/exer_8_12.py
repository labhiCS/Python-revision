def sandwich_list(*sandwich_names):
    for i in sandwich_names:
        print(i + " sandwich has been ordered.")

def main():
    sandwich_list('nutella')
    
if __name__ == '__main__':
    main()


