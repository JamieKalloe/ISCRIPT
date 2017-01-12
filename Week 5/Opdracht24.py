import shutil

"""
    Auteur: Jamie Kalloe - Michael van Kampen
"""
def main():
    copy('origineel.txt', 'kopie.txt')
    copy('shaw.txt', 'shaw2.txt')

def copy(source, destination, buffer_size=16000):
    with open(source, 'rb') as source:
        with open(destination, 'wb') as location:
            shutil.copyfileobj(source, location, buffer_size)

main()