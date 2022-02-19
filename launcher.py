from ToolGUI import ToolClient

def main():
    client = ToolClient().tool_menu()
    print('assigned client')
    client()
    print('client ran')

if __name__ == '__main__':
    main()