def is_spam(message):
    msg = message.lower()

    if "buy now" in msg or "free money" in msg:
        return True

    # repeated characters
    count = 0
    for i in range(1, len(msg)):
        if msg[i] == msg[i-1]:
            count += 1

    return count > 5

