messages = ['one', 'two', 'three']
sent = []

def send_message(messages):
    while messages:
        message = messages.pop()
        sent.append(message)
    return messages

print(send_message(messages))
print(sent)
