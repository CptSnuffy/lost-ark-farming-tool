from ToolGUI import ToolClient

#Run this file in a directory with the other two py files to run the program

def main():
    client = ToolClient().tool_menu()
    print('assigned client')
    client()
    print('client ran')

if __name__ == '__main__':
    main()