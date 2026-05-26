'''
costruire applicativo che dialoga con il container docker in mysql
(se non funziona docker sqlite)
serve indirizzo ip macchina locale (192.168.1.14)

ID | IMAGE
1     img.jpg
2     img.jpg
3     img.jpg

ID -> primarykey --> auto increment

utilizzare un ORM
creare seguenti api:
    - mostra tutto contenuto database (get)
    - inserire un nuovo elemento no doppioni --> https://randomfox.ca/floof
            solo img ogni volta che chiami
    - inserire un elemento manualmente -- > {"image","immagine.jpg"}
    - cancellare elemento --> {"img.jpg"} --> T/F
'''

from flask import Flask

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
