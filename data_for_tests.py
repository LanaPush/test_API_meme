main_data = {
        'text': 'Cat meme',
        'url': 'https://i.pinimg.com/736x/95/0a/2a/950a2ae627971a42a86b7a9b8fc70108.jpg',
        'tags': ["funny", "cats", "work"],
        'info': {"color": ["white", "black"], "objects": ["test", "picture"]}
    }

parameters = {
    'text_data': [{'text': 123}, {'text': ' '}, {'text': True}, {'text': { }}],
    'tags_data': [{'tags': 123}, {'tags': ''}, {'tags': True}, {'tags': { }}, {'tags': 'Jack'}],
              }
data_param = [(key, el) for key, nums in parameters.items() for el in nums]

auth_invalid_data = {'name': 123}, {'name': True}, { }
auth_data = {'name': 'Jack'}