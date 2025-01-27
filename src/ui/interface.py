class Interface:
    def __init__(self, train_function, generate_function):
        self.train_function = train_function
        self.generate_function = generate_function
        self.greetings = '''Hi! Looking to generate melodies? your are in a right place!
For help, please enter 'H'.\nTo start training the model, please enter 'T'.\nTo generate music, please enter 'G'.\nTo exit the application, enter 'Q' '''

    def mainmenu(self):
        while True:
            print(self.greetings)
            command = input()
            if command == 'H':
                print('Tähän ohjeet')
            elif command == 'T':
                self.trainmenu()
            elif command == 'G':
                self.generatemenu()
            elif command == 'Q':
                print('Bye!')
                break

    def trainmenu(self):
        file = input('Please give the name of the file for training: ')
        deg = input('Then the degree of generation (max 6)')
        self.train_function(file, int(deg))
        print('Model trained')

    def generatemenu(self):
        file = input('Please give the name for generated file.\n If empty, will be music.txt as default. ')
        self.generate_function()