def validate_if_email_is_string(email):
    if type(email) != str:
        raise TypeError("Email should be a string")


def validate_username(username):
    special_chars = ["_", "-"]

    if not username[0].isalpha():
        raise ValueError("First char in username should be a letter")

    for char in username:
        if not char.isalpha() and not char.isdigit() and char not in special_chars:
            raise ValueError(
                "Username should contain only letters, digits, dashes or underscores"
            )


def validate_provider(provider):
    for char in provider:
        if not char.isalpha() and not char.isdigit():
            raise ValueError("Provider should contain only letters or digits")


def validate_extension(extension):
    if not len(extension) == 3:
        raise ValueError("Extension length should by 3")


def split_email(email):
    try:
        user = email.split("@")[0]
        provider = email.split("@")[1].split(".")[0]
        extension = email.split("@")[1].split(".")[1]

        return user, provider, extension
    except IndexError:
        print("Email is invalid")


def validate_email(email):
    validate_if_email_is_string(email)

    user, provider, extension = split_email(email)

    validate_username(user)
    validate_provider(provider)
    validate_extension(extension)

    return True


def filter_valid_email(email_list):
    valid_email_list = []

    for email in email_list:
        try:
            validate_email(email)
        except ValueError as exc:
            print(exc)
        else:
            valid_email_list.append(email)

    return valid_email_list


# By ChatGPT
# def filter_valid_email(email_list):
#     return [email for email in email_list if validate_email(email) is None]
