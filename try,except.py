list= [1,2,3]

while True : 
    value = input('Position [q to quit] ?')
    if value == 'q' :
        break
    try : 
        position = int(value)
        print(list[position])
    except IndexError as err :
        print('Bad index :', err)
    except Exception as other :
        print('Somthing else broke :',other)
