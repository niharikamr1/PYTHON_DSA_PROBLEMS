import streamlit as st

st.title("Password Checker")
st.write("Check your password strength")


def has_min_length(password):
    return len(password) >= 8


def has_uppercase(password):
    for ch in password:
        if ch.isupper():
            return True
    return False


def has_lowercase(password):
    for ch in password:
        if ch.islower():
            return True
    return False


def has_digit(password):
    for ch in password:
        if ch.isdigit():
            return True
    return False


def has_special_char(password):
    special = "!@#$%^&*"
    for ch in password:
        if ch in special:
            return True
    return False


def analysePassword(password):

    flag = 0
    failed = []

    if has_min_length(password):
        flag += 1
    else:
        failed.append("Minimum 8 characters required")

    if has_uppercase(password):
        flag += 1
    else:
        failed.append("Uppercase letter missing")

    if has_lowercase(password):
        flag += 1
    else:
        failed.append("Lowercase letter missing")

    if has_digit(password):
        flag += 1
    else:
        failed.append("Digit missing")

    if has_special_char(password):
        flag += 1
    else:
        failed.append("Special character missing")


    if flag <= 2:
        strength = "Weak"
    elif flag == 3:
        strength = "Medium"
    else:
        strength = "Strong"

    return strength, flag, failed


password = st.text_input("Enter Password:", type="password")


if st.button("Analyse Password"):

    if password == "":
        st.warning("Please enter a password")

    else:
        strength, flag, failed = analysePassword(password)

        st.subheader("Result")
        st.success(f"Strength: {strength}")
        st.info(f"Flags: {flag}/5")

        # Progress bar
        st.progress(flag/5)

        if failed:
            st.warning("Failed Checks:")
            for item in failed:
                st.write("-", item)
        else:
            st.success("All checks passed")