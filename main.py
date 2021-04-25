from flask import Flask, render_template, redirect, url_for, request
from github import Github

app = Flask(__name__)
git = Github()


@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        user = request.form['name']
        return redirect(url_for("user", name=user))
    else:
        return render_template('index.html')


@app.route("/user/<name>", methods=['POST', 'GET'])
def user(name):
    if request.method == 'POST':
        user = request.form['name']
        return redirect(url_for(name=user))
    else:
        user = name
        user_data = git.get_user(login=user)
        repos = user_data.get_repos()
        repos_list = []
        stars = 0
        i = 1
        for repo in repos:
            repos_list.append(f"{i}. {repo.name}")
            stars += repo.stargazers_count
            i += 1
        return render_template('user.html', name=user, repos=repos_list, stars=stars)

    # user = "SparkyDoggie"
    # user_object = git.get_user(login=user)
    # repos = user_object.get_repos()
    # for i in range(repos.totalCount):
    #     return render_template("index.html")

    # print(u_data)
    # print(repos.get_page(0))
    # print(repos.totalCount)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
