from ToolGUI import ToolClient



def main():
    client = ToolClient()
    print('assigned client')
    client.tool_menu()
    print('client ran')

if __name__ == '__main__':
    main()
