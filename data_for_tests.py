main_data = {
        'text': 'Cat meme',
        'url': 'https://i.pinimg.com/736x/95/0a/2a/950a2ae627971a42a86b7a9b8fc70108.jpg',
        'tags': ["funny", "cats", "work"],
        'info': {"color": ["white", "black"], "objects": ["test", "picture"]}
    }

parameters_for_creating_meme = {
    'text_data': [{'text': 123}, {'text': ' '}, {'text': True}, {'text': { }}],
    'tags_data': [{'tags': 123}, {'tags': ''}, {'tags': True}, {'tags': { }}, {'tags': 'Jack'}],
              }
data_param_creating_meme = [(key, el) for key, nums in parameters_for_creating_meme.items() for el in nums]

parameters_for_change_meme = {
    'url_data': [{'url': ' '}, {'url': True}, {'url': {}}],
    'info_data': [{'info': ''}, {'info': True}, {'info': []}, {'info': 'Jack'}]
}
data_param_change_meme = [(key, el) for key, nums in parameters_for_change_meme.items() for el in nums]

auth_invalid_data = {'name': 123}, {'name': True}, { }
auth_data = {'name': 'Jack'}

data_for_update = {
        'id': 'Jack',
        'text': 'Cat meme',
        'url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRvaL5H038UJ0ZktVJ4Z5jWNLuAQzjRFAjgPw&s',
        'tags': ["funny", "cats", "work"],
        'info': {"color": ["white", "black"], "objects": ["test", "picture"]}
    }