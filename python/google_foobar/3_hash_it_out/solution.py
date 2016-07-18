def answer(digest):
    message = [0]
    for j in xrange(0, len(digest)):
        for i in xrange(digest[j], 129*255, 256):
            if (i ^ message[j]) % 129 == 0:
                message.append((i^message[j])/129)
                continue
    return message[1:]
