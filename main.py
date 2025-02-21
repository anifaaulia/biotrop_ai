from components.Header import *
from components.Main import *
from dotenv import load_dotenv


load_dotenv()

def main():

    Header()
    Main()

if _name_ == "_main_":
    main()
