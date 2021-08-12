import os



def main():
    i = 1
    # get the path of the dir where the files are 
    path = 'C:/Users/Atwa/Desktop/sport/'
    for filename in os.listdir(path):
        my_dest= "vid"+ str(i)+".mdp4"
        my_source = path + filename
        my_dest= path + my_dest
        os.rename(my_source, my_dest)
        i = i + 1


if __name__ =='__main__':
    main()