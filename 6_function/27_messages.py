messages = [
    "How are you?",
    "Are you good?",
    "How's it going?",
    "I am fine.",
    ]
sent_messages = []

def show_messages(message_list):
    """显示所有信息"""
    for message in message_list:
        print(message)

def send_messages(message_to_send, sent_list):
    """发送信息，同时保留原始列表"""
    while message_to_send:
        current_messages = message_to_send.pop()
        print(f"Sending: {current_messages}")
        sent_list.append(current_messages)

# 显示原始列表信息
show_messages(messages)
# 使用切片副本发送信息
send_messages(messages[:], sent_messages)

print("\nOriginal messages list:")
show_messages(messages)

print("\nSent messages list:")
show_messages(sent_messages)
