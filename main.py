from flask import Flask

import test

app = Flask(__name__)


@app.route("/")
def page_index():
    page_content = ""

    candidates = test.get_candidate_all()
    page_content = test.build_preformatted_list(candidates)
    return page_content


@app.route("/candidate/<int:uid>")
def page_candidate(uid):
    candidate = test.get_candidate_by_id(uid)
    candidates = [candidate]
    page_content = test.build_preformatted_list(candidates)
    return page_content

@app.route("/skill/<skill_name>")
def page_skill(skill_name):

    candidates = test.get_candidates_by_skill(skill_name)

    page_content = test.build_preformatted_list(candidates)
    return page_content

app.run()
