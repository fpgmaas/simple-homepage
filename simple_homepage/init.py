import os

class DirectoryInitiatior:

    def __init__(self, create_directory: bool = True):
        self.create_directory = create_directory

    def init(self):
        if self.create_directory:
            os.mkdir('simple_homepage')

        
        
