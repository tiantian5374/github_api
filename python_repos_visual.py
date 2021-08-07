import requests

from plotly.graph_objs import Bar
from plotly import offline

# 执行API调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f'Status code: {r.status_code}')

# 处理结果
response_dict = r.json()
response_dicts = response_dict['items']
repo_names, stars = [], []
for repo_dict in response_dicts:
    repo_names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

# 可视化
data = [{
    'type': 'bar',
    'x': repo_names,
    'y': stars,
}]
my_layout = {
    'title': 'GitHub上最受欢迎的Python项目',
    'xaxis': {'title': 'Repository'},
    'yaxis': {'title': 'stars'},
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='python_repos.html')
