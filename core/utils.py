import pyperclip as clip
import string
import secrets


def generate_specialString(password_length):
    choices = string.ascii_letters + string.digits + string.punctuation
    generated_string = "".join([secrets.choice(choices) for i in range(password_length)]).replace("|", "#").replace(":", "*")
    return generated_string


def generate_string(password_length):
    choices = string.ascii_letters + string.digits
    generated_string = "".join([secrets.choice(choices) for i in range(password_length)]).replace("|", "#").replace(":", "*")
    return generated_string


def copy_content(string):
    clip.copy(string)


