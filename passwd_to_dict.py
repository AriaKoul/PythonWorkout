def passwd_to_dict(filename):
    users = {}
    f = open(filename)
    with f as passwd:
        for line in passwd:
            if not line.startswith(('#', '\n')):
                user_info = line.split(':')
                users[user_info[1]] = int(user_info[2])
    return users

print(passwd_to_dict('/etc/passwd'))
